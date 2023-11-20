from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from first.models import Post, Comment, group
from first.forms import (
    PostForm,
    PostDeleteConfirmForm,
    CommentForm,
    commentDeleteConfirmForm,
    GroupfForm
)

from django.shortcuts import render
import subprocess, os

def post_list(request):
    posts = Post.objects.prefetch_related("tags")
    if "tag_id" in request.GET:
        posts = posts.filter(tags__id=request.GET["tag_id"])

    return render(request, "post_list.html", {"posts": posts})

def post_grouplist(request):
    groups = group.objects.all()
    # groups = group.objects.prefetch_related("tags")
    # if "tag_id" in request.GET:
    #     posts = posts.filter(tags__id=request.GET["tag_id"])
    return render(request, "post_grouplist.html", {"groups": groups})


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "題目上傳成功")
        return redirect("post_list")

    return render(request, "post_create.html", {"form": form})

def post_groupcreate(request):
    form = GroupfForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "群組建立成功")
        return redirect("post_grouplist")

    return render(request, "post_groupcreate.html", {"form": form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "文章編輯成功")
        return redirect("post_detail", post_id)

    return render(request, "post_update.html", {"form": form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = PostDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, "文章刪除成功")
        return redirect("post_list")

    return render(request, "post_delete.html", {"form": form})

def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        messages.success(request, "留言成功")
        return redirect("post_detail", post_id)

    return render(request, "post_comment.html", {"form": form})

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        comment = form.save()
        messages.success(request, "留言編輯成功")
        return redirect("post_detail", comment.post_id)

    return render(request, "comment_update.html", {"form": form})


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    form = commentDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        comment.delete()
        messages.success(request, "留言刪除成功")
        return redirect("post_detail", comment.post_id)

    return render(request, "comment_delete.html", {"form": form})

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, "register.html", {"form": form})


# def login(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
    
#     context = {
#         'form': form
#     }
#     return render(request, "login.html", {"form": form})

def login(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserCreationForm(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = UserCreationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = UserCreationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    register(request)
    return redirect('/')

def myword(request):

    return render(request, 'myword.html')

def result(request):

    return render(request, 'result.html')

def home(request):

    return render(request, 'home.html')


def post_compare(request):
    if request.method == 'POST':
        folder_path = request.POST.get('folder_path', '')
        output_filename = request.POST.get('output_filename', '')
        if folder_path and output_filename:
            try:
                command = f'dolos run -l python /{folder_path}/*.py > {output_filename}.text'
                subprocess.run(command, shell=True, check=True)
                messages.success(request, "比對成功")
                
                # 讀取文件
                similarity_values = []
                file_paths = []

                with open(f'{output_filename}.text', 'r') as file:
                    next(file) 
                    for line in file:
                        fields = line.split()
                        if len(fields) == 5:  
                            similarity = float(fields[2])
                            file_path = fields[1]
                            similarity_values.append(similarity)
                            file_paths.append(file_path)
                
                # Similarity轉換成百分比
                similarity_percentages = [round(value * 100, 1) for value in similarity_values]

                # 刪除讀取完成的檔案
                os.remove(f'{output_filename}.text')

                return render(request, 'result.html', {'percentages': similarity_percentages, 'file_paths': file_paths})
            except subprocess.CalledProcessError as e:
                messages.error(request, "比對失敗")
    return render(request, 'post_compare.html')

