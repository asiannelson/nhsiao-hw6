from pyramid.config import Configurator
from views import *

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('color', '/color/{query}')

    config.add_route('form','/form')
    config.add_route('form_handler','/form_handler')

    config.scan()
    return config.make_wsgi_app()