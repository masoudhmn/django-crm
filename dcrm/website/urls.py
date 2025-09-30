from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'), # type: ignore
    path('logout/', views.logout_user, name='logout'), # type: ignore
    path('register/', views.register_user, name='register'), # type: ignore
    path('record/<int:pk>', views.customer_record, name='record'), # type: ignore
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'), # type: ignore
    path('update_record/<int:pk>', views.update_record, name='update_record'), # type: ignore
    path('add_record/', views.add_record, name='add_record'),
]
