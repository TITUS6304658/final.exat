from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *





admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(home)
admin.site.register(project)
admin.site.register(contract)
admin.site.register(title)
admin.site.register(owner)
admin.site.register(result)
admin.site.register(system_action)
