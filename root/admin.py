from django.contrib import admin
from .models import *
# Register your models here.
class BoxProductInline(admin.TabularInline):
    model = Box.products.through
    extra = 1

class BoxSpinInline(admin.TabularInline):
    model = BoxSpin
    extra = 1

class PrizeInline(admin.TabularInline):
    model = Prize
    extra = 1

class BoxAdmin(admin.ModelAdmin):
    inlines = [
        BoxProductInline,
    ]
    exclude = ('products','slug',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        BoxProductInline,
    ]
    exclude = ('boxes','slug',)

class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        BoxSpinInline,
        PrizeInline,
    ]
    exclude = ('boxes_spin','prizes',)

admin.site.register(Category)
admin.site.register(Box,BoxAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(BoxSpin)
admin.site.register(Prize)
admin.site.register(SpinNumber)
admin.site.register(Message)
admin.site.register(Classification)