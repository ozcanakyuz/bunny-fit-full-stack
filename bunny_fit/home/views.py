from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render


from home.forms import LoginForm, SignUpForm
from home.models import UserProfile

#! LOG IN & SIGN-UP
def index(request):
        if request.method == 'POST': #?check post
            login_form = LoginForm(request.POST)
            signup_form = SignUpForm(request.POST)
            if 'login_submit' in request.POST:  #! LOG IN FORM
                 if login_form.is_valid():   #* IF THE DATA IS VALID
                    username = login_form.cleaned_data['username']
                    password = login_form.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        login(request,user)
                        messages.success(request, "Başarılı bir şekilde giriş yaptınız {}".format(user.username))
                        return HttpResponseRedirect('/')
                    else:
                        messages.warning(request, "Kullanıcı adı veya Parola hatalı! {}".format(username))
            elif 'signup_submit' in request.POST:  #! SIGN UP FORM
                if signup_form.is_valid():
                    signup_form.save()
                    username = signup_form.cleaned_data.get('username')
                    password = signup_form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    current_user = request.user
                    data = UserProfile()
                    data.user_id = current_user.id
                    data.image="images/users/user.png"
                    data.save()
                    messages.success(request, 'Hesabınız oluşturuldu!')
                    return HttpResponseRedirect('/user')
                else:
                    messages.warning(request, signup_form.errors)
                    return HttpResponseRedirect('/')
            else:
                login_form = LoginForm()
                signup_form = SignUpForm()
                context = {'login_form': login_form,
                        'signup_form': signup_form,
                        'page': 'Home',} 
                return render(request, 'index.html', context)
        return render(request, 'index.html', {'page': 'Home'})

#! LOG OUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
