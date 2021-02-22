from django.contrib import admin
from . import models
# Register your models here.


#admin.site.register(models.Article)
#admin.site.register(models.Comment)

class CommentInLine(admin.StackedInline):
    model = models.Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
