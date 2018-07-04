"""amadoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ecommerceapp.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^cart/$',cart,name='cart'),
    url(r'^checkout/$',checkout,name='checkout'),
    url(r'^product-details/(\d+)/$',product_details,name='detail'),
    url(r'^shop/$',shop,name='shop'),
    url(r'^shop/(\w+)/$',single_category,name='category'),
    url(r'^login/$',login,name='login'),
    url(r'^signup/$',sign_up,name='signup'),
    url(r'^auth-check/$',auth_view,name='check'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^search/$',search,name='search'),
    url(r'^delete/(\d+)$',delete,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
