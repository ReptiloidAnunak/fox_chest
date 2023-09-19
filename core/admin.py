from django.contrib import admin

from core.models import User
from store.models import Brand, Bodysuit, TShort, Pants, Jacket
import store.models as store_models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('name', 'country')
    list_per_page = 20


class BodysuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class TShortAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class PantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class JacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


admin.site.register(User)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Bodysuit, BodysuitAdmin)
admin.site.register(TShort, TShortAdmin)
admin.site.register(Pants, PantsAdmin)
admin.site.register(Jacket, JacketAdmin)


