from django.conf.urls import url
# from django.contrib import admin
from ipmanage.views import Index,Iprange
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'/ip_range_list/$', Iprange.as_view(), name='ip_range_list'),
    url(r'/ip_range_add/$', Iprange.as_view(), name='ip_range_add'),
]
