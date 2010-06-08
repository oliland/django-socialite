from django.contrib import admin
from oauth_access.models import UserAssociation

class UserAssociationAdmin(admin.ModelAdmin):
    list_display = ('user','name','service','identifier','expires')
    list_filter = ('service',)
    search_fields = ['user__username','user__first_name','user__last_name','identifier']
    
    def name(self, obj):
        return "%s %s" % (obj.user.first_name, obj.user.last_name)
        
admin.site.register(UserAssociation, UserAssociationAdmin)
