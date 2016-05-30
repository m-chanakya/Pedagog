from django.shortcuts import render_to_response
from django.template.context import RequestContext

	
def topics(request):
	template_name = 'forums/topics.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)
	
def threads(request):
	template_name = 'forums/threads.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)

def questions(request):
	template_name = 'forums/questions.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)

def question(request):
	template_name = 'forums/question.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)