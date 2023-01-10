from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'emit/index.html', context)


def space(request, space):
    context = {
        'space': space
    }

    return render(request, 'emit/space.html', context)
