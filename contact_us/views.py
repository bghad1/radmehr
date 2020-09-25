from django.shortcuts import render


def home_contact_us(request):
    return render(request, 'contact.html', {})
