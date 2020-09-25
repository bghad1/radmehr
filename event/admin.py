from django.contrib import admin
from .models import EventType, Event


class EventTypeAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    list_display = "title", "shamsidate", "event_type", "status", "event_index"
    list_filter = "status", "event_type"
    search_fields = "title", "event_type"


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)

