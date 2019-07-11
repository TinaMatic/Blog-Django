from django.urls import path
from blog import views

urlpatterns = [
    path('', views.first_page,name='first_page'),
    path('blog/', views.BlogListView.as_view(),name='blog_list'),
    path('blog/<int:pk>', views.BlogDetailsView.as_view(),name = 'blog_details'),
    path('blog/new/', views.BlogCreateView.as_view(), name='blog_new'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('drafts/',views.BlogDraftView.as_view(), name='blog_draft'),
    path('blog/<int:pk>/publish/', views.blog_publish, name='blog_publish'),
]
