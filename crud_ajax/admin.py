from django.contrib import admin
from . models import CrudUser

@admin.register(CrudUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','address','age']