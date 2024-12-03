"""
启动命令:
uwsgi --http :9090 --wsgi-file foobar.py
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]

