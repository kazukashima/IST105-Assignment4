from django.shortcuts import render
from .forms import InputForm
import math

def calculator_view(request):
    result = None
    error = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            try:
                if a < 1:
                    error = 'Value A is too small.'
                elif b == 0:
                    error = 'Value B is zero and will not affect the result.'
                elif c < 0:
                    error = 'Value C must be non-negative.'
                else:
                    c3 = c ** 3
                    if c3 > 1000:
                        base = math.sqrt(c3) * 10
                    else:
                        base = math.sqrt(c3) / a
                    result = base + b
            except Exception as e:
                error = f'Calculation error: {str(e)}'
        else:
            error = 'Invalid input. Please enter numbers.'
    else:
        form = InputForm()
    return render(request, 'calcapp/result.html', {'form': form, 'result': result, 'error': error})
