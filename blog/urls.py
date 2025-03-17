from django.urls import path

from blog.views import HomePageView, PostView, MyPostsView, NewPostView, UpdatePostView, DeletePostView, \
    HomePageListView, PostDetailView, MyPostListView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('post/<str:id>', PostDetailView.as_view(), name='post'),
    path('post/<str:id>/update', UpdatePostView.as_view(), name='updatedPost'),
    path('me', MyPostListView.as_view(), name='myposts'),
    path('new', NewPostView.as_view(), name='newpost'),
    path('post/<str:id>/delete', DeletePostView.as_view(), name='deletePost'),
]