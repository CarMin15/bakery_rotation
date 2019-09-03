from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('votes/', views.votes, name='votes'),
    path('yours/', views.yours, name='yours'),
    path('create/', views.create, name='create'),
    # path('details/<int:item_id>/', views.details, name='details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
