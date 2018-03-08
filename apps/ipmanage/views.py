from django.shortcuts import render
from django.views import View

from datetime import datetime
from netaddr import  *

from ipmanage.models import IPRange
# Create your views here.


class Index(View):

    def get(self, request, *args, **kwargs):
        path = request.path
        return render(request, 'ipmanage/base.html',locals())


class Iprange(View):

    def get(self, request, *args, **kwargs):
        path = request.path
        if path == '/ipmanage/ip_range_list/':
            ip_range_all = IPRange.objects.all()
            return render(request, 'ipmanage/ip_range_list.html', locals())
        elif path == '/ipmanage/ip_range_add/':
            return render(request, 'ipmanage/ip_range_add.html',locals())

    def post(self,request, *args, **kwargs):
        start_ip = request.POST.get("start_ip")
        end_ip = request.POST.get("end_ip")
        desc = request.POST.get("des")
        create_time = datetime.now()
        ip_list = list(iter_iprange(start_ip, end_ip))
        obj = IPRange(start_ip=start_ip,end_ip=end_ip,desc=desc,use_ip=0,left_ip=len(ip_list),create_time=create_time)
        obj.save()
        return render(request, 'ipmanage/ip_range_add.html')


