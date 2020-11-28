from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(DailyTask)
admin.site.register(Leave)
admin.site.register(TodoList)
admin.site.register(Department)
admin.site.register(Profile)
