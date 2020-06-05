from django.contrib import admin
from .models import Comment,Post
from mediumeditor.admin import MediumEditorAdmin
# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Post)
class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):
    mediumeditor_fields = ('text', )