
from django.urls import path,include
from Product import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("productData",views.createProductViewSet)
router.register("productImageData",views.createProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),

]