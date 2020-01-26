from django.shortcuts import render
from chart.calculator import get_result_points


# Create your views here.


def viewer(request):
    if request.method == 'POST':
        form = request.POST.dict()

        a = form.get("a")
        b = form.get("b")
        w0 = form.get("w0")
        dt = form.get('dt')
        t1 = form.get('t1')
        t2 = form.get('t2')


        points_sets = get_result_points(a, b, w0, dt, t1, t2)

    return render(request, 'viewer.html',
                  {'points_set_1': points_sets[0], 'points_set_2': points_sets[1]
                   ,'points_set_3': points_sets[2]})


def form(request):
    return render(request, 'form.html')
