from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404
from .models import Author, Post, Tag

user_profile = {
    
    "text": "Faith is enthusiastic about writing about tech and the world"
}

# Create your views here.
def index(request):
    posts = Post.objects.all()

    profiles = user_profile.values()

    return render(request, "blog/index.html", {
        "posts": posts,
        "profiles": profiles
    })

def posts(request):
  posts = Post.objects.all()

  return render(request, "blog/blog_posts.html", {
      "posts":posts,
  })


def myposts(request, slug):
   
    try:
        post = get_object_or_404(Post, slug=slug)
        return render(request, "blog/my_posts.html", {
            "title": post.title,
            "content": post.content
        })
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)