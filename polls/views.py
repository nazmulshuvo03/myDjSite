from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics

from .models import Question, Choice
from .serializer import QuestionSerializer, QuestionChoiceSerializer


class IndexViewSet(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailViewSet(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'pk'


class ResultsViewSet(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionChoiceSerializer
    lookup_field = 'pk'


def vote(request, pk, choice):
    question = get_object_or_404(Question, pk=pk)
    selected_choice = question.choice_set.get(pk=choice)
    selected_choice.votes += 1
    selected_choice.save()

    response = f'Voted successfully to "{selected_choice.choice_text}" for "{question.question_text}"'

    return HttpResponse(response)
