from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    is_public = models.BooleanField(default=True)

    tags = models.ManyToManyField(to="Tag", blank=True)

    image = models.ImageField(upload_to="posts/%Y/%m/%d/", null=True, blank=True)

    # null -> 可以存放 null 到資料庫中
    # blank -> 這個欄位是可以不填寫的
    
    # 自動產生的欄位
    # comment_set => 代表了與 Comment 資料表的關聯（<model>_set）


    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=500)

    # FK 刪除的策略
    # models.CASCADE：連帶刪除 -> 刪除 Post 時一併刪除 Comment
    # models.PROTECT：保護 -> 刪除 Post 時，若有 Comemnt 存在阻止 Post 刪除
    # models.SET_DEFAULT：刪除 Post 時，將 Comment 中的 post 欄位設定成預設值
    # models.SET_NULL：刪除 Post 時，將 Comment 中的 post 欄位設定成 null    

    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)


    # 自動產生的欄位
    # post_id => 代表管連到的 Post 的 PK （<fk>_id）

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name