from bbbs.articles.models import Article
from rest_framework.views import APIView
from rest_framework.response import Response

from bbbs.articles.models import Article
from bbbs.movies.models import Movie
from bbbs.questions.models import Question
from bbbs.places.models import Place
from bbbs.rights.models import Right
from bbbs.videos.models import Video

from bbbs.afisha.serializers import EventSerializer
from bbbs.articles.serializers import ArticleSerializer
from bbbs.movies.serializers import MovieSerializer
from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer
from bbbs.rights.serializers import RightSerializer
from bbbs.videos.serializers import VideoSerializer

from bbbs.main.stubs import HISTORY #MOVIES, VIDEO, ARTICLES


class MainView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            city = request.user.profile.city.first()
            events = city.events.all()
        else:
            events = None
        places = Place.objects.filter(chosen=True, show_on_main_page=True)
        articles = Article.objects.filter(show_on_main_page=True)
        movies = Movie.objects.filter(show_on_main_page=True)
        questions = Question.objects.filter(show_on_main_page=True)
        rights = Right.objects.filter(show_on_main_page=True)
        videos = Video.objects.filter(show_on_main_page=True)   
        
        articles_serializer = ArticleSerializer(articles, many=True)
        movies_serializer = MovieSerializer(movies, many=True)
        questions_serializer = QuestionListSerializer(questions, many=True)
        places_serializer = PlaceListSerializer(places, many=True)
        events_serializer = EventSerializer(events, many=True,
                                            context={'request': request})
        rights_serializer = RightSerializer(rights, many=True)
        videos_serializer = VideoSerializer(videos, many=True)
        
        return Response({
            'event': events_serializer.data,
            'history': HISTORY,
            'place': places_serializer.data,
            'articles': articles_serializer.data,
            'movies': movies_serializer.data,
            'video': videos_serializer.data,
            'questions': questions_serializer.data,
            'rights': rights_serializer.data,
        })
