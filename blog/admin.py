from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInline]      # прекрепляет создание рецепта в создании поста
    save_as = True                # дублирует нижние кнопки сохранения-удаления модели вверх
    save_on_top = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']


@admin.register(models.Banner)
class BanerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'get_image']
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
