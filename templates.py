from bottle import request, route, template, run, debug

@route('/hello')
@route('/hello/<name>')
def hello(name="World"):
    return template('hello_template', name=name)

run(host='localhost', port=8080, debug=True, reloader=True)
