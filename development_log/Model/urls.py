from django.urls import path
from .views import get_LoginParams_data

urlpatterns = [
    # 其他URL配置...
    path('login/account', get_LoginParams_data, name='get_LoginParams_data'),
]