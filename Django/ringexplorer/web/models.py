from django.db import models

class ring(models.Model):
	ringsize = models.CharField(max_length = 256)
	ringindex = models.CharField(max_length = 256)
	block = models.CharField(max_length = 256)
	timestamp = models.CharField(max_length = 256)
	chain = models.CharField(max_length = 256)
	ringhash = models.CharField(max_length = 256)
	mineraddress = models.CharField(max_length = 256)
	
	order1hash = models.CharField(max_length = 256)
	order1lrcReward = models.CharField(max_length = 256)
	order1lrcFeeState = models.CharField(max_length = 256)
	order1splitS = models.CharField(max_length = 256)
	order1splitB = models.CharField(max_length = 256)
	
	order2hash = models.CharField(max_length = 256)
	order2lrcReward = models.CharField(max_length = 256)
	order2lrcFeeState = models.CharField(max_length = 256)
	order2splitS = models.CharField(max_length = 256)
	order2splitB = models.CharField(max_length = 256)
	
	order3hash = models.CharField(max_length = 256)
	order3lrcReward = models.CharField(max_length = 256)
	order3lrcFeeState = models.CharField(max_length = 256)
	order3splitS = models.CharField(max_length = 256)
	order3splitB = models.CharField(max_length = 256)
