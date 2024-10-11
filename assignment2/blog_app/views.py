from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.urls import reverse
from .models import Post
from .forms import CommentForm

# View-level caching for post list page (caches for 60 seconds)
@cache_page(60)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Low-Level Caching for Comment Count
    cache_key = f'post_{post.id}_comment_count'
    comment_count = cache.get(cache_key)
    
    if comment_count is None:
        comment_count = post.comments.count()
        cache.set(cache_key, comment_count, 300)  # Cache timeout set to 5 minutes (300 seconds)

    recent_comments = post.comments.order_by('-created_date')[:5]

    return render(request, 'blog_app/post_detail.html', {
        'post': post,
        'recent_comments': recent_comments,
        'comment_count': comment_count,
    })

def add_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            
            # Invalidate the cached comment count
            cache_key = f'post_{post.id}_comment_count'
            cache.delete(cache_key)
            
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        form = CommentForm()
    return render(request, 'blog_app/add_comment.html', {'form': form, 'post': post})
``
