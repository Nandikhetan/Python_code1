from django.urls import path,include
from . import views
from .views import StudentInfoForm


urlpatterns = [


    path('',StudentInfoForm.as_view()),
    path('', views.detail_view),

]
