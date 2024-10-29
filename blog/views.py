from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import Http404

my_posts = {
    "The invisible God":"God ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "The importance of tech": "Tech ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "How to train up your child": "Child ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
}

post_images ={
    "The invisible God":"blog/images/Jesus.jpg",
    "The importance of tech": "blog/images/tech.jpg",
    "How to train up your child": "blog/images/child.avif"
}

# Create your views here.
def index(request):
    titles = list(my_posts.keys())
    images =  list(post_images.values())
    texts = list(my_posts.values())

    posts_data = []
    for title, text, image in zip(titles, texts, images):
        if len(text) > 200:
            text = text[:30] + "..."
        posts_data.append({'title': title, 'text': text, 'image': image})
    
    context = {
        "name": "Faith",
        "title": "Faith's Blog",
        "text": "Hi, my name is Faith and i love to blog about tech and the world!",
        "image": "blog/images/Faith.png"
    }
  
    image = context["image"]
    return render(request, 'blog/index.html', {
        "context": context,
        "image": image,
        "posts": posts_data
    })

def posts(request):
    titles = list(my_posts.keys())
    images =  list(post_images.values())
    texts = list(my_posts.values())

    posts_data = []
    for title, text, image in zip(titles, texts, images):
        if len(text) > 200:
            text = text[:80] + "..."
        posts_data.append({'title': title, 'text': text, 'image': image})
        
    return render(request, "blog/blog_posts.html", {
        "posts_data": posts_data
    })

def myposts(request, title):
    try:
        post = my_posts[title]
        return render(request, "blog/my_posts.html", {
            "titles": title,
            "texts": post
        })
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)