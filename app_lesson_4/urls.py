from django.urls import path
from .views import index, top_sellers, advertisements_post

urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name="top-sellers"),
    path('advertisement-post/', advertisements_post, name='adv-post')
]
