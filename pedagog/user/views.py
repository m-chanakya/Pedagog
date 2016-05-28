from user.models import *
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
	template_name = 'accounts/index.html'
	context = RequestContext(request, {'user': request.user, 'request': request})
	return render_to_response(template_name, context_instance=context)

class login(View):
	template_name = 'accounts/login.html'

	def post(self, request, *args, **kwargs):
		response = {'status' : 0}
		login_data = request.POST
		user = None
		email = login_data.get('email', None)
		password = login_data.get('password', None)
		if not email or not password:
			response['status'] = 1
			response['message'] = 'Missing details in form.'
			return HttpResponse(json.dumps(response), content_type="application/json")	
		if User.objects.filter(email = email).exists():
			user = User.objects.get(email = email)
			user = auth.authenticate(username = user.username, password = password)
		elif User.objects.filter(username = email).exists():
			user = auth.authenticate(username = email, password = password)
		if user:
			auth.login(request, user)
			# if user.is_active:
			# 	auth.login(request, user)
			# else:
			# 	response['status'] = 1
			# 	response['message'] = 'Confirm email address'			
		else:
			response['status'] = 1
			response['message'] = 'The credentials you entered were invalid.'
		return HttpResponse(json.dumps(response), content_type="application/json")
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('home')
		return render_to_response(self.template_name, context_instance=RequestContext(request))

class signup(View):
	def post(self, request, *args, **kwargs):
		response = {'status' : 0}
		user_data = request.POST
		try:
			with transaction.atomic():
				username = user_data['username']
				email = clean_email(user_data['email'])
				first_name = user_data['first_name']
				last_name = user_data['last_name']
				password = user_data['password']
				#salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
				#activation_key = hashlib.sha1(salt+email).hexdigest()  
				user = User(
					username = username,
					email = email,
					first_name = first_name,
					last_name = last_name
					)
				user.set_password(password)
				#user.is_active = False
				user.save()
				#profile = Profile.objects.get(user = user)
				#profile.activation_key = activation_key
				#profile.save()
				#print user.pk
				#send_activation_email.delay(user_id = user.pk)
				#response['message'] = 'Activation email has been sent'
		except Exception as e:
			transaction.rollback()
			response['status'] = 1
			response['message'] = str(e[0])
		return HttpResponse(json.dumps(response), content_type="application/json")

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('home')
		return redirect('/accounts/login#signup')