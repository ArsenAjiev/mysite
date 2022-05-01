from polls.models import Question,Choise
from django.core.management.base import BaseCommand
from django.db.utils import Error
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create questions and choises'

    def handle(self, *args, **kwargs):
        if Question.objects.count() == 0:
            question = Question.objects.create(question_text="Do you like coffee?", pub_date=timezone.now())
            Choise.objects.create(question=question, choise_text="yes")
            Choise.objects.create(question=question, choise_text="no")
            Choise.objects.create(question=question, choise_text="I don't know")
            print('Successfully created ')
        else:
            print('question  exist')




