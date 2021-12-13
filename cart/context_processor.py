from . models import *
from . views import *

def count(request):
    item_count=0
    if 'admin' in request.path:
        return{}
    else:
        try:
            ct=cartlist.objects.filter(cart_ID=ca_id(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.qnty
        except cartlist.DoesNotExist:
            item_count=0
        return dict(itc=item_count)