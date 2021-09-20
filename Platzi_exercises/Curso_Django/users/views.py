"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.user.is_authenticated:
                return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

def signup_view(request):
    '''Signup view'''

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        # Por si a alguno le pasó que le dio un Multikey value error, les dejo la solución en Django 3.0 para los métodos de post: - .get() -
        password = request.POST.get('passwd', True)
        password_confirm = request.POST.get('passwd_confirmation', True)

        # PASSWORD VALIDATION
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})
        
        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})
        
        # USERNAME VALIDATION 
        try:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()

            profile = Profile(user=user)
            profile.save()

            login(request, user)
            return redirect('feed') # CAMBIAR >> Redireccionar a completar perfil
        except IntegrityError as ie:
            error = f'There is another account using {username}'
            return render(request, 'users/signup.html', {'error': error})

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')