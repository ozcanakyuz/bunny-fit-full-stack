from django.http import HttpResponse
from django.shortcuts import render


def index(request):
        return render(request, 'index.html', {'page': 'Home'})

    # if request.method == 'POST':  #check post
    #     login_form = LoginForm(request.POST)
    #     signup_form = SignUpForm(request.POST)
    #     if 'login_submit' in request.POST:     #! LOG IN FORM
    #         if login_form.is_valid():
    #             username = login_form.cleaned_data['username']
    #             password = login_form.cleaned_data['password']
    #             user = authenticate(username=username, password=password)
    #             if user is not None:
    #                 login(request, user)
    #                 messages.success(request, "You have successfully logged in {}".format(user.username))
    #                 return HttpResponseRedirect('/')
    #             else:
    #                 messages.warning(request, "The Information Entered Is Incorrect, Try Again! {}".format(username))
    #                 return HttpResponseRedirect('/')
    #     elif 'signup_submit' in request.POST:  #! SIGN UP FORM
    #         if signup_form.is_valid():
    #             signup_form.save()
    #             username = signup_form.cleaned_data.get('username')
    #             password = signup_form.cleaned_data.get('password')
    #             user = authenticate(username=username, password=password)
    #             login(request, user)
    #             current_user = request.user
    #             data = UserProfile()
    #             data.user_id = current_user.id
    #             data.image="images/users/user.png"
    #             data.save()
    #             messages.success(request, 'Your account has been created!')
    #             return HttpResponseRedirect('/user')
    #         else:
    #             messages.warning(request, signup_form.errors)
    #             return HttpResponseRedirect('/')
    #     else:
    #         login_form = LoginForm()
    #         signup_form = SignUpForm()
    #     login_form = LoginForm()
    #     signup_form = SignUpForm()
    #     context = {'login_form': login_form,
    #                'signup_form': signup_form,
    #                'page_obj': page_obj,
    #                'page': 'Home',} 
    #     return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html', {'page': 'Log In'})