from django.urls import path
from .views import MainView, PostDetailView, SignUpView,SignInView,SuccessView,FeedbackView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('my_blog_app/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/', FeedbackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
]
