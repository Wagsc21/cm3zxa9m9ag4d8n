
from django.db import models
from time import time
from django.contrib.auth import settings
class Query(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.TextField()
	details = models.TextField()
	pub_date = models.DateTimeField('date published')
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	#thumbnail = models.FileField(upload_to=get_upload_file_name)
	def __str__(self):
		return self.title

class Comment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL)
	name =  models.TextField()
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	query = models.ForeignKey(Query)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)


class Notification(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL)	
	name = models.TextField()
	query = models.ForeignKey(Query) 
