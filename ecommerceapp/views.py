from django.shortcuts import *
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db.models import Q
# Create your views here.
def index(request):
    category=Categories.objects.all()
    return render(request,'index.html',{'cat':category})
def shop(request):
    category=Categories.objects.all()
    default_category='chair'
    all_product=Product.objects.filter(category__slug = default_category)
    return render(request,'shop.html',{'cat':category,'pro':all_product,'d':default_category})
def single_category(request,slug):
    category=Categories.objects.all()
    default_category=slug
    all_product=Product.objects.filter(category__slug = default_category)
    return render(request,'shop1.html',{'cat':category,'pro':all_product,'d':slug})
def product_details(request,d):
    product = Product.objects.get(id=d)
    if request.method=='POST':
        form=Cartform(request.POST)
        all_items=Cart.objects.all()
        cart_data={}
        for i in all_items:
            cart_data[i.product.id]={'product':i.product,'quantity':i.quantity}
        q = request.POST['quantity']
        if form.is_valid():
            if int(d) in cart_data.keys():
                c=Cart.objects.get(product__id=d)
                c.quantity += int(q)
                c.total_price += float(c.product.price)* float(q)
                c.save()
            else:
                f=form.save(commit=False)
                f.product=product
                f.quantity=q
                f.total_price=float(product.price) * float(q)
                f.save()

            return HttpResponseRedirect('/cart/')
    else:
        form = Cartform()
    return render(request,'product-details.html',{'detail':product,'form':form})
def cart(request):
    all_items=Cart.objects.all()
    total=[]
    for i in all_items:
        total.append(i.total_price)
    return render(request,'cart.html',{'all_items':all_items,'sum':sum(total)})
@login_required(login_url="/login/")
def checkout(request):
    return render(request,'checkout.html')
def login(request):
    return render(request,"index0.html")
def sign_up(request):
    if request.method=="POST":
        form=Info_form(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            u= User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            p=Info(user=u,pic=form.cleaned_data['pic'])
            p.save()
            return redirect('login')
    else:
        form=Info_form()
    return render(request,"signup1.html",{'form':form})
def auth_view(request):
    #print request.POST,type(request)
    username=request.POST['username']
    password=request.POST['password']
    #match username & password
    #if not match,authenticate() will return None
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('checkout')
    else:
        return HttpResponseRedirect('/invalid/')
def logout(request):
     auth.logout(request)
     return HttpResponseRedirect('/')

def search(request):
    if request.method=="POST":
        s=request.POST.get('search')
        s=Product.objects.filter(name__icontains=s)
        if s:
            return render(request,'search.html', {'q':s})
        else:
            return render(request,'search.html', {'msg':'not found'})

def delete(request,d):
    item=Cart.objects.get(id=d)
    item.delete()
    return HttpResponseRedirect('/cart/')
