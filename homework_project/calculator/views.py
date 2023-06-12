from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        data = request.POST
        context = {
            'number_one': data.get('first_number'),
            'number_two': data.get('second_number'),
            'choose': data.get('choose')
        }
        number_one = int(context.get('number_one'))
        number_two = int(context.get('number_two'))
        operations = {
            '+': number_one + number_two,
            '-': number_one - number_two,
            '*': number_one * number_two,
            '/': number_one // number_two,
        }
        if context.get("choose") in operations:
            final_results = operations[context.get("choose")]
            context['results'] = final_results
            return render(request, 'pages/results.html', context)
    else:
        return render(request, 'pages/home.html')

# Create your views here.
