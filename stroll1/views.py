from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm,ratingForm

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users

from django.contrib.auth.models import Group

from django.db.models import Avg

from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

# from rest_framework.viewsets import ModelViewSet

# from .serializers import ProductSerializer, RatingSerializer

# from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @login_required(login_url='login')

# @allowed_users(allowed_roles=['admin'])
def index(request):
   
    dests = Destination.objects.all()
    context = {'dests': dests}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def payment(request):
    return render(request, 'payment.html')
   
    # dests = Destination.objects.all()
    # context = {'dests': dests}

def search(request):
    # blogdatas = Blogs.objects.all()
    query = request.GET['query']
    if len(query) > 80:
        blogdatas= Blogs.objects.none()
    else:
        # blogdatasname = Blogs.objects.filter(name__icontains=query)
        # blogdatastag = Blogs.objects.filter(tag__icontains=query)
        blogdatasdesc = Blogs.objects.filter(description__icontains=query)

        # blogdatas = blogdatasname.union(blogdatastag)
        # blogdatas1 = blogdatas.union(blogdatasdesc)
        paginator = Paginator(blogdatasdesc, 1)
        page_number = request.GET.get('page')
        try:
             blogdatasdesc = paginator.page(page_number)
        except PageNotAnInteger:
             blogdatasdesc =paginator.page(1)
        except EmptyPage:
             blogdatasdesc = paginator.page(paginator.num_pages)
             
             
             
        # final = paginator.get_page(page_number)

    # if blogdatas.count(datas) == 0:
    #     messages.warning(request, "No Search results found. Please refine your keyword.")
    context = {'blogdatas': blogdatasdesc, 'query': query, 'page': page_number}
    return render(request, 'search.html', context)

def custom(request):
    data = json.loads(request.body)
    # print(data)
    # name = form['name']

    Custom.objects.create(
        name = data['form']['name'],
        destnation = data['form']['destination'],
        activity = data['form']['activity'],
        duration = data['form']['duration'],
        date = data['form']['date'],
    )
    print(data['form']['name'])


    return JsonResponse('Payment Complete', safe=False)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.info(request, "Username or Password incorrect")
                return render(request, 'login.html')

        context = {}
        return render(request, 'login.html', context)

@unauthenticated_user
def register(request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user =form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name = 'customer')

                user.groups.add(group)

                Customer.objects.create(
                     user = user,
                     name= user.username,
                )

                messages.success(request, 'Account was created for ' + username )
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
     
     context = {}
     return render(request, 'userpage.html', context)


def ratingPage(request, dest_id):
    #  user = request.user
     destination = Destination.objects.get(id=dest_id)
     reviews = Rating.objects.filter(destination=destination)
     avg_reviews = reviews.aggregate(Avg('rating'))
     reviews_count = reviews.count()
     user = request.user
     form = ratingForm()

     if request.method == 'POST':
          form = ratingForm(request.POST)
          
          if form.is_valid:
               rate = form.save(commit=False)
               rate.user = user
               rate.destination = destination
               rate.save()
               return redirect('home')

     context = {'form': form, 'destination': destination, 'avg_reviews' : avg_reviews,'reviews_count' : reviews_count}
     return render(request, 'rating.html', context)
# from rest framework


def destination_details(request, dest_id):
     
    if Destination.objects.filter(id=dest_id).exists():
        destination = Destination.objects.get(id=dest_id)
        reviews = Rating.objects.filter(destination=destination)
        avg_reviews = reviews.aggregate(Avg('rating'))
        reviews_count = reviews.count()

    context = {'destination': destination, 'reviews_count': reviews_count, 'avg_reviews': avg_reviews, 'reviews':reviews}
    return render(request, 'destination_details.html', context)


def maps(request):
     return render(request, 'maps.html')

def mapsktm(request):
     return render(request, 'mapsktm.html')
def mapsbkt(request):
     return render(request, 'mapsbkt.html')
def mapslpr(request):
     return render(request, 'mapslpr.html')

def mapsboudha(request):
     return render(request, 'mapsboudha.html')
     



