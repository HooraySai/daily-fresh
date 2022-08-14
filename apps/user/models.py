from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# class AddressManager(models.Manager):
#     def get_default_addr(self, user):
#         try:
#             address = self.get(user=user, is_default=True)
#         except:
#             address = None
#         return address
#     # 改变原来的查询结果集
#     # 封装方法

class Address(BaseModel):
    # 地址模型
    user = models.ForeignKey('User', verbose_name='所属用户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    addr = models.CharField(max_length=256, verbose_name='收货地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    is_default = models.BooleanField(default=False, verbose_name='是否为默认')
    # 自定义的模型管理类
    # object = AddressManager()

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name
