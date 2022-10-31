from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ModeForm
from . models import products
from django import forms
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
def add_product(request):
    print("hai")
    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        if request.POST.get('offer')== 'on':
            offer = True
        else:
            offer = False
        print(offer)
        print(name)
        p = products(name=name,price=price,desc=desc,image=image,offer=offer)
        p.save()
        print("product added")
    return  render(request,'add_product.html')
def update(request,product_id):
    obj = products.objects.get(id=product_id)
    form = ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html')


