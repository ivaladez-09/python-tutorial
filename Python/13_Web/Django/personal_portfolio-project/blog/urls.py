from django.urls import path
from . import views


app_name = 'blog'  # When referencing to some html use app_name:html_name

urlpatterns = [
    # blog/ is implicit added to the URL
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
