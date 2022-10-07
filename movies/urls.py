from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
    # 리스트
    path('list/', views.list, name='list'),
    # 조회
    path('<int:pk>/', views.detail, name='detail'),
    # 생성    
    path('create/', views.create, name='create'),
    # 수정
    path('<int:pk>/update/', views.update, name='update'),
    # 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]