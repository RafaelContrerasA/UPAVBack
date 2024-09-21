from django.urls import path
from users.api.views import RegisterView, UserView, ChangePasswordView, CustomTokenObtainPairView, UserDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import UserListView
urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', UserView.as_view()),
    path('auth/pass/', ChangePasswordView.as_view(), name='change_password'),
    path('auth/users/', UserListView.as_view(), name='user_list' ),
    path('auth/users/<int:user_id>/', UserDeleteView.as_view(), name='user_delete'),
]
