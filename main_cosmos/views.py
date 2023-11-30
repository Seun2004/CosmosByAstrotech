from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    allShows = Show.objects.all() # selct * from show, everything from media
    
    context = {
        "medias": allShows,
    }
    
    return render(request, 'main_cosmos/index.html', context)

# detail page
def detail(request, id):
    show = Show.objects.get(id=id) # select everything from movie where id=id 
    ratings = UserRating.objects.filter(show=id)
        
    
    context = {
        "show" : show,
        "ratings": ratings
    }
    
    return render(request, 'main_cosmos/details.html', context)


# add shows to database
def add_show(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = ShowForm(request.POST or None)

                # check if the form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main_cosmos:home")
            else:
                form = ShowForm()
            return render(request, 'main_cosmos/addshows.html', {"form": form, "controller": "Add Show"})
        # if they are not an admin:
        else:
            return render(request, 'main_cosmos/notadmin.html')
    # if they are not logged in:
    return redirect("useraccounts:login")
    
    
 # edit shows
def edit_show(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the shows linked with id
            show = Show.objects.get(id=id)

            #form check
            if request.method == "POST":
                form = ShowForm(request.POST or None, instance=show)
                #check if form is valid
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main_cosmos:detail", id)
            else:
                form = ShowForm(instance=show)
            return render(request, 'main_cosmos/addshows.html', {"form": form, "controller": "Edit Show"})
        else:
            return render(request, 'main_cosmos/notadmin.html')
    # if they are not logged in:
    return redirect("useraccounts:login")



# delete shows
def del_show(request, id=id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            #get the show
            show = Show.objects.get(id=id)

            #delete the show
            show.delete()
            return redirect("main_cosmos:home")
        else:
            return render(request, 'main_cosmos/notadmin.html')
    # if they are not logged in:
    return redirect("useraccounts:login")


def rate_show(request, id):
    if request.user.is_authenticated:
        show = Show.objects.get(id=id)
        if request.method == "POST":
            form = RatingForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.planet = request.POST["planet"]
                data.user = request.user
                data.show = show
                data.save()
                return redirect("main_cosmos:detail", id)
        else:
            form = RatingForm()
        return render(request, "main_cosmos/details.html", {"form": form})
    else:
        return redirect("useraccounts:login")
    
