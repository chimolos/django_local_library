from django.shortcuts import render, redirect
from . models import Todo,Category,Profile, Appraisal,Plan
from . forms import CategoryForm, TodoForm, RegisterForm, ProfileForm, UserProfileForm, AppraisalForm, PlanForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def index(request):
    # catform = CategoryForm(instance=request.user)
    myform = TodoForm()
    alltodos = Todo.objects.all()
    cat = Category.objects.filter(user_id=request.user.id).first()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        catform = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        if catform.is_valid():
            catform.instance.user = request.user
            catform.save()
            return redirect('index')

    else:
        form = TodoForm()
        # catform = CategoryForm()

    context = {
        'todos':alltodos,
        'form':myform,
        # 'cform': catform
    }
    return render(request, 'index.html', context)

def completeit(request,todo_id):
    todo = Todo.objects.filter(pk=todo_id).first()
    if todo.completed_status:
        todo.completed_status = False
    else:
        todo.completed_status = True

    todo.save()
    return redirect('index')

def del_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')

def appraisal(request):
    #theapprform = AppraisalForm(instance=request.user)
    if request.method == 'POST':
        theapprform = AppraisalForm(request.POST)
        theapprform.save()
        return redirect('index')

    context = {
        'apprform':theapprform,
    }
    return render(request, 'appraisal.html', context)

def plan(request):
    #theplanform = PlanForm(instance=request.user)
    if request.method == 'POST':
        theplanform = PlanForm(request.POST)
        theplanform.save()
        return redirect('index')

    context = {
        'planform':theplanform
    }
    return render(request, 'plans.html',context)

@login_required(login_url='longinpage')
def userprofile(request):
    profile = Profile.objects.filter(user_id=request.user.id).first()
    plan = Plan.objects.all()
    #print(profile)
    theform = ProfileForm(instance=profile)
    theuserform = UserProfileForm(instance=request.user)
    if request.method == 'POST':
        theform = ProfileForm(request.POST,instance=profile)
        theuserform = UserProfileForm(request.POST,instance=request.user)
        theform.save()
        theuserform.save()
        return redirect('index')
    context = {
        'myplan': plan,
        'form':theform,
        'userform':theuserform
    }
    return render(request,'profilepage.html', context)


#Security
def longinpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid username/password')
    context = {}
    return render(request, 'loginpage.html', context)

def logoutpage(request):
    return render(request, 'logout.html')

def signout(request):
    logout(request)
    return redirect('loginpage')

def registerpage(request):
    #form = UserCreationForm()
    newform = RegisterForm()
    if request.method == 'POST':
        newform = RegisterForm(request.POST)
        if newform.is_valid():
            myuser = newform.save()
            # p = Profile(user=myuser)
            # p.save()
            Profile.objects.create(user=myuser)
            login(request,myuser)
            return redirect('index')
    context = {
        'form':newform,
    }
    return render(request,'registerpage.html', context)
