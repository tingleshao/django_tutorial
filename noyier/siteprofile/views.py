# Create your views here.

from django.http import HttpResponse


def welcome(request):
	image_data = open("static/images/1.jpg","rb").read()
	# output = 'hello!'
	return HttpResponse(image_data, mimetype="image/jpg")
	
	