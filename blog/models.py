from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	Plant_Model = models.CharField(max_length = 100)
	Customer_Name = models.CharField(max_length = 100)
	Pre_Order_Sheet_No = models.IntegerField ()
	Date_Of_Delivery = models.DateTimeField(default = timezone.now)
	Sales_Persons_Name = models.ForeignKey(User, on_delete = models.CASCADE)
	Random_Key = models.IntegerField()

	def __str__(self):
		return self.Plant_Model

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk': self.pk})	


