from django.db import models
import datetime

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_data = models.DateTimeField('data published')
	def __unicode__(self):
		return self.question
		
	def was_published_today(self):
		return self.pub_data.date() == datetime.date.today()
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
	
