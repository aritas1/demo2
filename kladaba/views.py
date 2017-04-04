from django.shortcuts import render
from django.views import generic
from kladaba.models import Exam

# Create your views here.

def exam_detail(request, id):
    context = {
        'exam' : Exam.objects.get(pk=id)
    }
    return render(request, 'kladaba/exam_detail.html', context)


class ExamListView(generic.ListView):
    model = Exam