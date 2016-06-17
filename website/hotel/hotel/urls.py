"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns,url,include
from django.contrib import admin
from hotel.views import hotel,transportation,contact,taipei,home,taipei101,cks,museum,yehliu,yms,huashan,xingtian,tamsui,chiufen,longshan 

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^taipei/$',taipei),

    url(r'^taipei/home.html$',home),
    url(r'^taipei/hotel.html$',hotel),
    url(r'^taipei/transportation.html$',transportation),
    url(r'^taipei/contact.html$',contact),
    url(r'^taipei/taipei101.html$',taipei101),
    url(r'^taipei/Chiang Kai-shek Memorial Hall.html$',cks),
    url(r'^taipei/National Palace Museum.html$',museum),
    url(r'^taipei/Yeh Liu Geo Park.html$',yehliu),
    url(r'^taipei/Yangmingshan National Park.html$',yms),
    url(r'^taipei/Huashan 1914 Creative Park.html$',huashan),
    url(r'^taipei/xingtian temple.html$',xingtian),
    url(r'^taipei/Tamsui.html$',tamsui),
    url(r'^taipei/Chiufen.html$',chiufen),
    url(r'^taipei/Longshan Temple.html$',longshan),


    
)
