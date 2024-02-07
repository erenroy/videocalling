from django.shortcuts import render ,  redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import Opensource
from django.http import HttpResponse
from .models import OpenRoom
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})

    return render(request, 'register.html')


def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login_view")

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')


@login_required
def videocall(request):
    if request.method == 'POST':
        form = Opensource(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('meeting')  # Redirect to a success page or handle as needed
    else:
        form = Opensource()
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name,'form':form})

def create(request):
    if request.method == 'POST':
        title = request.POST['room_name']
        desc = request.POST['objective']
        link = request.POST['link']
        code = request.POST['code']
        topic = request.POST['topic']

        new_create = OpenRoom(title=title,desc=desc,link=link,code=code,topic=topic)
        new_create.save()

        success = 'Room Create Successfully'
        return HttpResponse(success)

def test(request):
    # if request.method == 'POST':
    #     shortforms = Opensource(request.POST , request.FILES)
        
    #     if shortforms.is_valid():
    #         shortforms.instance.user = request.user
    #         shortforms.save()
        
    #     return redirect('home')
    # shortforms = OpenRoom()

    # if request.method == 'POST':
    #     form = Opensource(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('test')  # Redirect to a success page or handle as needed
    # else:
    #     form = Opensource()

    return render(request, 'unique/test.html',{'form':form})


 

#  <h2 id="textid">Enter The title</h2>
#               {{ form.title }}
#               <h2 id="textid">Enter The  Room Details ( Write the description what your room focuses on )</h2>
#               {{ form.desc }}
#               <h2 id="textid">Room Arrangement Topic</h2>
#               {{ form.topic }}
#               <h2 id="textid">Room Code</h2>
#               {{ form.code }}
#               <h2 id="textid">Join Link</h2>
#               {{ form.link }}