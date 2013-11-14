from django.contrib import admin
from mv_test.models import *

class MVProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_agent',)
    #list_filter = ('status_code','view_name')
    search_fields = ('user__username','user_agent',)
    
admin.site.register(Group)
admin.site.register(Variation)
admin.site.register(MVProfile, MVProfileAdmin)
admin.site.register(Goal)
admin.site.register(Success)

