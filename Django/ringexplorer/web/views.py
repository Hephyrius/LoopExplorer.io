from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.db.models import F
from django.core.paginator import Paginator
from .models import ring
from .forms import ringIndexForm


def index(request):
	if request.method == 'GET':
		print(request.GET)
	
	data = ring.objects.all().order_by('-id')[:10]
	
	form = ringIndexForm()
	
	context={'result':data, 'form': form}
	return render_to_response('HomePage.html', context)

def allRings(request):
	data = ring.objects.all()
	
	form = ringIndexForm()
	
	paginator = Paginator(data, 15)
	
	page = request.GET.get('page')
	data = paginator.get_page(page)
	
	context={'result':data, 'form': form}
	return render_to_response('AllRingsPage.html', context)
	
def getRing(request):
	query = request.GET.get('ringindex')
	data = ring.objects.filter(ringindex = query).annotate(
	lrcFees=F('order1lrcFeeState')+F('order2lrcFeeState')+F('order3lrcFeeState')).annotate(
	rate=F('order1fillamount')/F('order2fillamount'))

	form = ringIndexForm()
	context={'result':data[0],'form': form}
	
	return render_to_response('RingBasic.html', context)