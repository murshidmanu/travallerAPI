from django.urls import path
from api.v1.places import views


urlpatterns = [
    path('', views.places),
    path('view/<int:pk>', views.place),
    path('protected/<int:pk>', views.protected),
    path('comments/create/<int:pk>/', views.create_comment),
    path('comments/list/<int:pk>/', views.comments_list),
    path('like/<int:pk>/', views.like)
]
 