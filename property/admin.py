from django.contrib import admin

from .models import Flat, Claim, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ['created_at']
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('price', 'new_building', 'construction_year',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)
    list_display = ('text',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name','phonenumber', 'pure_phonenumber',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
