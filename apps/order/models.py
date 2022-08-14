from django.db import models
from db.base_model import BaseModel
from goods.models import *


# Create your models here.


class OrderInfo(BaseModel):
    pay_method_choice = (
        (0, '货到付款'),
        (1, '微信支付'),
        (2, '支付宝支付'),
        (3, '银联支付'),
    )
    ORDER_STATUS = {
        0: '待支付',
        1: '待发货',
        2: '待收货',
        3: '待评价',
        4: '已完成'
    }
    order_status_choice = (
        (0, '待支付'),
        (1, '待发货'),
        (2, '待收货'),
        (3, '待评价'),
        (4, '已完成'),
    )
    order_id = models.CharField(max_length=128, verbose_name='订单id', default='')
    user = models.ForeignKey('user.User', verbose_name='用户', on_delete=models.CASCADE)
    addr = models.ForeignKey('user.Address', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=pay_method_choice, default=3,)
    order_status = models.SmallIntegerField(choices=order_status_choice, default=1)
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tran_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    trade_num = models.CharField(max_length=128, verbose_name='支付编号', default='')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    '''订单商品模型类'''
    order = models.ForeignKey('OrderInfo', verbose_name='订单', on_delete=models.CASCADE)
    sku = models.ForeignKey('goods.GoodsSKU', verbose_name='商品的SKU', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, )
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    comment = models.CharField(max_length=256, )

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

