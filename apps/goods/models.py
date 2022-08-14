from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField


class GoodsType(BaseModel):
    name = models.CharField(max_length=20, verbose_name='商品名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type')

    class Meta:
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(BaseModel):
    '''商品SPU'''
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    detail = HTMLField(blank=True, verbose_name='商品详情')

    class Meta:
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsSKU(BaseModel):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    type = models.ForeignKey('GoodsType', verbose_name='商品种类', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', verbose_name='商品的SPU', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    display_type = models.BooleanField(default=True, verbose_name='首页展示方式')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    stock = models.IntegerField(default=100, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    status = models.SmallIntegerField(default=1, choices=status_choice, verbose_name='商品状态')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(BaseModel):
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='goods', verbose_name='商品图片')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class gooo(BaseModel):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '测试'
        verbose_name_plural = verbose_name


class IndexGoodsBanner(BaseModel):
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name='轮播商品图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name


class TypeBanner(BaseModel):
    DISPLAY_TYPE_CHOICES = (
        (0, "标题"),
        (1, "图片")
    )
    type = models.ForeignKey('GoodsType', verbose_name='商品类型', on_delete=models.CASCADE)
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品sku', on_delete=models.CASCADE)
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        verbose_name = '主页分类商品'
        verbose_name_plural = verbose_name


class PromotionBanner(BaseModel):
    '''首页促销活动'''
    name = models.CharField(max_length=20, verbose_name='活动名称')
    url = models.CharField(max_length=256, verbose_name='商品连接')
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        verbose_name = '主页促销活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

