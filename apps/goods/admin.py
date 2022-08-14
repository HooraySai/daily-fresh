from django.contrib import admin
from goods.models import *

# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # 更新表中数据调用
        super().save_model(request, obj, form, change)
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()
        print('产生tasks完毕')

    def delete_model(self, request, obj):
        # 删除表中数据调用
        super().delete_model(request, obj)
        from celery_task.tasks import generate_static_index_html
        generate_static_index_html.delay()


class GoodsSKUAdmin(BaseModelAdmin):
    pass


class GoodsAdmin(BaseModelAdmin):
    pass


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class GoodsImageAdmin(BaseModelAdmin):
    pass


class PromotionBannerAdmin(BaseModelAdmin):
    pass


class TypeBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsImage, GoodsImageAdmin)
admin.site.register(PromotionBanner, PromotionBannerAdmin)
admin.site.register(TypeBanner, TypeBannerAdmin)
