"""Posts views definitions"""
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

#global variable
posts = [
            {
                'title': 'Mont Blanc',
                'user': {
                    'name': 'Yésica Cortés',
                    'picture': 'https://picsum.photos/60/60/?image=1027'
                },
                'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
                'photo': 'https://picsum.photos/800/600?image=1036',
            },
            {
                'title': 'Via Láctea',
                'user': {
                    'name': 'Christian Van der Henst',
                    'picture': 'https://picsum.photos/60/60/?image=1005'
                },
                'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
                'photo': 'https://picsum.photos/800/800/?image=903',
            },
            {
                'title': 'Nuevo auditorio',
                'user': {
                    'name': 'Uriel (thespianartist)',
                    'picture': 'https://picsum.photos/60/60/?image=883'
                },
                'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
                'photo': 'https://picsum.photos/500/700/?image=1076',
            }
        ]

def list_posts1(request):
    """A Django view that list all posts using only code and path in url"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
        # se desempaqueta todo el diccionario de una vez con kwargs en vez de poner arg por arg: name=post['name']
    return HttpResponse('<br>'.join(content))

def list_posts2(request):
    """A Django view that list all posts using templates"""
    return render(request, 'feed.html', {'posts': posts})
