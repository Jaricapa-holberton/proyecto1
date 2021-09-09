"""User admin classes."""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from users.models import Profile

# see class 16 for more info
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    # set the properties of the users in the admin page
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # set few properties as hyperlink
    list_display_links = ('pk', 'user')
    # set few properties as editable fields
    list_editable = ('phone_number', 'website', 'picture')
    # allow to admin search fields
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_numer')
    # allow to admin filter fields
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')
    # set the visual fields for input data when create a new profile
    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
    readonly_fields = ('created','modified')
"""
Une los modelos de usuario y perfil para no tener que crear un usuario para asociarlo con un perfil
"""
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(UserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
admin.site.unregister(User)
admin.site.register(User,UserAdmin)