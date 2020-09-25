from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


def blog_view(request):
    object_list = Post.objects.all().order_by('-created_on')
    paginator = Paginator(object_list, 5)
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
        'posts': posts
    }
    return render(request, 'blog.html', context)
    # return render(request, 'blog_view.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    # post = Post.objects.get(title=title)

    form = CommentForm()
    if request.method == 'Post':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        'form': form,
    }
    return render(request, "single_post.html", context)
    # return render(request, "blog_detail.html", context)


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'
