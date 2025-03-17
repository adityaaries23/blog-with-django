from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from blog.models import Post
from core.utils import custom_404


class HomePageListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    paginate_by = 5
    ordering = ['-created_at']

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super(HomePageListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostView(View):
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


class MyPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']
    template_name = 'home.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(actor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyPostsView(View):
    def post(self, request):
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, actor=user)
        return redirect('myposts')


class NewPostView(View):
    def get(self, request):
        return render(request, 'create_post.html')


class UpdatePostView(View):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            return render(request, 'create_post.html', {'post': post})
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
