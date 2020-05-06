from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from order.models import ShopCart, ShopCartForm
from product.models import Category


def index(request):
    return HttpResponse("Order App")

@login_required(login_url='/login') #login durumu kontrol edilir
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')#urli alır
    current_user = request.user #Access User Session Information

    checkproduct = ShopCart.objects.filter(product_id = id)
    if checkproduct:
        control = 1 #ürün sepette var
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid:
            if control==1:#ürün varsa güncelle
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request,"Ürün başarı ile sepete eklenmiştir.Teşekkür Ederiz..")
        return HttpResponseRedirect(url)
    else:#sepete ekleye basılınca
        if control == 1:  # ürün varsa güncelle
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart() #model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request,"Ürün başarı ile sepete eklenmiştir.Teşekkür Ederiz..")
            return HttpResponseRedirect(url)

    messages.warning(request,"Ürün sepete eklemede hata oluştu! Lütfen kontrol ediniz...")
    return HttpResponseRedirect(url)

@login_required(login_url='/login') #login durumu kontrol edilir
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session Information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    total =0
    for rs in shopcart:
        total += rs.product.price * rs.quantity

    context = {'shopcart':shopcart,
               'category':category,
               'total':total,
              }
    return render(request,'Shopcart_products.html',context)

@login_required(login_url='/login') #login durumu kontrol edilir
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Ürün Sepetten Silindi...")
    return HttpResponseRedirect("/shopcart")
