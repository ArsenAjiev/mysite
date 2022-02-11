from django.urls import path

from polls.views import vote, IndexView, DetailView, ResultsView

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    #path('', index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/result/
    #path('<int:question_id>/result', result, name='result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='result'),








]

