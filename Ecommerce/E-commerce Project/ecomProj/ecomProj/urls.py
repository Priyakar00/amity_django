"""
URL configuration for ecomProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ecomApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('About_Us',views.about),
    # path('Service_Us',views.services),
    path('Contact_Us',views.contact),
    path('Gallery_Us',views.gallery),
    path('Pricing_Us',views.pricing),

    path('Product_Us',views.products),
    path('single_product_details/<id>',views.single_details),

    path('cart',views.carts),
    path('Cart_Us',views.cartdisplay),

     path('remove/<kslug>',views.remove_cart),

     path('Signup_Us',views.signup),

     path('Login_Us',views.login),

     path('signUp',views.signup1),

     path('UserName',views.username),

     path('UserLogout',views.userlogout),

     path('Checkout',views.checkout_fun),

     path('callback',views.callback),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
