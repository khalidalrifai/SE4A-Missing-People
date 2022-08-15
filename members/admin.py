from django.contrib import admin

from .models import Lost, Find, Members

@admin.register(Lost)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'Name','photo','date']

@admin.register(Find)
class ImageAdmin2(admin.ModelAdmin):
    list_display = ['id' ,'photo','date']

@admin.register(Members)
class ImageAdmin3(admin.ModelAdmin):
    list_display = ['id' ,'Username','Password','Email']

