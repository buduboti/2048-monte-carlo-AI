from tkinter import *
from puzzle import *
from random import randint
from threading import Thread
import copy

N, M = 100, 10

def V(t):
    s, e = 0, 0.
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0 :
                s, e = s + t[i][j], e + 1
    return s/e
"""
def V(t):
    m, e = 0, 0.
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0 :
                e += 1
            if t[i][j] > m :
                m = t[i][j]
    return m/e
"""
def test(gg):
    for j in range(M):
        i = randint(0, 3)
        if i == 0 :
            gg.ifai(KEY_UP)
        elif i == 1 :
            gg.ifai(KEY_DOWN)
        elif i == 2 :
            gg.ifai(KEY_LEFT)
        elif i == 3 :
            gg.ifai(KEY_RIGHT)
    return V(gg.matrix)


def test_N(gg):
    e = 0.
    for i in range(N):
        tg = copy.copy(gg)
        try:
            e += test(tg)
        except ValueError as e:
            print 'Time out!'
    return e/N
"""

def test_N(gg):
    e = 0.
    for i in range(N):
        tg = copy.copy(gg)
        temp = test(tg)
        if temp > e:
            e = temp
    return e
"""
def mat_out(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sys.stdout.write(str(mat[i][j]) + '\t')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

def ai(_N, _M):
    global N
    global M
    N, M = int(_N), int(_M)
    w, l, gg = 0, 0, GameGrid()
    f = open('stat.txt', 'a')

    ok = True

    while True:
        gs = game_state(gg.matrix)
        tg1, tg2, tg3, tg4 = copy.copy(gg), copy.copy(gg), copy.copy(gg), copy.copy(gg)
        #print 'Status 1'
        tg1.ifai(KEY_UP)
        tg2.ifai(KEY_DOWN)
        tg3.ifai(KEY_LEFT)
        tg4.ifai(KEY_RIGHT)
        #print 'Status 2'
        t1, t2, t3, t4 = test_N(tg1), test_N(tg2), test_N(tg3), test_N(tg4)
        #print 'Status 3'
        if t1 > t2 and t1 > t3 and t1 > t4 and gg.matrix != tg1.matrix : # UP
            gg.ifai(KEY_UP)
        elif t2 > t3 and t2 > t4 and gg.matrix != tg2.matrix : # DOWN
            gg.ifai(KEY_DOWN)
        elif t3 > t4 and gg.matrix != tg3.matrix : # LEFT
            gg.ifai(KEY_LEFT)
        elif gg.matrix != tg4.matrix : # RIGHT
            gg.ifai(KEY_RIGHT)
        else :
            if t1 > t2 and t1 > t3 and gg.matrix != tg1.matrix : # UP
                gg.ifai(KEY_UP)
            elif t2 > t3  and gg.matrix != tg2.matrix : # DOWN
                gg.ifai(KEY_DOWN)
            elif gg.matrix != tg3.matrix : # LEFT
                gg.ifai(KEY_LEFT)
            else:
                if t1 > t2 and gg.matrix != tg1.matrix : # UP
                    gg.ifai(KEY_UP)
                elif gg.matrix != tg2.matrix : # DOWN
                    gg.ifai(KEY_DOWN)
                else :
                    if gg.matrix != tg1.matrix : # UP
                        gg.ifai(KEY_UP)
                    else:
                        gs = 'lose'
        #print 'Status 4'
        #mat_out(gg.matrix)
        gg.update_grid_cells()
        #print 'Status 5'
        if ok :
            if gs == 'win':
                e = gg.max()
                gg.quit()
                return e
                print("You Win!")
                ok = False
                f.write('1')
                s = raw_input()
        if gs == 'lose':
            e = gg.max()
            gg.quit()
            return e
            print("You Lose!")
            f.write('0')
            break

    gg.update_grid_cells()
    mat_out(gg.matrix)
