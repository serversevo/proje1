from django.db import models

# Create your models here.
from django.forms import TextInput, ModelForm, Textarea


class Setting(models.Model):
    STATUS = (  # açılan kutu
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppasword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)  # sadece ekleme zamnında tarih için
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  # titleyi döndürecek

class ContactFormMessage(models.Model):
    STATUS = (
            ('New', 'New'),
            ('Read', 'Read'),
            ('Closed', 'Closed')
    )

    name = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS, max_length=10, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage#hangi modele ait
        fields = ['name', 'email', 'subject', 'message']#formda görülecek elemanlar
        widgets = {#ayrıntı ayarları,  içinde yazacaklar
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email' : TextInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
            'message' : Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }