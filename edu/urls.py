from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('tag', views.TagStudy.as_view(), name='tag_study'),
    path('new', views.NewContent.as_view(), name="new_content"),
]