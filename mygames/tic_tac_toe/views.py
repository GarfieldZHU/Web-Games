#coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .algorithm import *
import json

# Create your views here.

def index(request):
    if request.session.get('board', False):
        #新登录时如果有session，清空之
        del request.session['board']
    return render_to_response('tic_tac_toe/index.html', {})

def opponent(request):
    if request.method == 'GET':
        m = int(float(request.GET['m']))
        n = int(float(request.GET['n']))
        win = 0
        #如果session中没有缓存当前的棋盘，初始化棋盘
        if not request.session.get('board', False):
            board = [[0,0,0],[0,0,0],[0,0,0]]
            board[m][n] = 1
            #print 'no board', board
            p, q = ai_judge(board)
            print p, q
            board[p][q] = -1
            request.session['board'] = board
            data = (win, board)
            return HttpResponse(json.dumps(data))
        else:
            board = request.session['board']
            #print 'has board', board
            #若已缓存当前棋盘，判断点击位置是否有效
            if board[m][n] == 0:
                board[m][n] = 1
                #print "m, n: ", m, n
                p, q = ai_judge(board)
                #print "p, q: ", p, q
                board[p][q] = -1
                request.session['board'] = board
                win = if_win(board)
                data = (win, board)
                print data
                return HttpResponse(json.dumps(data))
            else:
                data = (win, board)
                return HttpResponse(json.dumps(data))

        return HttpResponse(json.dumps(data))
