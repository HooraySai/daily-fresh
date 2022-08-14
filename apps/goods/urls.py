from django.urls import path, re_path
from goods import views

# from goods import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('goods/(?P<goods_id>\d+)', views.DetailView.as_view(), name='detail'),
    re_path('list/(?P<type_id>\d+)/(?P<page>\d+)', views.ListView.as_view(), name='list'),
]