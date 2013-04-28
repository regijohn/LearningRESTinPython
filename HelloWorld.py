from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

@view_config(route_name = 'perfData', request_method = 'POST')
def receivePerfData(request): 
    print 'Data received from client: ' + str(request.json_body['data1'])
    return Response("Perf data received")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    #Add route for the declarative view
    config.add_route('perfData', '/perfdata')
    #Need to perform a scan to extrac the declared views
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
