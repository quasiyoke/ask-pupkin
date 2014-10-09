# -*- coding: utf-8 -*-

'''
3rd part of the first homework includes creating simple WSGI script. That's it!
'''


ENCODING = 'utf-8'

def application(environ, start_response):
    output = u'привет, мир'
    output = output.encode(ENCODING)
    response_headers = {
        'Content-Type': 'text/plain; charset=%s' % ENCODING,
        'Content-Length': str(len(output)),
    }
    start_response('200 OK', response_headers.items())
    return [output]
