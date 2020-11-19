from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
from .regression import linear_regressor, knn_regressor, decision_tree_regressor, idSearch, acutual
import numpy


def football(request):
    global player_name
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['player_name']
            id = idSearch(str(player_name))
            if id == 0:
                player_name, acut, lin, knn, dt, error = None, None, None, None, None, 'Player does not exist!'
            else:
                acut = acutual(int(id))
                l = linear_regressor(int(id))
                lin = numpy.around(l, decimals=1)
                knn = knn_regressor(int(id))
                dt = decision_tree_regressor(int(id))
                lin = lin[0][0]
                knn = knn[0][0]
                dt = dt[0]
                error = ''
    else:
        form = SearchForm()
        player_name, error = None, ''
        acut = ''
        lin = ''
        knn = ''
        dt = ''
    return render(request, 'polls/football_analysis.html', {'form': form, 'player_name': player_name, 'acut': acut,
                                                            'lin': lin, 'knn': knn, 'dt': dt, 'error': error})


def about(request):
    return render(request, 'polls/about.html')


def rmse(request):
    rl, rk, rd = 2.8, 1.5, 1.3
    return render(request, 'polls/rmse.html', {'rl': rl, 'rk': rk, 'rd': rd})
