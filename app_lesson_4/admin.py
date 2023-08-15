from django.contrib import admin
from .models import Advertisements
from django.utils.html import format_html


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date', 'created_image', 'user']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    def preview(self, obj):
        return format_html(
                '<a href="{}"><img src="{}" style="max-height: 200px;"></a>', obj.image.url, obj.image.url
        )
    preview.short_description = 'Выбранный файл'

    readonly_fields = ('preview',)

    fieldsets = (
        ('Общие', {'fields': ('title', 'description', ('image', 'preview'), 'user')}),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
            })
    )


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements, AdvertisementsAdmin)

# Register your models here.
