from django.http import HttpResponse
from django.shortcuts import render
from . models import products
# Create your views here.
def demo(request):
    product = products.objects.all()
    for p in product:
        print(p.name)
        print(p.image)
    return render(request,'index.html',{'products':product})

def single_product(request,product_id):
    product1=products.objects.get(id=product_id)
    return render(request,'single-product.html',{'product':product1})
