from django.http import HttpResponse


def show_contacts(request):
	output = 'show contacts: tom, jerry...'
	return HttpResponse(output)
	
