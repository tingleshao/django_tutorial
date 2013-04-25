from django.db import models

class News(models.Model):
	title = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date published')
	content = models.TextField()
	tag_line = models.TextField()
	source = models.CharField(max_length=50)
	views = models.IntegerField()
	image = models.ImageField(upload_to='uploads/images')