from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    )
    list_editable = ('price', 'new_building', 'construction_year',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline, ]


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)
    list_display = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'phonenumber', 'pure_phonenumber',)
