"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from first import views

from core.views import my_path, add, minus, multiplied_by, divided_by
from first.views import (
    post_list,
    post_grouplist,
    post_detail,
    post_create,
    post_groupcreate,
    post_update,
    post_delete,
    post_comment,
    post_compare,
    comment_update,
    comment_delete,
    register,
    login,
    logout,
    myword, 
    home,
    result,
    search_view,
)
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("my-path/", my_path),
    path("add/<int:n1>/<int:n2>/", add),
    path("minus/<int:n1>/<int:n2>/", minus),
    path("multiplied_by/<int:n1>/<int:n2>/", multiplied_by),
    path("divided_by/<int:n1>/<int:n2>/", divided_by),
    path("post-list/", post_list, name="post_list"),
    path("post-grouplist/", post_grouplist, name="post_grouplist"),
    path("post-detail/<int:post_id>/", post_detail, name="post_detail"),
    path("post-create/", post_create, name="post_create"),
    path("post-groupcreate/", post_groupcreate, name="post_groupcreate"),
    path("post-update/<int:post_id>/", post_update, name="post_update"),
    path("post-delete/<int:post_id>/", post_delete, name="post_delete"),
    path("post-comment/<int:post_id>/", post_comment, name="post_comment"),
    path("post-compare/", post_compare, name="post_compare"),
    path("comment-update/<int:comment_id>/", comment_update, name="comment_update"),
    path("comment-delete/<int:comment_id>/", comment_delete, name="comment_delete"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("myword/", myword, name="myword"),
    path("result/", result, name="result"),
    path('',home, name="home"),
    path('search/', search_view, name='search'),
    path('login/', LoginView.as_view(template_name='your_login_template.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #path("login_01/<int:comment_id>/", comment_delete, name="comment_delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 