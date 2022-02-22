from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Test, Question, Option
from .serializers import UserSerializer, GroupSerializer, TestSerializer, QuestionSerializer, OptionSerializer

# Create your views here.
from django.http import Http404
from .models import Test 
from .models import Question 
from .models import Option
from curdapp.forms import TestForm

def index(request):
    tests = Test.objects.all()
    return render(request, 'curdapp/index.html', {'Tests': tests})

def createTest(request):
    if request.method == "POST":
        form = TestForm(request.POST)

    if form.is_valid():
        try:
            form.save()
            return redirect('/')
        except:
            pass
    else:
        form=TestForm()
    return render(request, 'curdapp/index.html', {'form':form})


def show(request):
    test = Test.objects.all()
    return render(request, "curdapp/index.html",{'tests':tests})

def edit(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Test.DoesNotExist:
        raise Http404("Test Does Not Exist")
    return render(request, 'curdapp/edit.html',{'test':test})

def update(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Test.DoesNotExist:
        raise Http404("Test Does Not Exist")
    form = TestForm(request.POST, instance = test)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'curdapp/edit.html', {'test':test})

def destroy(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Test.DoesNotExist:
        raise Http404("Test Does Not Exist")
    employee.delete()

    return redirect("/")


class UserViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows users to be viewed or edited.
    # """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows groups to be viewed or edited.
    # """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all() 
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all() 
    serializer_class = QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all() 
    serializer_class = OptionSerializer

