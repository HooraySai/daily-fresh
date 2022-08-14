from django.urls import path, re_path
from user import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    re_path('active/(?P<token>.*)/', views.ActiveView.as_view(), name='active'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', login_required(views.LogoutView.as_view()), name='logout'),
    path('', views.UserInfoView.as_view(), name='user'),
    re_path('order/(?P<page>\d+)/', login_required(views.UserOrderView.as_view()), name='order'),
    path('address/', login_required(views.AddressView.as_view()), name='address'),
]
