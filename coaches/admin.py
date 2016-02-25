from django.contrib import admin
from django.contrib.auth.models import User
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ['first_name','last_name','gender', 'skype', 'description']

    def first_name(self, obj):
    	return obj.user.first_name
    	
    def last_name(self, obj):
    	return obj.user.last_name

admin.site.register(Coach, CoachAdmin)

