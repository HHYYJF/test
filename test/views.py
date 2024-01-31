from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from test.forms import UserRegistrationForm, UserLoginForm
from test.models import PaymentRequest,Requisite


def index(request):
    sor = request.GET.get('a')
    if sor == "2":
        pos = Requisite.objects.all().order_by('-account')
    elif sor == "3":
        pos = Requisite.objects.all().order_by('account')
    elif sor == "4":
        pos = Requisite.objects.all().order_by('owner')
    elif sor == "5":
        pos = Requisite.objects.all().order_by('-owner')
    elif sor == "6":
        pos = Requisite.objects.all().order_by('number')
    elif sor == "7":
        pos = Requisite.objects.all().order_by('limit')
    elif sor == "7":
        pos = Requisite.objects.all().order_by('-limit')
    else:
        pos = Requisite.objects.all()
    return render(request, 'test/index.html', {'pos': pos})

def qq(request):
    po = PaymentRequest.objects.all()
    return render(request,'test/qq.html',{'po':po})

def podrobno(request, pk):
    post = PaymentRequest.objects.filter(pk = pk)
    return render(request,'test/qq.html',{'post':post})

def poisk(request):
    po = request.GET.get('q')
    try:
        pos = Requisite.objects.filter(pay=po) | Requisite.objects.filter(account=po) | Requisite.objects.filter(owner=po) | Requisite.objects.filter(number=po)
        return render(request, 'test/index.html', {'pos': pos})
    except:
        Requisite.objects.filter(limit=po)
        return render(request, 'test/index.html', {'pos': pos})

def login(request, e_handler500=None):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            if e_handler500:
                forms = UserLoginForm()
                return render(request,'test/index.html.html',{'form': form})
        else:
            return HttpResponse('Вы вели не правильно логин или пароль')
    else:
        form = UserLoginForm()
        return render(request, 'test/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        email = request.POST['email']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        user = User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()

        return render(request,'test/index.html')
    else:
        form = UserRegistrationForm()
        return render(request, 'test/registration.html', {'form': form})

def logaut(request):
    logout(request)
    return HttpResponseRedirect('/')
