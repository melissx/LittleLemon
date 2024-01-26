from django.urls import path, include
from . import views
from .views import MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index')
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls)),
]


