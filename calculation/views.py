from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import CalculationForm
from .models import Calculation


# class Calculations(ListView):
#     model = Calculation
#     template_name = 'home.html'

#     def get_queryset(self):
#         return self.model.objects.order_by('-pk')[:10]


class Calculations(generic.CreateView):
    model = Calculation
    template_name = 'home.html'
    success_url = '#'
    form_class = CalculationForm

    def get_context_data(self, *args, **kwargs):
        context = super(Calculations, self).get_context_data(*args, **kwargs)
        context['calculations'] = Calculation.objects.order_by('-pk')[:10]
        return context

    def form_valid(self, form):
        response = super(Calculations, self).form_valid(form)
        calc = self.object
        calc.result = eval(calc.expression)
        calc.save()
        return response
        return HttpResponse('foo')


# def calculations(request):

#     if request.method == 'POST':
#         form = CalculationForm(data=request.POST)
#         if form.is_valid():
#             return HttpResponse('ok')
#         else:
#             return render(request, 'home.html',
#                           {'form': form,
#                            'errors': form.errors})
#     else:
#         form = CalculationForm()
#         calculations = Calculation.objects.order_by('-pk')[:10]
#         context = {
#             'calculations': calculations,
#             'form': form,
#         }
#         return render(request, 'home.html', context)
