from flask import Flask, url_for, redirect, render_template, request, session, make_response

app = Flask(__name__)

@app.route('/set_session')
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    session['username'] = 'shixiaolou'
    return 'session set on'

@app.route('/get_session')
def get_session():
    value = session.get('username')
    return 'session name: {}'.format(value)

@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return 'del session {}'.format(value)



@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/temp/<testname>')
def test_id(testname):
    resp = make_response(render_template('test_name.html', testname = testname))
    resp.set_cookie('username',testname)
    return resp

@app.route('/user/<username>')
def starinfo(username):
    return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def starid(post_id):
    return 'Hello {}'.format(post_id)

@app.route('/test')
def test():
    print(url_for('starinfo', username='zhoutangquan'))
    print(url_for('starid', post_id = 1314, _external=True))
    print(url_for('starid', post_id = 2, q='python haode'))
    print(url_for('starid', post_id = 2, _anchor='a'))
    return 'test'

@app.route('/<redirectname>')
def hello(redirectname):
    if redirectname == "haode":
        return 'hello {}'.format(redirectname)
    else:
        return redirect(url_for('test'))


@app.route('/requestargs/<requestname>')
def request_args(requestname):
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time:', request.args.getlist('time'))

    return 'Hello {}'.format(requestname)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('method:', request.method)
    print('name:', request.form['name'])
    print('hobbies:', request.form.getlist('hobbies'))

    return 'register successed!'

@app.route('/httptest', methods=['GET', 'POST'])
def httptest():
    if request.method == 'GET':
        print('t:', request.form['t'])
        print('q:', request.form['q'])
        return 'It is a get request'
    elif request.method == 'POST':
        print('Q:', request.form.getlist('Q'))
        return 'It is a post request'
    else:
        pass
    





if __name__ == '__main__':
    app.run()
