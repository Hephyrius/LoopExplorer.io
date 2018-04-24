from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .models import ring
from .forms import ringIndexForm

def index(request):
	if request.method == 'GET':
		print(request.GET)
		
	form = ringIndexForm()
	
	context={'form': form}
	return render(request, 'HomePage.html', context)

def allRings(request):
	data = ring.objects.all()
	
	form = ringIndexForm()
	context={'result':data, 'form': form}
	
	return render_to_response('AllRingsPage.html', context)
	
def getRing(request):
	query = request.GET.get('ringindex')
	data = ring.objects.filter(ringindex = query)
	
	form = ringIndexForm()
	context={'result':data[0], 'form': form}
	
	return render_to_response('RingBasic.html', context)