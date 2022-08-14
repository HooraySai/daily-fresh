"""daily_fresh_again URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.static import serve
from daily_fresh_again import settings
from goods.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()), # 项目首页
    path('tinymce/', include(('tinymce.urls', 'tinymce'))), # 富文本编辑器
    path('user/', include(('user.urls', 'user'))),
    path('cart/', include(('cart.urls', 'cart'))),
    path('goods/', include(('goods.urls', 'goods'))),
    path('order/', include(('order.urls', 'order'))),
    # 暴露客户端指定文件
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),

]
