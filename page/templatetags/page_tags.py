from django import template
from ..models import SinglePage
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('footer.html')  # takes_context=True)
def show_pages(count=4):
    latest_pages = SinglePage.objects.filter(show_page=True).order_by('page_index')[:count]
    return {'latest_pages': latest_pages}

