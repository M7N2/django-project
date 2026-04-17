from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	"""Blog post model"""
	title = models.CharField(max_length=200)
	text = models.TextField(max_length=2000)
	date_added = models.DateTimeField(auto_now_add=True)
	# Associating data with a specific user.
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.title