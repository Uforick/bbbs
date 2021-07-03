from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from bbbs.afisha.views import EventList, EventParticipantList
from bbbs.questions.views import (QuestionList,
                                  QuestionViewPost,
                                  QuestionTagList)

from bbbs.common.views import CityList, MyTokenObtainPairView, ProfileView
from bbbs.main.views import MainView
from bbbs.places.views import PlaceListView, PlacePostUpdateView, PlaceTagList
from bbbs.rights.views import RightList, RightView, RightTagList
from bbbs.articles.viesws import ArticleListView
from bbbs.materials.viesws import MaterialListView
from bbbs.movies.viesws import MovieListView
from bbbs.books.viesws import BookListView
from bbbs.videos.viesws import VideoListView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
   path('admin/', admin.site.urls),

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('api/v1/token/', MyTokenObtainPairView.as_view(), name='my_token_obtain_pair'),
   path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   path('api/v1/questions/', QuestionList.as_view()),
   path('api/v1/question/', QuestionViewPost.as_view()),
   path('api/v1/questions/tags/', QuestionTagList.as_view()),

   path('api/v1/cities/', CityList.as_view()),
   path('api/v1/profile/', ProfileView.as_view()),
   path('api/v1/main/', MainView.as_view()),
   path('api/v1/afisha/events/', EventList.as_view()),
   path('api/v1/afisha/event-participants/', EventParticipantList.as_view()),

   path('api/v1/places/', PlaceListView.as_view()),
   path('api/v1/place/', PlacePostUpdateView.as_view()),
   path('api/v1/places/tags/', PlaceTagList.as_view()),

   path('api/v1/rights/', RightList.as_view()),
   path('api/v1/right/', RightView.as_view()),
   path('api/v1/rights/tags/', RightTagList.as_view()),

   path('api/v1/articles/', ArticleListView.as_view()),

   path('api/v1/books/', BookListView.as_view()),

   path('api/v1/materials/', MaterialListView.as_view()),

   path('api/v1/movies/', MovieListView.as_view()),

   path('api/v1/videos/', VideoListView.as_view()),
]
