from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .models import ring

def index(request):
	return render(request, 'HomePage.html')
	
def allRings(request):
	data = ring.objects.all()
	print(data)
	#return render(request, 'AllRingsPage.html')
	return render_to_response('AllRingsPage.html', {'result':data})
	
def getRing(request):
	return render(request, 'RingBasic.html')