from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import Message


@login_required
def index(request):
    all_messages = Message.objects.all()

    context = {
        'all_messages': all_messages
    }

    return render(request, 'core/index.html', context)
