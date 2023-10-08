from django.contrib import admin

from core.models import User
from bot.models import TgUser
from store.models import (Brand, Bodysuit, TShort, Pants, Jacket, Overall, ClothingSet,
                          Robe, LongSleeve, Underwear, SocksTights, Sweatshirt, Doll, Angel, Family)
from sales.models import Order


class TgUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'tg_user_id')
    list_filter = ('username', 'last_name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('name', 'country')
    list_per_page = 20


class BodysuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class TShortAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class PantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class JacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class OverallAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class ClothingSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class RobeAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class LongSleeveAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class UnderwearAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class SocksTightsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class SweatshirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'color', 'material', 'sex', 'age', 'brand', 'price', 'quantity')
    list_filter = ('color', 'sex', 'brand', 'price')
    list_per_page = 20


class DollAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'price', 'number_of_figures')
    list_filter = ('name', 'material', 'price', 'number_of_figures')
    list_per_page = 20


class AngelAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'price', 'number_of_figures')
    list_filter = ('name', 'material', 'price', 'number_of_figures')
    list_per_page = 20


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'price', 'number_of_figures')
    list_filter = ('name', 'material', 'price', 'number_of_figures')
    list_per_page = 20


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_user', 'executor', 'status', 'created')
    list_filter = ('tg_user', 'executor', 'status', 'created')
    list_per_page = 20


admin.site.register(User)
admin.site.register(TgUser, TgUserAdmin)

admin.site.register(Brand, BrandAdmin)

admin.site.register(Bodysuit, BodysuitAdmin)
admin.site.register(TShort, TShortAdmin)
admin.site.register(Pants, PantsAdmin)
admin.site.register(Jacket, JacketAdmin)
admin.site.register(Overall, OverallAdmin)
admin.site.register(ClothingSet, ClothingSetAdmin)
admin.site.register(Robe, RobeAdmin)
admin.site.register(LongSleeve, LongSleeveAdmin)
admin.site.register(Underwear, UnderwearAdmin)
admin.site.register(SocksTights, SocksTightsAdmin)
admin.site.register(Sweatshirt, SweatshirtAdmin)


admin.site.register(Doll, DollAdmin)
admin.site.register(Angel, AngelAdmin)
admin.site.register(Family, FamilyAdmin)

admin.site.register(Order, OrderAdmin)


