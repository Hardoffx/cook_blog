from django.urls import path
from django.views.decorators.cache import cache_page
3
from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('<slug:slug>/''<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),  # левый slug тип данных, с правой стороны указываем ключ
    # path('', cache_page(60 * 15)(views.HomeView.as_view()), name='home'), # Кешируем полностью всю страницу 'Главная'
    path('', views.HomeView.as_view(), name='home'),  # Отображение 'Главной' без кеширования
]

