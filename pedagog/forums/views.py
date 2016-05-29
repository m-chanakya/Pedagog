from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
	template_name = 'forums/index.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)
	