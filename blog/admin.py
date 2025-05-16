from django.contrib import admin
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display =('name','email','post','created_at','approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name','email','body')


admin.site.register(Post)
admin.site.register(Comment,CommentAdmin)