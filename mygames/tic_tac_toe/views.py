from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import json

# Create your views here.

def index(request):
    return render_to_response('tic_tac_toe/index.html', {})

def opponent(request):
    if request.method == 'GET':
        m = int(float(request.GET['m']))
        n = int(float(request.GET['n']))
        #print m, n
        if request.session.get('board', False):
            print 'here'
            board = request.session['board']
            board = [[0,0,0],[0,0,0],[0,0,0]]
            board[m][n] = 1
            return HttpResponse(json.dumps(board))
        else:
            pass
        request.session['board'] = board
        return HttpResponse(json.dumps(board))
