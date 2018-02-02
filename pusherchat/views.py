from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
import names
from oracle import views
pusher = Pusher(
    app_id='441799',
    key='694ffbf91035a4c545c8',
    secret='ac844e257ca1c9f6fcbd',
    cluster='us2',
    ssl=True
)

# Create your views here.
#@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"chat.html");


@csrf_exempt
def broadcast(request):
    if 'UserID' in request.COOKIES: 
        UID = request.COOKIES['UserID']
    sample = views.getUser(UID)
    pusher.trigger(u'a_channel', u'an_event', {u'name': sample[0][0], u'message': request.POST['message']})
#    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");