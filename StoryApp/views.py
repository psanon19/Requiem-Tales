from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PlayerCharacterModel, CharacterClassesModel
from .forms import PlayerCharacterForm, UserForm

@login_required
def index(request):
    form_list = PlayerCharacterModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'StoryApp/index.html', context)


def post_new(request):
    if request.method == 'POST':
        form = PlayerCharacterForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.username = request.user
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
    classInfo = (post.CharacterClassesModel_set.all())
    context = {'post': post, 'classInfo': classInfo}
    return render(request, 'StoryApp/detail.html', context)