
from django.urls import path,include
from accounts import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("userModels",views.AccountViewSet)
router.register("userProfile",views.userProfileModel)


urlpatterns = [
    path('', include(router.urls)),

]
