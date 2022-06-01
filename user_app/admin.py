from django.contrib import admin
from . models import User,UserAccount
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # list_display = ('id', )
     fields = ['login_name','first_name', 'email', 'admin']

admin.site.register(User, UserAdmin)
admin.site.register(UserAccount)
