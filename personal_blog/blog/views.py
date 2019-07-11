from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, View, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

from blog.models import Blog, Comment
from blog.forms import BlogForm, CommentForm

# Create your views here.
#view for showing all the blogs
class BlogListView(ListView):
    context_object_name = 'blogs'
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#view for showing only one blog post
class BlogDetailsView(DetailView):
    context_object_name = 'blog_details'
    model = Blog
    template_name = 'blog/blog_details.html'

#view for creating a blog
class BlogCreateView(CreateView):
    # login_url = '/login/'
    # redirect_field_name = 'blog/blog_details.html'
    # form_class = BlogForm
    fields = ('author', 'title', 'image', 'body')
    model = Blog

#view for updating the blog
class BlogUpdateView(UpdateView):
    fields = ('title', 'image', 'body')
    model = Blog

#view for deleting the blog
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')

#view for displaying the blog draft
class BlogDraftView(ListView):
    context_object_name = 'blog_draft'
    model = Blog
    template_name = "blog/blog_draft_list.html"

    def get_queryset(self):
        return Blog.objects.filter(published_date__isnull=True).order_by('created_date')

#First page
def first_page(request):
    return render(request, 'blog/first_page.html')

def blog_publish(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    return redirect('blog_details', pk=pk)
