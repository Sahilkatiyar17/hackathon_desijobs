from django.urls import path
from . import views
from .views import PostListView, PostCreateView,PostDeleteView,PostDetailView

urlpatterns = [
    path('register/',views.Register,name="register"),
    path('login/',views.Login_page,name="login"),
    path('',views.Home,name="home"),
    path('jobs/',PostListView.as_view(),name="jobs"),
    path('create/',PostCreateView.as_view(),name="create"),
    path('logout/',views.logout, name="logout"),
    path('detail/<int:pk>/delete',PostDeleteView.as_view(),name="delete"),
    path('detail/<int:pk>/',PostDetailView.as_view(),name="detail"),
    path('course/',views.course,name="course"),
    path('about/',views.aboutus,name="about"),
]