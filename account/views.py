from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login

from .forms import LoginForm


def user_login(request):

    if request.method == 'POST':

        form = LoginForm()

        if form.is_valid():

            cd = form.cleaned_data
            user = authenticate(user=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Successfully authenticated')

                else:
                    return HttpResponse('Disabled user')

            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
