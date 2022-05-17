from django.contrib import admin

# Register your models here.

from .models import Tag, Photo

admin.site.register(Tag)
admin.site.register(Photo)
