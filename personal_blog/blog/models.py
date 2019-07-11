from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    #if you want to publish the post make it today's date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #have a list of comments and grab approved comments and show them
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def substring(self):
        return self.body[0:100]

    #what to do after creating a page
    #go to the details page of that post
    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey('blog.Blog', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog_list')

    def __str__(self):
        return self.text
