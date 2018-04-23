from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

def index(request):
	return render(request, 'HomePage.html')
	
def allRings(request):
	return render(request, 'AllRingsPage.html')
	
def getRing(request):
	return render(request, 'RingBasic.html')