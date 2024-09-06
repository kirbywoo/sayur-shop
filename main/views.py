from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Eva Yunia Aliyanshah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)