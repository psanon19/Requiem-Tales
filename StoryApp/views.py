from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PlayerCharacterModel, CharacterClassesModel
from .forms import PlayerCharacterForm, UserForm
from random import *

@login_required
def index(request):
    form_list = PlayerCharacterModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'StoryApp/index.html', context)


def post_new(request):
    if request.method == 'POST':
        # the_model = get_object_or_404(CharacterClassesModel)
        # print(the_model.magic)
        form = PlayerCharacterForm(request.POST, )
        if form.is_valid():
            #newModel = PlayerCharacterForm(instance=form)
            #print(newModel)

            newpost = form.save(commit=False)
            newpost.username = request.user
            newpost.strength = str(newpost.classFK.strength)
            newpost.magic = str(newpost.classFK.magic)
            newpost.skill = str(newpost.classFK.skill)
            newpost.speed = str(newpost.classFK.speed)
            newpost.faith = str(newpost.classFK.faith)
            newpost.resistance = str(newpost.classFK.resistance)
            newpost.defence = str(newpost.classFK.defence)
            newpost.constitution = str(newpost.classFK.constitution)
            newpost.movement = str(newpost.classFK.movement)
            newpost.current_gold = str((randint(1,20)+15)*100)


            print(newpost)
            print("Chosen FullName is: " + str((randint(1,20)+15)*100))


            #
            newpost.save()
            return redirect('userindex')
    else:
        form = PlayerCharacterForm()

    return render(request,'StoryApp/new.html', {'form': form})


@login_required
def userindex(request):
    form_list = PlayerCharacterModel.objects.filter(username=request.user)
    # post = get_object_or_404(TransactionModel, pk=pk)
    context = {'form_list': form_list, }
    return render(request, 'StoryApp/index.html', context)


def createUser(request):
    if request.method == 'POST':
        User.objects.create_user(request.POST.get("first_name"), request.POST.get("email"),
                                     request.POST.get("password"), )

        return redirect('userindex')
    else:
        form = UserForm()
        return render(request, 'StoryApp/createUser.html', {'form': form})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(PlayerCharacterModel, pk=pk)
    classInfo = post.classFK
    context = {'post': post, 'classInfo': classInfo}
    return render(request, 'StoryApp/detail.html', context)


def test_post(request):
    # form = PlayerCharacterModel(request.POST,instance=PlayerCharacterModel)
    b = PlayerCharacterModel(full_name="James Macky", current_gold=10,strength=10)
    b.save()
