from django.urls import path
from rest_framework.routers import SimpleRouter
from api.v1.home_page import views

router = SimpleRouter()

router.register('api/v1/header_navigations', views.HeaderNavigationViewSet)
router.register('api/v1/adventages', views.AdventageViewSet)

urlpatterns = [
    path('', views.homePage, name="home")
]

urlpatterns += router.urls
