from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=250)
    image_name= models.CharField(max_length=80)
    date = models.DateField(max_length=50)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.excerpt} {self.image_name} {self.date} {self.slug} {self.content} {self.author}"

    def get_absolute_url(self):
        return reverse("myposts", args=[self.slug])

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return f"{self.caption} {self.post}"