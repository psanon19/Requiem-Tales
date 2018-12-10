from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PlayerCharacterModel
from .forms import PlayerCharacterForm, UserForm

@login_required
def index(request):
    form_list = PlayerCharacterModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'StoryApp/index.html', context)


@login_required
def userindex(request):
    form_list = PlayerCharacterModel.objects.filter(username=request.user)
    # post = get_object_or_404(TransactionModel, pk=pk)
    context = {'form_list': form_list, }
    return render(request, 'StoryApp/index.html', context)


def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("first_name"), request.POST.get("email"),
                                     request.POST.get("password"), )
            form.save()
            return redirect('userindex')
    else:
        form = UserForm()
        return render(request, 'StoryApp/createUser.html', {'form': form})
