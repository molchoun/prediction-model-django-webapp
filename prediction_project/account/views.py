from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required
def profile(request):
    return render(
        request,
        'profile.html',
        {'section': 'profile'}
    )


def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request,
                'registration/signup_done.html',
                {'new_user': new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'registration/signup.html',
        {'user_form': user_form}
    )
