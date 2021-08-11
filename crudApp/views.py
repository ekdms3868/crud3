from django.http import request
from .forms import PostForm,CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment

# Create your views here.

#메인페이지
def main(request):
    return render(request, 'crudApp/main.html')

#글쓰기페이지
def new(request):
    return render(request, 'crudApp/new.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'crudApp/new.html',{'form':form})

#읽기페이지
def read(request):
    posts = Post.objects
    return render(request, 'crudApp/read.html', {'posts' : posts})

#수정페이지
def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'crudApp/edit.html', {'form':form})

#삭제 함수
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')

#댓글 함수
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail',id)
    else:
        form = CommentForm()
        return render(request, 'crudApp/detail.html', {'post':post, 'form':form})