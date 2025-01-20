from django.shortcuts import render, get_object_or_404
from .models import Post, Author

# Create your views here.
def main_page(request):
    return render(request, "blog/main_page.html")

def authors(request):
    return render(request, "blog/authors_posts.html")

def post_view(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/posts_page.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})
