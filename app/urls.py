from django.urls import path,include
from .views import display, QuestionAPI, latest
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("questions", QuestionAPI)

urlpatterns = [
    path('display', display, name = 'display'),
    path('api', include(router.urls)),
    path('latest', latest, name = 'latest'),
    path('', views.user_login, name = 'user-login'),
    path('search', views.search, name = 'search'),
]