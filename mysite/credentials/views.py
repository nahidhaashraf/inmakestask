from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from credentials.models import Branch, Application
from .models import Branch
# Create your views here.
# def home(request):
#     branches = Branch.objects.all()
#     return render(request,'credentials/home.html',{'branches':branches})
# bankapp/views.py



def branches_view(request):
    branches = Branch.objects.all()
    return render(request, 'index.html', {'branches': branches})


def login_view(request):
    return render(request, 'login.html')


def registration_view(request):
    return render(request, 'register.html')

def new_page_view(request):
    return render(request, 'new_page.html')


def application_form_view(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
        materials = request.POST['material1']

        application = Application(
            name = name,
            dob = dob,
            age = age,
            gender = gender,
            phone = phone,
            address=address,
            district = district,
            branch = branch,
            account_type =account_type,
            materials= materials
        )
        application.save()

        success_message = "Application accepted"
        return render(request, 'application_form.html', {'success_message': success_message})

    return render(request, 'application_form.html')









def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['Password']
        confirmpsw=request.POST['Confirm Password']
        if password==confirmpsw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')