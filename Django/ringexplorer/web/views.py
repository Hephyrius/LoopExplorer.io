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
	print(data)
	#return render(request, 'AllRingsPage.html')
	return render_to_response('AllRingsPage.html', {'result':data})
	
def getRing(request):
	query = request.GET.get('ringindex')
	data = ring.objects.filter(ringindex = query)
	print(data)
	return render_to_response('RingBasic.html', {'result':data[0]})