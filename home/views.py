from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from django.http import HttpResponse
from blog .models import Post
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    allpost = Post.objects.all()
    context = {
        'allpost': allpost
    }
    return render(request, 'home/home.html', context)


def about(request):
    messages.info(request, 'Welcome to About.')
    return render(request, 'home/about.html')


def contact(request):
    messages.info(request, 'Welcome to Contact.')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        textarea = request.POST['textarea']
        if len(name) < 2 or len(email) < 3 or len(phone) < 4 or len(textarea) < 3:
            messages.warning(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, textarea=textarea)
            contact.save()
            messages.success(request, "Your massege has been send !")

    return render(request, 'home/contact.html')


def search(request):
    searchin = request.GET['searchcont']

    if len(searchin) > 50:
        allpost = Post.objects.none()
    else:
        allposttitle = Post.objects.filter(title__contains=searchin)
        allpostcontent = Post.objects.filter(content__contains=searchin)
        allpost = allposttitle.union(allpostcontent)
    if len(allpost) == 0:
        messages.info(request, "Please fill the form correctly !")
    letsgo = {
        'allpost': allpost,
        'searchin': searchin,
    }
    return render(request, 'home/search.html', letsgo)


def singup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(username) > 60:
            messages.warning(request, "Username is so big !")
            return redirect('home')
        if password1 != password2:
            messages.warning(request, "Password is not match !")
            return redirect('home')
        if not username.isalnum():
            messages.warning(request, "Username must be text and creaccter !")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been Created !")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')


def loginl(request):

    if request.method == "POST":
        username11 = request.POST['username']
        password22 = request.POST['password']

        user = authenticate(username=username11, password=password22)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Loged in !')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Input')
            return redirect('home')

    return HttpResponse('Log In')


def logoutl(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')
