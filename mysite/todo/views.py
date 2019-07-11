from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.views import View
from django.views.generic.edit import CreateView,DeleteView

#トップ画面表示
class Preview_Todo(View):
    def get(self, req, *args, **kwargs):
        posts = Post.objects.all()
        form = PostForm()
        context = {'posts': posts, 'form':form, }
        return render(req, 'todo/index.html', context)
index = Preview_Todo.as_view()

#ToDo追加機能
class Create_Todo(CreateView):
    def post(self, req, *args, **kwargs):
        form = PostForm(req.POST)
        form.save(commit=True)
        return HttpResponseRedirect(reverse('index'))
add = Create_Todo.as_view()

#ToDo削除機能
class Delete_Todo(DeleteView):
    def delete(self, req, id=None):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return HttpResponseRedirect(reverse('index'))
delete = Delete_Todo.as_view()
