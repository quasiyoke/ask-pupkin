# -*- coding: utf-8 -*-

'''
3rd part of the first homework includes creating simple WSGI script. That's it!
'''

import cgi


ENCODING = 'utf-8'

def get_row(item):
    value = item[1]
    if len(value) > 1:
        value = '<ol>%s</ol>' % ''.join(['<li>%s</li>' % v for v in value])
    else:
        try:
            value = value[0]
        except IndexError:
            value = ''
    return '<tr><th>%s</th><td>%s</td></tr>' % (item[0], value, )

def application(environ, start_response):
    output = u'<h1>привет, мир</h1>'
    
    request_get_items = cgi.parse_qs(environ['QUERY_STRING']).items()
    if len(request_get_items):
        output += '<h2>GET</h2><table>%s</table>' % ''.join(map(get_row, request_get_items))

    try:
        request_body_size = int(environ['CONTENT_LENGTH'])
    except (ValueError, KeyError):
        pass
    else:
        request_body = environ['wsgi.input'].read(request_body_size)
        request_post_items = cgi.parse_qs(request_body).items()
        if len(request_post_items):
            output += '<h2>POST</h2><table>%s</table>' % ''.join(map(get_row, request_post_items))
    
    output = output.encode(ENCODING)
    response_headers = {
        'Content-Type': 'text/html; charset=%s' % ENCODING,
        'Content-Length': str(len(output)),
    }
    start_response('200 OK', response_headers.items())
    return [output]
