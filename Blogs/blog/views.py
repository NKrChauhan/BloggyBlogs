from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Comment,Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DeleteView,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm,CommentForm


@login_required
def logout_view(request):
    logout(request)


@login_required
def approve_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=post.author
            comment.post=post
            comment=form.save()
            return redirect('post_detail',pk=post.pk)
        else:
            form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form,'post':post})

@login_required
def publish_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

def index(request):
    return render(request,'blog/index.html',{})

class PostListView(ListView):
    template_name='blog/post_list.html'
    context_object_name = 'object_list'
    now=timezone.now()
    queryset=Post.objects.filter(publish_date__lte=now).order_by('-publish_date')

class AboutView(TemplateView):
    template_name='blog/about.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    redirect_field_name ='blog/draft_list.html'
    model=Post
    fields=('title','text')

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    fields=['title','text']
    template_name='blog/post_update.html'
    redirect_field_name='blog/post_detail.html'

class PostDetailView(DetailView,LoginRequiredMixin):
    model=Post
    context_object_name ='post'
    def get_object(self):
        return get_object_or_404(Post,pk=self.kwargs.get('pk'))

class DraftView(ListView,LoginRequiredMixin):
    model=Post
    template_name='blog/draft_list.html'
    redirect_field_name='blog/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-create_date')

class DeletePostView(DeleteView):
    model = Post
    success_url=reverse_lazy('post_list')
