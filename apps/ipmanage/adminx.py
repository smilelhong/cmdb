import xadmin
from ipmanage.models import IPRange,IPAddress

class IPRangeAdmin(object):
    list_display = ["start_ip", "end_ip", "use_ip", "left_ip", "desc", "create_time"]



xadmin.site.register(IPRange, IPRangeAdmin)