from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Message

from .tools import csrf_encrypted, get_csrf_encrypted


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
    context = {
        'csrfencryptedtoken': get_csrf_encrypted(request)
    }

    return render(request, 'core/post_comment.html', context)


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


#@csrf_protect
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


@csrf_encrypted
def save_comment_encrypt(request):
    # on récupere les champs
    user = request.user
    body = request.POST.get('body')

    # on cree un nouvel objet et sauvegarde en base
    new_message = Message(body=body, user=user)
    new_message.save()

    # redirection vers l'accueil
    return redirect('/csrf')
