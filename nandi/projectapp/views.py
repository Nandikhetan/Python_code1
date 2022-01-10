from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, request
import  urllib
from django.views.generic.detail import DetailView
from .models import StudentInfo,StudentAcademics

from .forms import StudentInfo2
from django.views.generic.list import ListView
from django.views.generic import TemplateView


def detail_view(request):
    context={}
    context["dataset"]=StudentInfo.objects.all()
    return render(request, "StudentInfo.html", context)
class Student2(TemplateView):
    template_name = "StudentInfo"

class StudentDetailView(DetailView):
    model= StudentInfo
    model=StudentAcademics


class StudentInfoForm(FormView):
    form_class = StudentInfo2
    template_name = "studentform.html"
    success_url = "/admin/projectapp/studentinfo/"

    def form_valid(self, form):
        form.student()
        return super().form_valid(form)





