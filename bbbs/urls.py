from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from bbbs.afisha.views import EventList, EventParticipantList
from bbbs.common.views import CityList, ProfileView
from bbbs.main.views import MainView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=settings.SNIP_EMAIL),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

app_urls = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('cities/', CityList.as_view(), name='city_list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('main/', MainView.as_view(), name='main_view'),
    path('afisha/events/', EventList.as_view(), name='event_list'),
    path('afisha/event-participants/', EventParticipantList.as_view(), name='event_participant'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/', include(app_urls)),
]

