from django.shortcuts import render


def homepage(request):
    # return render(request, 'index.html', {})
    # return render(request, 'index-sanje.html', {})
    return render(request, 'brand-sanje-original.html', {})
