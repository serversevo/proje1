from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images

class ProductImageInline(admin.TabularInline):#ımages tablosundan 5 tane resim oluşacak şekilde alan oluştur
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']#hangi sutunların gözükeceğini belirtik
    list_filter = ['status']#status durumuna göre listelenecek
    readonly_fields = ('image_tag',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)