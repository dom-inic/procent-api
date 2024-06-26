from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm

@login_required
def dashbaord(request):
    return render(request, 'users/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password 
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # save user object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form':user_form})
