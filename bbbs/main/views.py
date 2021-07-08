import random

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


PLACES_OBJ_ON_MAIN_PAGE = 1
ARTICLES_OBJ_ON_MAIN_PAGE = 1
MOVIES_OBJ_ON_MAIN_PAGE = 4
VIDEOS_OBJ_ON_MAIN_PAGE = 1
QUESTIONS_OBJ_ON_MAIN_PAGE = 3
RIGHTS_OBJ_ON_MAIN_PAGE = 1



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
        

        try:
            events_data = events_serializer.data[0]
        except:
            events_data = []
        try:
            places_data = random.sample(places_serializer.data, PLACES_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Place._meta.verbose_name_plural}" заполните поле '
                             f'"{Place.show_on_main_page.field.verbose_name}" и "{Place.chosen.field.verbose_name}" '
                             f'хотя бы у {PLACES_OBJ_ON_MAIN_PAGE} события!')
        try:
            articles_data = random.sample(articles_serializer.data, ARTICLES_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Article._meta.verbose_name_plural}" заполните поле '
                             f'"{Article.show_on_main_page.field.verbose_name}" '
                             f'хотя бы у {ARTICLES_OBJ_ON_MAIN_PAGE} статей!')
        try:
            movies_data = random.sample(movies_serializer.data, MOVIES_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Movie._meta.verbose_name_plural}" заполните поле '
                             f'"{Movie.show_on_main_page.field.verbose_name}" '
                             f'хотя бы у {MOVIES_OBJ_ON_MAIN_PAGE} фильмов!')
        try:
            videos_data = random.sample(videos_serializer.data, VIDEOS_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Video._meta.verbose_name_plural}" заполните поле '
                             f'"{Video.show_on_main_page.field.verbose_name}" '
                             f'хотя бы у {VIDEOS_OBJ_ON_MAIN_PAGE} видео!')
        try:
            questions_data = random.sample(questions_serializer.data, QUESTIONS_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Question._meta.verbose_name_plural}" заполните поле '
                             f'"{Question.show_on_main_page.field.verbose_name}" '
                             f'хотя бы у {QUESTIONS_OBJ_ON_MAIN_PAGE} вопросов!')        
        try:
            rights_data = random.sample(rights_serializer.data, RIGHTS_OBJ_ON_MAIN_PAGE)
        except:
            raise IndexError(f'В разделе "{Right._meta.verbose_name_plural}" заполните поле '
                             f'"{Right.show_on_main_page.field.verbose_name}" '
                             f'хотя бы у {RIGHTS_OBJ_ON_MAIN_PAGE} прав!')  

        return Response({
            'event': events_data,
            'history': HISTORY, #history_data,
            'place': places_data,
            'articles': articles_data,
            'movies': movies_data,
            'video': videos_data,
            'questions': questions_data,
            'rights': rights_data
        })
