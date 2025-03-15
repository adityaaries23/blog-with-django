from django.shortcuts import render, redirect
from django.views import View

from blog.models import Post
from core.utils import custom_404


# Create your views here
class HomePageView(View):
    def get(self, request):
        user = request.user
        posts = Post.objects.all().order_by('-created_at')
        context = {
            'posts': posts,
            'user': user,
        }
        return render(request, 'home.html', context)
class PostView(View):
    def get(self, request, id):
        try:
            posts = Post.objects.get(id=id)
            posts.views += 1
            posts.save()
        except Post.DoesNotExist:
            return custom_404(request)

        return render(request, 'post.html', {'post': posts})

    def post(self, request, id):
        try:
            title = request.POST['title']
            content = request.POST['content']
            post = Post.objects.get(id=id)
            post.title = title
            post.content = content
            post.save()
        except Post.DoesNotExist:
            return custom_404(request)
        return render(request, 'post.html', {'post': post})

class MyPostsView(View):
    def get(self, request):
        posts = Post.objects.filter(actor=request.user).order_by('-created_at')
        context = {
            'posts': posts,
            'user': request.user,
        }
        return render(request, 'home.html', context)

    def post(self, request):
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, actor=user)
        return redirect('myposts')

class NewPostView(View):
    def get(self, request):
        return render(request,'create_post.html')


class UpdatePostView(View):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            return render(request,'create_post.html',{'post':post})
        except Post.DoesNotExist:
            return custom_404(request)

class DeletePostView(View):
    def post(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return redirect('myposts')
        except Post.DoesNotExist:
            return custom_404(request)


