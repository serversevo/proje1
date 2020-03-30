from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (#açılan kutu
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)

    slug = models.SlugField()#metinsel çağırım için metin değişkeni
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)#on_delete=models.CASCADE silme işleminde ona ait alt sınıfın silinmesini sağlar
    create_at = models.DateTimeField(auto_now_add=True)#sadece ekleme zamnında tarih için
    update_at = models.DateTimeField(auto_now=True)#her zaman tarih eklmesi için, hem güncelleme hem ekleme

    def __str__(self):
        return self.title#titleyi döndürecek

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Product(models.Model):
    STATUS = (#açılan kutu
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#relation with Category table
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)  # sadece ekleme zamnında tarih için
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title#titleyi döndürecek

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)#on_delete product silindiğinde imagesların silinmesi için
    title = models.CharField(max_length=70, blank=True)#blank= true boş geçilebilmesi için
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title  # titleyi döndürecek
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
