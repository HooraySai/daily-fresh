
from django.urls import path, include, re_path
from order.views import *


urlpatterns = [
    path('place/', OrderPlaceView.as_view(), name='place'),
    path('commit/', OrderCommitView.as_view(), name='commit'),
    path('pay/', OrderPayView.as_view(), name='pay'),
    path('check/', CheckPayView.as_view(), name='check'),
    re_path('comment/(?P<order_id>.+)', CommentView.as_view(), name='comment'),
]
