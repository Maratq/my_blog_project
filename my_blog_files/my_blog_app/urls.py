from django.urls import path
from .views import MainView, PostDetailView, SignUpView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    ]
