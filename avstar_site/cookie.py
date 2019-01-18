from flask import Flask, render_template, request, make_response, redirect, url_for

app= Flask(__name__)

app.config['SECRET_KEY'] = 'XXX'

@app.route('/')
def index():
    return render_template('cookie_index.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    #if request.method == 'POST':
        resp = make_response(render_template('cookie_index.html'))
        print(request.form.get('name'))
        resp.set_cookie('userID', request.form.get('name'))
        resp.set_cookie('test', 'test')
        print(request.cookies)
        return render_template('readcookie.html')

@app.route('/getcookie')
def getcookie():
    user = request.cookies.get('userID')
    print(user)
    return '<h1>welcome, {}</h1>'.format(user)
