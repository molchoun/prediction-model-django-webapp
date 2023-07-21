from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

@login_required
def profile(request):
    houses = request.user.house.all()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(request.META)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return render(
        request,
        'profile.html',
        {'section': 'profile',
         'user': request.user,
         'recent_predictions': houses}
    )


def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
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
