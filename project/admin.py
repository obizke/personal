from django.contrib import admin

# Register your models here.
from project.models import Post, Category,Jwear, Comment


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Post)
admin.site.register(Jwear)
admin.site.register(Comment)