from django.contrib import admin

from .models import Flat, Claim


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('price', 'new_building', 'construction_year',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)
    list_display = ('text',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)