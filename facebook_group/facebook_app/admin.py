from django.contrib import admin
from facebook_app.models import *

# Register your models here.

admin.site.register(Users)
admin.site.register(FacbookGroup)
admin.site.register(GroupMembers)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Replies)

