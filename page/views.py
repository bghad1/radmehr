from django.shortcuts import render, get_object_or_404
from page.models import SinglePage
# from page.forms import forms


def page_view(request, slug):
    page_detail = get_object_or_404(SinglePage, slug=slug)
    # form = (instance=SinglePage)
    # page_detail = SinglePage.objects.all()
    context = {
        'page_detail': page_detail
    }
    return render(request, 'page-sanje.html', context)
