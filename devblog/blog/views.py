from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    post_list = Post.published.all()
    # paginator init
    paginator = Paginator(post_list, 8)  # pagination with posts per page
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    # error handling for page_number not an int
    except PageNotAnInteger:
        posts = paginator.page(1)
    # error handling for excess page number in URL
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
