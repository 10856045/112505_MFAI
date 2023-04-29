from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from first.models import Post
from first.forms import PostForm, PostDeleteConfirmForm


def post_list(request):
    posts = Post.objects.prefetch_related("tags")
    if "tag_id" in request.GET:
        posts = posts.filter(tags__id=request.GET["tag_id"])

    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "文章建立成功")
        messages.info(request, "文章建立成功")
        messages.warning(request, "文章建立成功")
        messages.error(request, "文章建立成功")
        return redirect("post_list")

    return render(request, "post_create.html", {"form": form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = PostForm(request.POST or None, instance=post)
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
    return render(request, "post_comment.html")
