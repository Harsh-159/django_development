from django.shortcuts import render
from  base_app.forms import UserForm,UserProfileInfo

from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'base_app_template/index.html',)

@login_required
def special(request):
    return HttpResponse("Cool you are logged in")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered=False
    if request.method =="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'user_pic' in request.FILES:
                profile.user_pic=request.FILES['user_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfo()
    return render(request,'base_app_template/registration.html',
                                                                {'user_form':user_form,
                                                                'profile_form':profile_form,
                                                                'registered':registered},)

def user_login(request):
    if request.method=="POST":
        print("Hola")
        usern=request.POST.get('name')
        passw=request.POST.get('pass')

        user=authenticate(username=usern,password=passw)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed.")
            print("Username:{} Password:{}".format(usern,passw))
            return HttpResponse("Invalid Details Provided")
    else:
        return render(request,'base_app_template/login.html')
