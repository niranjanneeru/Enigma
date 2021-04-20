from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedTabularInline

from csi_localhost.response.models import Response
from .models import Profile


class ResponseAdmin(NestedTabularInline):
    model = Response
    fields = ('question', 'answer', 'create_date', 'status')
    extra = 0


class ProfileAdmin(NestedModelAdmin):
    inlines = [ResponseAdmin]
    search_fields = ['name', 'college', 'nick_name', 'marks']
    list_display = ['name', 'marks', 'college']
    list_filter = ['marks']


admin.site.register(Profile, ProfileAdmin)
