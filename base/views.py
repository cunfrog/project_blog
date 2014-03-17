from django.shortcuts import render_to_response


def home(request):
    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False
    return render_to_response('base/home.html', {'loggedin': loggedin})


def login(request):
    return render_to_response('base/login.html')


def signup(request):
    return render_to_response('base/signup.html')


def logout(request):
    logout(request)
