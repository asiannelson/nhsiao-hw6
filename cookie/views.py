from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.url import route_url

#@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
#def my_view(request):
	#return {'project': 'Pyramid Scaffold'}
@view_config(route_name='color', renderer='templates/mytemplate.jinja2')
def my_view_color(request):
	mydict = request.matchdict
	return {'color': mydict['query']}

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
	return {'project': 'nhsiao-hw6'}

@view_config(route_name ='form', renderer='templates/template.jinja2')
def form(request):
	return {'project': 'nhsiao-hw6'}

@view_config(request_method ='POST', route_name='form_handler', renderer='templates/mytemplate.jinja2')
def colorView(request):
	print (request.POST['color'])
	return {'bgcolor': request.POST['color']}