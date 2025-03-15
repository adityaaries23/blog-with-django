from django.urls import path

from blog.views import HomePageView, PostView, MyPostsView, NewPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<str:id>', PostView.as_view(), name='post'),
    path('post/<str:id>/update', UpdatePostView.as_view(), name='updatedPost'),
    path('me', MyPostsView.as_view(), name='myposts'),
    path('new', NewPostView.as_view(), name='newpost'),
    path('post/<str:id>/delete', DeletePostView.as_view(), name='deletePost'),
]