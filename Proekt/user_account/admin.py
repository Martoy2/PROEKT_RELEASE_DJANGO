from django.contrib import admin
from .models import NewUser, CheckPayment, Course
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput


class UserAdminConfig(UserAdmin):
   search_fields = ('email',)
   list_filter = ('email', 'is_active', 'is_staff', 'subscribe',)
   ordering = ('-start_date', )
   list_display = ('email', 'is_active', 'is_staff', 'subscribe', 'subscribe_date', 'start_date', 'balance',)

   fieldsets = (
      (None, {'fields':('email', 'password', 'start_date', 'user_image',)}),
      ('Состояние', {'fields':('balance', 'subscribe', 'subscribe_date')}),
      ('Права', {'fields':('is_active', 'is_staff')}),
   )

   add_fieldsets = (
      (None, {
         'classes': ('wide',),
         'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
       ),
   )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(CheckPayment)
admin.site.register(Course)