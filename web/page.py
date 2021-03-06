from numpy import array
import random as rd
import math
import flask
from flask import Flask, request

ab_vect = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4  , 7.0],
    [2.0, 1.0, 4.0, 3  , 8.0]
], dtype=float)

def vector_gauss(ab_vect):
    ab_vect = ab_vect.copy()
    d = len(ab_vect)

    for x in range(d):
        ab_vect[x] = ab_vect[x] / ab_vect[x,x]
        for i in range(x+1,d):
            ab_vect[i] = ab_vect[i] - ab_vect[x]*ab_vect[i,x]


    for x in range(2, d+1):
        for i in range(d-x, -1, -1):
            ab_vect[i] = ab_vect[i] - ab_vect[d-x+1]*ab_vect[i,d-x+1]


    x = ab_vect[:, -1]
    return x


def gcd(a_number,b_number):
    if b_number == 0:
        return a_number
    else:
        return gcd(b_number, a_number % b_number)

def extended_gcd(a_number,b_number):
    if a_number == 0:
        return (0, 1)
    else:
        x_num , y_num = extended_gcd(b_number % a_number, a_number)
    return ( y_num - (b_number // a_number) * x_num, x_num)

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/', methods = ['GET','POST'])
def root():
    return flask.render_template(
        'base.html'
    )


@app.route('/gauss', methods = ['GET','POST'])
def gauss():
    if request.method == 'POST':
        ab_vect[0,0] = request.form.get('a1', type=int)
        ab_vect[0,1] = request.form.get('a2', type=int)
        ab_vect[0,2] = request.form.get('a3', type=int)
        ab_vect[0,3] = request.form.get('a4', type=int)
        ab_vect[0,4] = request.form.get('a5', type=int)
        ab_vect[1,0] = request.form.get('b1', type=int)
        ab_vect[1,1] = request.form.get('b2', type=int)
        ab_vect[1,2] = request.form.get('b3', type=int)
        ab_vect[1,3] = request.form.get('b4', type=int)
        ab_vect[1,4] = request.form.get('b5', type=int)
        ab_vect[2,0] = request.form.get('c1', type=int)
        ab_vect[2,1] = request.form.get('c2', type=int)
        ab_vect[2,2] = request.form.get('c3', type=int)
        ab_vect[2,3] = request.form.get('c4', type=int)
        ab_vect[2,4] = request.form.get('c5', type=int)
        ab_vect[3,0] = request.form.get('d1', type=int)
        ab_vect[3,1] = request.form.get('d2', type=int)
        ab_vect[3,2] = request.form.get('d3', type=int)
        ab_vect[3,3] = request.form.get('d4', type=int)
        ab_vect[3,4] = request.form.get('d5', type=int)
    task_1 = vector_gauss(ab_vect)
    return flask.render_template(
    'gauss.html',
    vect_1 = ab_vect[0],
    vect_2 = ab_vect[1],
    vect_3 = ab_vect[2],
    answer_g = task_1
    )


@app.route('/euclid', methods = ['GET','POST'])
def euclid():
    if request.method == 'POST':
        a_num=request.form.get('a_num', type=int)
        b_num=request.form.get('b_num', type=int)
    else:
        a_num=rd.randint(1,100)
        b_num=rd.randint(1,100)
    short = gcd(a_num, b_num)
    pro = extended_gcd(a_num,b_num)
    return flask.render_template(
        'euclid.html',
        a = a_num,
        b = b_num,
        ans_1 = short,
        ans_2_1 = pro[0],
        ans_2_2 = pro[1]
    )

if __name__ == '__main__':
   app.run(debug = True)
