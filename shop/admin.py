from django.contrib import admin
from .models import Product, Order
# Register your models here.


#modification for admin
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

#making table and search fiel
class ProductAdmin(admin.ModelAdmin):

    #define action
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    #making table in admin
    list_display=('title','price','discount_price','category','description','image')

    #search field
    search_fields = ('title','category')

    #action
    actions  = ('change_category_to_default',)

    #editable

    list_editable = ('price',)




admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
