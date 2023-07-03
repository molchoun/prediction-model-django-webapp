from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import HouseForm
from .prediction import get_model, process_data


class HomePageView(TemplateView):
    template_name = 'home.html'


def form_view(request):
    prediction = ''
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            # cd['elevator'], cd['new_construction'] = int(cd['elevator']), int(cd['new_construction'])
            model = get_model()
            df = process_data(cd)
            prediction = model.predict(df)[0]

            return JsonResponse({'prediction': "{:.2f}".format(prediction)})
    else:
        form = HouseForm()
    return render(
        request,
        'prediction_form.html',
        {
            'form': form,
            'prediction': prediction
        }
    )

