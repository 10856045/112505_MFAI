from first.models import Post, Comment, Tag


# 建立 Post 方法一

post = Post()
post.title = 'Title01'
post.content = 'Content01'
post.save()

# 建立 Post 方法一之一

post = Post(title='Title02', content='Content01')
post.save()

# 建立 Post 方法

Post.objects.create(title='Title003', content='Content003')

# 查詢 Post

Post.objects.get(id=9)
Post.objects.get(title='Title003')
Post.objects.get(id=9, title='Title003')
Post.objects.get(id=10, title='Title003')
Post.objects.get(title='1111')

# 查詢過濾 Post
# 會傳傳多筆資料，如果需要第一筆可以用 [0] 或是 .first() 取得

Post.objects.filter(id=9)  
Post.objects.filter(title='Title003')
Post.objects.filter(id=9, title='Title003')
Post.objects.filter(id=10, title='Title003')
Post.objects.filter(title='1111')

Post.objects.filter(title='1111').first()
Post.objects.filter(title='1111').last()
Post.objects.filter(title='1111')[0]
Post.objects.filter(title='1111')[0:2]

# 全部的 Post

Post.objects.all()
Post.objects.order_by('title')
Post.objects.order_by('-title')
Post.objects.order_by('?')

Post.objects.filter(title='1111').order_by('id')

# 修改 Post

post = Post.objects.get(id=9)
print(post.title)
post.title = 'Title003 - 修改過'
post.save()

posts = Post.objects.filter(title='1111')
posts.update(title='2222')

# 刪除 Post

post = Post.objects.get(id=9)
post.delete()

posts = Post.objects.filter(title='2222')
posts.delete()

# 關聯操作

post = Post.objects.create(title='Title 001', content='Content 001')
comment = Comment.objects.create(content='Comment 001', post=post)

post.comment_set.all()  # 取得此篇 post 的所有留言
comment.post  # 取得留言所屬的文章物件
comment.post_id  # 取得留言 FK 的值

tag1 = Tag.objects.create(name='T01')
tag2 = Tag.objects.create(name='T02')
tag3 = Tag.objects.create(name='T03')

post.tags.add(tag1, tag2)  # 將 tag1 與 tag2 和 post 建立關係

post.tags.all()  # 取得此 post 的所有標籤
tag1.post_set.all()  # 取得此標籤的所有文章

post.tags.remove(tag1)  # 將 tag1 從與此文章的關係刪除
post.tags.clear()  # 清除此文章的所有標籤

post.tags.set([tag2, tag3])  # 將此文章的標籤關係覆蓋成 tag2 與 tag3，結果與先 clear 再 add 相同


# 獲取關聯資料

for post in Post.objects.prefetch_related('tags'):  # 從一往多關係，預先獲取關聯資料
    print(post.title)
    for tag in post.tags.all():
        print(tag.name)

    print('=====')


for comment in Comment.objects.select_related('post'):  # 從多往一，預先獲取關聯資料
    print(comment.post.title)
    print(comment.content)
    print('=====')