from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')), 
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('user/<int:user_id>/', views.UserFindView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)