from bottle import route, get, post, request, run, template, static_file, error

# @route('/<action>/<user>')
# def user_api(action, user):
#     return template('action: {{action}}, user: {{user}}', action=action, user=user)

# @route('/show/<name:re:[a-z]+>')
# def alphabet(name):
#     assert name.isalpha()
#     return template("alphabet {{name}}", name=name)

@get('/login')
def login():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    """

@post('/login')
def do_login():
    reg_username = 'user'
    reg_password = 'pass'
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == reg_username and password == reg_password:
        return "<p>Login success.</p>"
    else:
        return "<p>Login failed.</p>"

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/Users/shibata/dev/python/tutorial-web/bottle')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080)
