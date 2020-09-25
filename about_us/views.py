from django.shortcuts import render
from about_us.models import AboutUs


def home_about_us(request):
    about_detail = AboutUs.objects.all()
    context = {
        'about_detail': about_detail
    }
    return render(request, 'about-sanje.html', context)
