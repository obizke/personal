from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from juben.models import Contact
from project.filters import UserFilter
from project.forms import SignUpForm, UserDeleteForm, PostForm, AuthorForm, ItemForm
from project.models import Post, Item


@login_required()
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    context = {
        'filter': user_filter
    }
    return render(request, 'search/user_list.html', context)


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = AuthorForm()

    context = {
        'form': form,
    }
    return render(request, 'admin/author.html', context)


@login_required
def admin(request):
    items = Item.objects.all()
    blogs = Post.objects.all().order_by('-id')[:2]
    count = User.objects.count()
    contacts = Contact.objects.all()
    context = {
        'count': count,
        'contacts': contacts,
        'blogs': blogs,
        'items': items
    }
    return render(request, 'admin/home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('admin')
    else:
        form = SignUpForm()
    context = {
        'form': form

    }
    return render(request, 'registration/signup.html', context)


@login_required
def contact(request):
    contacts = Contact.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(contacts, 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    context = {
        'contact': contacts
    }
    return render(request, 'admin/contact.html', context)


@login_required
def delete_contact(request, pk):
    cont = Contact.objects.get(id=pk)
    if request.method == 'POST':
        cont.delete()
        return redirect('admin')
    else:
        delete_form = UserDeleteForm()
    context = {
        'cont': cont,
        'delete_form': delete_form
    }
    return render(request, 'admin/delete.html', context)


@login_required
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('admin')
    context = {
        'user': user
    }

    return render(request, 'registration/delete_account.html', context)


@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'admin/post.html', context)


@login_required
def update_post(request, pk):
    blog = Post.objects.get(id=pk)
    form = PostForm(instance=blog)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            form = PostForm()

    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'admin/update_post.html', context)


@login_required()
def delete_post(request, pk):
    blog = Post.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('admin')
    context = {
        'blog': blog
    }
    return render(request, 'admin/post_delete.html', context)


# products

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = ItemForm()

    context = {
        'form': form,
    }
    return render(request, 'admin/item.html', context)


@login_required
def update_product(request, pk):
    items = Item.objects.get(id=pk)
    form = PostForm(instance=items)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=items)

        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            form = ItemForm()

    context = {
        'items': items,
        'form': form
    }
    return render(request, 'admin/update_product.html', context)


@login_required()
def delete_product(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin')
    context = {
        'item': item
    }
    return render(request, 'admin/product_delete.html', context)
