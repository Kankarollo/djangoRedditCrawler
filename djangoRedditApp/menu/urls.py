from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='menu-home'),
    path('search-reddit/', views.search_reddit_page, name='menu-search-reddit')
]

urlpatterns += staticfiles_urlpatterns()
