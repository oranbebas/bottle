from bottle import route, static_file, abort, redirect, run

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/Users/shibata/dev/python/tutorial-web/bottle', download=filename)

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

@route('/wrong/url')
def wrong():
    redirect('right/url')

run(host='localhost', port=8080)
