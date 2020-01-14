from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._internal import req

from .models import Message


@login_required
def index(request):
    all_messages = Message.objects.all()

    context = {
        'all_messages': all_messages
    }

    return render(request, 'core/index.html', context)


@login_required
def view_comment(request, pk):
    return render(request, 'core/view_comment.html', {'message': Message.objects.get(id=pk)})


@login_required
def post_comment(request):

    return render(request, 'core/post_comment.html', {})


@login_required
def save_comment(request):
    # on récupere les champs
    user = request.user
    body = request.GET.get('body')

    # on cree un nouvel objet et sauvegarde en base
    new_message = Message(body=body, user=user)
    new_message.save()

    # redirection vers l'accueil
    return redirect('/csrf')


@login_required
def save_comment_post(request):
    # on récupere les champs
    user = request.user
    body = request.POST.get('body')

    # on cree un nouvel objet et sauvegarde en base
    new_message = Message(body=body, user=user)
    new_message.save()

    # redirection vers l'accueil
    return redirect('/csrf')


@login_required
def update_password(request):
    user = request.user
    newpassword = request.GET.get('newpassword')
    user.set_password(newpassword)
    user.save()
    return redirect('/csrf')


def presentation(request):
    return render(request, 'core/presentation.html', {})
