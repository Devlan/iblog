from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField('标题', max_length=60)
    content = models.TextField('正文')
    create_time = models.DateTimeField('创建时间')
    author = models.CharField('作者', max_length=40)
    tag = models.CharField('标签', max_length=30)

    def __str__(self):
        return self.title
