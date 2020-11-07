from django.shortcuts import render, redirect
from clinicapp.models import Exam
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from clinicapp.forms import ExamForm
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse


# Create your views here.
class ExamList(LoginRequiredMixin, generic.ListView):
    queryset = Exam.objects.filter(result="Negative").order_by('-created_date')
    # paginate_by = 5
    template_name = 'clinicapp/table.html'

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    fields = ('name', 'passport', 'result')
    template_name = 'clinicapp/profile.html'
    def get_success_url(self):
        return reverse('exams',)

class ExamDetail(generic.DetailView):
    model = Exam
    template_name = 'clinicapp/result.html'

# def index(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = ExamForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             passport = form.cleaned_data["passport"]
#             #exam = form.save(commit=False)
#             exam = Exam(name, passport)
#             exam.author = request.user
#             exam.published_date = timezone.now()
#             exam.save()
#             return redirect('exams', pk=exam.pk)
#     else:
#         form = ExamForm()
#     # if request.method == 'POST':
#     #     name = request.POST['name']
#     #     passport = request.POST['passport']
#     return render(request,'clinicapp/profile.html')


def login(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                msg.append('You account has been deactivated!')
    else:
        msg.append('Invalid Login credentials, try again!')
    return render(request, 'login.html', {'errors': msg})


def logout(request):
    logout(request)
