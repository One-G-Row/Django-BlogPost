from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404
from .models import Author, Post, Tag

user_profile = {
    
    "text": "Faith is enthusiastic about writing about tech and the world"
}

# Create your views here.
def index(request):
    #fetch all posts, sort them in descending order by date and slice the first three posts
    posts = Post.objects.all().order_by("-date")[:3]

    profiles = user_profile.values()

    return render(request, "blog/index.html", {
        "posts": posts,
        "profiles": profiles
    })

def posts(request):
  #fetch all posts and sort them by date in descending order.
  posts = Post.objects.all().order_by("-date")

  return render(request, "blog/blog_posts.html", {
      "posts":posts,
  })

#post details page
def myposts(request, slug):
    tags = Tag.objects.all()
    try:
        #post = Post.objects.get(slug=slug) or
        post = get_object_or_404(Post, slug=slug)
        return render(request, "blog/my_posts.html", {
            "title": post.title,
            "author": post.author,
            "date": post.date,
            "content": post.content,
            "tags": tags
        })
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)
    