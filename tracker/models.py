from django.db import models
from django.utils import timezone

class Evidence(models.Model):
	requestor = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateField(default=timezone.now)
	required_date = models.DateField()
	system = models.CharField(max_length=200)
	owner = models.CharField(max_length=200)
	received = models.BooleanField(default = False)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title


class Engagements(models.Model):
	clientName = models.CharField(max_length = 30)
	engagementType = models.CharField(max_length  = 30)
	