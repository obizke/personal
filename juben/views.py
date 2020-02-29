from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

# Create your views here.

from project.forms import ContactForm, CommentForm
from project.models import Post, Item


# counting the categories in the post
def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def results(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }

    return render(request, 'rama/search_results.html', context)


def index(request):
    items = Item.objects.all().order_by('-created')[:3]
    featured = Post.objects.filter(featured=True).order_by('-created')[:3]
    context = {
        'blog_post': featured,
        'items': items

    }
    return render(request, 'rama/index.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {
        'form': form,
    }

    return render(request, 'rama/contact.html', context)


def details(request, pk):
    recent = Post.objects.filter(featured=True).order_by('-created')[:3]
    category_count = get_category_count()
    blogs = get_object_or_404(Post, id=pk)
    form_class = CommentForm
    form = form_class(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = blogs
            form.save()

    context = {
        'blogs': blogs,
        'form': form,
        'category_count': category_count,
        'recent': recent

    }
    return render(request, 'rama/single-blog.html', context)


def blog(request):
    recent = Post.objects.filter(featured=True).order_by('-created')[:3]
    category_count = get_category_count()
    blog_info = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(blog_info, 1)
    try:
        blog_info = paginator.page(page)
    except PageNotAnInteger:
        blog_info = paginator.page(1)
    except EmptyPage:
        blog_info = paginator.page(paginator.num_pages)
    context = {
        'blog_info': blog_info,
        'recent': recent,
        'category_count': category_count,
    }
    return render(request, 'rama/blog.html', context)


def product(request):
    return render(request, 'rama/category.html')


def product_details(request, pk):
    items = get_object_or_404(Post, id=pk)
    context = {
        'items': items
    }
    return render(request, 'rama/single-product.html', context)
