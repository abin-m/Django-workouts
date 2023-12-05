from django.urls import path
from user.views import RegisterUser, LoginUser,TokenRefresh

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
    # ... (other paths)
]