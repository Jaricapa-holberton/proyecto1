"""Platzigram URLs module."""

# Django apps
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# Created apps
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    # urls for learn django
    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),
    # app urls
    path('admin/', admin.site.urls),
    path('posts/', posts_views.list_posts, name='feed'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
