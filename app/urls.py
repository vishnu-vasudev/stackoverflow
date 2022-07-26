from django.urls import path,include
from .views import index, QuestionAPI, latest
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("questions", QuestionAPI)

urlpatterns = [
    path('index', index, name = 'index'),
    path('', include(router.urls)),
    path('latest', latest, name = 'latest'),
    path('user-reg', views.user_reg, name = 'user-reg'),
    path('check', views.check, name = 'check'),
]