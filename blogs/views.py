from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import PostForm
# Access restriction.
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Show a certain number of posts.
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    """Blogs app home page."""
    posts = BlogPost.objects.order_by('-date_added')[:4]
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def check_post_owner(request, post):
    """Protecting user topics - ONLY for edit/delete"""
    if post.owner != request.user:
        raise Http404

@login_required
def view_post(request, post_id):
    """View a single post"""
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)    

@login_required
def create_post(request):
    """Сreating a new post."""
    if request.method != 'POST':
        # An empty form is created.
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            # Linking new topics to the current user.    
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:post', post_id=new_post.id)

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Editing an existing post."""
    post = get_object_or_404(BlogPost, id=post_id)
    check_post_owner(request, post)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
           form.save()
           return redirect('blogs:index')

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    """Delete a post, for owner"""
    post = get_object_or_404(BlogPost,id=post_id, owner=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('blogs:index')

    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)

@login_required
def all_posts(request):
    """Show all posts"""
    posts = BlogPost.objects.order_by('-date_added')

    # Show certain numbers of posts.
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)
