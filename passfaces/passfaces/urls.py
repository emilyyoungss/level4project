from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'passfaces.views.home', name='home'),
    # url(r'^passfaces/', include('passfaces.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^faces/', include('faces.urls'))
]    
