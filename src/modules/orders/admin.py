from django.contrib import admin
from .models import Order


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'order', 'price_in_dollars', 'price_in_rubles', 'delivery_date')

    list_filter = ('delivery_date', )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'number',
                    'order',
                    ('price_in_dollars',
                    'price_in_rubles'),
                    'delivery_date',
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                )
            }
        ),
    )

    search_fields = ('number', 'order')

    readonly_fields = ('created_date', 'changed_date',)
