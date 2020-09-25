from django.contrib import admin
from .models import SinglePage


class SinglePageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "page_index")
    pass


admin.site.register(SinglePage, SinglePageAdmin)
