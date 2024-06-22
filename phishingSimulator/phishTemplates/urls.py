from django.urls import path

from . import views

urlpatterns = [
    path('', views.templateHome, name='templateHome'),
    path('create_template', views.create_tempalte, name="create_template")
]