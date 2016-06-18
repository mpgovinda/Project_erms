from django.http import Http404
# from django.contrib.auth import
from django.shortcuts import render
from django.shortcuts import RequestContext, redirect
from datetime import date, datetime
from .forms import *


def login(request):
    loginForm = LoginForm()
    return render(request, 'login.html', {'loginForm': loginForm})


def hod(request):
    return render(request, 'hod.html', {})


def hod_cv(request):
    form = Person.objects.all()
    # form2 = Degree.objects.all()
    return render(request, 'hod_cv.html', {'form_cv': form})


def hod_inter(request):
    return render(request, 'hod_inter.html', {})


def hod_inter_create(request):
    context = RequestContext(request)
    if request.method == 'POST':
        inter_form = InterviewForm(request.POST)

        if inter_form.is_valid():
            inter = inter_form.save(commit=False)
            inter.user = request.user
            inter.save()

            return redirect('/hod/hod_inter/hod_succs')
        else:
            print inter_form.errors
    else:
        inter_form = InterviewForm()
    return render(request, 'hod_inter_create.html', {'inter_form': inter_form}, context)


# def hod_cv_filter(request):
#     context = RequestContext(request)
#     if request.method == request.GET('')


def hod_succs(request):
    return render(request, 'hod_succs.html', {})


def hod_inter_overview(request):
    inter_obj = Interview()
    Date = date.today()
    if inter_obj.Date == Date:
        form = Interview.objects.all(Date=Date)
        event = 'Today Interviews'
        context1 = {
            'event1': event,
            'ovr_form_1': form,
        }
    if inter_obj.Date < Date:
        form = Interview.objects.all(Date=Date)
        event = 'Past Interviews'
        context2 = {
            'event2': event,
            'ovr_form_2': form,
        }
    if inter_obj.Date > Date:
        form = Interview.objects.all(Date=Date)
        event = 'Future Interviews'
        context3 = {
            'event3': event,
            'ovr_form_3': form,
        }

    return render(request, 'hod_inter_overview.html', (context1, context2, context3))


# def hod_profile(request, NIC):
#     return HttpResponse("<h1>Profile of NIC:"+NIC+"</h1>")

def hod_profile(request, NIC):
    try:
        profile = Person.objects.get(NIC=NIC)
        context = RequestContext(request)
        if request.method == 'POST':
            hod = HodReviewForm(request.POST, request.FILES)
            if hod.is_valid():
                review = hod.save(commit=False)
                review.user = request.user
                review.save()

                return redirect('')
            else:
                print hod.errors
        else:
            hod = HodReviewForm()
    except Person.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'hod_cv_profile.html', {'hod_form': hod, 'pro_form': profile}, context)


def hod_msg(request):
    return render(request, 'hod_msg.html', {})


def hod_send_msg(request):

    context = RequestContext(request)
    if request.method == 'POST':
        msg_form = HodMessageForm(request.POST)
        if request.user.is_authenticated():
            if msg_form.is_valid():
                msg = msg_form.save(commit=False)
                msg.user = request.user
                msg.save()
                return redirect('/hod/hod_msg/send')
            else:
                print msg_form.errors
    else:
        msg_form = HodMessageForm()
    return render(request, 'hod_send_msg.html', {'msg_form': msg_form}, context)


def hod_msg_succs(request):
    msg_obj = Message_Send()
    if request.user.is_authenticated():
        username = request.user.username
        msg_obj.Sender = username
        msg_obj.SentDate = date.today()
        msg_obj.SentTime = datetime.time()
        dsc = True
        context = {
            'dsc': dsc,
        }
    else:
        error = 'User authentication error'
        context = {
            'error': error,
        }

    return render(request, 'hod_msg_succs.html', context)


def hod_recieve_msg(request):
    usr = request.user.username
    if request.user.is_authenticated():
        msg = Message_Recieve.objects.get(Reciever=usr)
        context = {
            'msg': msg,
        }
    else:
        error = 'User is not Authenticated one.'
        context = {
            'error': error,
        }
    return render(request, 'hod_recieve_msg.html', context)


def deo(request):
    context = RequestContext(request)
    if request.method == 'POST':
        deoForm = PersonForm(request.POST)

        if deoForm.is_valid():
            data = deoForm.save(commit=False)
            data.user = request.user
            data.save()

            return redirect('/deo/deo_submit/')
        else:
            print deoForm.errors

    else:
        deoForm = PersonForm()
    return render(request, 'deo.html', {'deoForm': deoForm}, context)


def deo_submit(request):
    return render(request, 'deo_submit.html', {})


def deo_profile(request):
    profile_form = Person.objects.all()
    return render(request, 'deo_profile.html', {'profile_form': profile_form})
