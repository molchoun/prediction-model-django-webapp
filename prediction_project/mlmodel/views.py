from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import HouseForm
from .models import House
from .prediction import get_prediction_model, process_data
from django.contrib.auth import get_user_model


class HomePageView(TemplateView):
    template_name = 'home.html'


def form_view(request):
    prediction = ''
    user = get_user_model()
    public_user = user.objects.get(username='public')
    recent_predictions = House.objects.filter(author=public_user).order_by('-id')[:10]

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            model = get_prediction_model()
            df = process_data(cd)
            prediction = model.predict(df)[0]

            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.author = request.user
            else:
                form.author = public_user
            form.prediction = float(prediction)
            form.save()
            return JsonResponse({'prediction': "{:.2f}".format(prediction)})
    else:
        form = HouseForm()
    return render(
        request,
        'prediction_form.html',
        {
            'form': form,
            'prediction': prediction,
            'recent_predictions': recent_predictions
        }
    )

