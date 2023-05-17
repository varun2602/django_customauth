from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from . import models 

class UserAdminManager(UserAdmin):
    list_display = ['email', 'user_name', 'password', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ('email', 'user_name', 'is_staff')
    search_fields = ('email', 'user_name')
    ordering  = ('email',)
    fieldsets = (
        (None, {'fields':('email', 'username')}),
        ('Personal', {'fields':('about',)})
    )
    # formfield_overrides = {
    #     models.CustomUser.about: {'widget':Textarea(attrs = {'rows':10, 'cols':40})}
    # }
admin.site.register(models.CustomUser, UserAdminManager)
