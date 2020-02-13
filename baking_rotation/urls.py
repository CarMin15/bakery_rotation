from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('votes/', views.votes, name='votes'),
    path('yours/', views.yours, name='yours'),
    path('details/<int:item_id>/', views.details, name='details'),

    path('bakedgood/add/', views.BakedGoodCreate.as_view(), name='add-bakedgood'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
