from django.db import models


# Create your models here.
class UserInfo(object):
    user_name = models.CharField('用户名', max_length=20),
    user_passwd = models.CharField('密码', max_length=40),
    user_email = models.CharField('邮箱', max_length=30),
    user_profile_photo = models.ImageField(upload_to='user_profile_photo/'),

    def __str__(self):
        return self.user_name
