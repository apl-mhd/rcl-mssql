from django.contrib import admin
from . models import *

admin.site.register(ORDER_MASTER)
admin.site.register(ORDER_DETAILS)
admin.site.register(RETURN_REQ_MASTER)
admin.site.register(RETURN_REQ_DETAILS)