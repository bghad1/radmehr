from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def seminar_detail(request, slug):
    # criterion1 = Q(status='published')
    # criterion2 = Q(event_type="seminar")
    # seminars_published = Event.objects.get(slug & criterion1 & criterion2)
    # seminars = Event.objects.filter(slug=seminars_published)
    # seminars = Event.objects.get(slug=slug)
    seminars = get_object_or_404(Event, slug=slug)
    context = {
        'seminars': seminars
    }
    return render(request, "seminar_detail.html", context)


def exhibition_detail(request, slug):
    # criterion1 = Q(status='published')
    # criterion2 = Q(event_type="exhibition")
    # exhibition_published = Event.objects.get(slug & criterion1 & criterion2)
    # exhibitions = Event.objects.filter(slug=exhibition_published)
    # cr1 = Q(events='2')
    # cr2 = Q(slug=slug)
    # exhibitions = Event.objects.get(cr1 & cr2)
    exhibitions = get_object_or_404(Event, slug=slug)
    # exhibitions = Event.objects.get(slug=slug)
    context = {
        'exhibitions': exhibitions
    }
    return render(request, "exhibition_detail.html", context)


# def seminar_view(request):
#     criterion1 = Q(status='published')
#     criterion2 = Q(event_type="seminar")
#     seminars = Event.objects.filter(criterion1 & criterion2).order_by('event_index')
#     paginator = Paginator(seminars, 5)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'seminars': seminars
#     }
#     return render(request, "seminar_view.html", context)

def seminar_view(request):
    criterion1 = Q(status='published')
    criterion2 = Q(event_type="seminar")
    # seminars1 = Event.objects.get(criterion1 & criterion2)
    seminars = Event.objects.filter(criterion1 & criterion2).order_by('event_index')
    paginator = Paginator(seminars, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'seminars': seminars
    }
    print(seminars)
    return render(request, "seminar_view.html", context)


# def exhibition_view(request):
#     # criterion3 = Q(status='published')
#     # criterion4 = Q(event_type="exhibition")
#     # exhibitions_view = Event.objects.filter(criterion3 & criterion4).order_by('event_index')
#     exhibitions_view = Event.objects.filter(event_type="exhibition").order_by('event_index')
#     paginator = Paginator(exhibitions_view, 5)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'exhibitions_view': exhibitions_view
#     }
#     return render(request, "exhibition_view.html", context)

def exhibition_view(request):
    criterion3 = Q(status='published')
    criterion4 = Q(event_type="exhibition")
    # exhibitions_view = Event.objects.filter(criterion3 & criterion4).order_by('event_index')
    # exhibitions_view = Event.objects.filter(event_type="exhibition").order_by('event_index')
    # exhibitions_view = Event.objects.filter(event_type=criterion3)
    exhibitions_view = Event.objects.filter(criterion3 & criterion4)
    # paginator = Paginator(exhibitions_view, 5)
    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer deliver the first page
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range deliver last page of results
    #     posts = paginator.page(paginator.num_pages)
    context = {
        'exhibitions_view': exhibitions_view
    }
    print(exhibitions_view)
    return render(request, "event_view.html", context)

# def seminar_detail(request, slug):
    # seminars_published = Event.objects.filter(status='published')
    # seminars = Event.objects.filter(slug=seminars_published)
    # context = {
    #     'seminars': seminars
    # }
    # return render(request, "seminar_detail.html", context)

# def exhibition_detail(request, slug):
#     exhibition_published = Event.objects.filter(status='published')
#     exhibitions = Event.objects.filter(slug=exhibition_published)
#     context = {
#         'exhibitions': exhibitions
#     }
#     return render(request, "exhibition_detail.html", context)
