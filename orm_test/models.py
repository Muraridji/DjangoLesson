from operator import truediv

from django.db import models
from django.db.models import CASCADE


class Author(models.Model):

    username = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(default="Authors bio")

    def __str__(self):
        return f"Author {self.username}"


class Post(models.Model):
    title = models.CharField(max_length=52, unique=True)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.author})"
'''
    def published_recently(self):
        current_time = models.DateTimeField(auto_now_add=True)
        if self.created_at > current_time:
            return True
'''

class PostLike(models.Model):
    author = models.ForeignKey(Author, related_name="post_like", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_like", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Liked post"
        unique_together = ("author", "post")

    def __str__(self):
        return f"Post {self.post.title} liked by {self.author.username}"


class PostDisLike(models.Model):
    author = models.ForeignKey(Author, related_name="post_dislike", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_dislike", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "DisLiked post"
        unique_together = ("author", "post")

    def __str__(self):
        return f"Post {self.post.title} disliked by {self.author.username}"

class PostComment(models.Model):
    author = models.ForeignKey(Author, related_name="comment", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comment", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"Comment for post {self.post.title} made by {self.author.username}"