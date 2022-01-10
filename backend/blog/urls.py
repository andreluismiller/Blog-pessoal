from django.urls import path
from .views import PostBlogListView, PostBlogDetailView, PostBlogFeaturedView, PostBlogCategoryView

urlpatterns = [
    path('', PostBlogListView.as_view()),
    path('<slug>', PostBlogDetailView.as_view()),
    path('featured', PostBlogFeaturedView.as_view()),
    path('category', PostBlogCategoryView.as_view()),
]