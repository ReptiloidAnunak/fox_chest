from django.contrib import admin

from core.models import User
from bot.models import TgUser
from store.models import Brand, Bodysuit, TShort, Pants, Jacket
from sales.models import Order


class TgUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'tg_user_id')
    list_filter = ('username', 'last_name')


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

admin.site.register(Order, OrderAdmin)


