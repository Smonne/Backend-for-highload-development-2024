from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from blog_app.models import User, Post, Comment, Tag

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
