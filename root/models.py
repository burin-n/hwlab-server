from django.db import models

# Create your models here.


class State(models.Model):
	state = models.IntegerField(default='12')
	setting = models.CharField(max_length=100, default = '')
	humid = models.IntegerField(default = -100)
	temp = models.IntegerField(default = -100)
	manual = models.BooleanField(default = False)
	degree = models.BooleanField(default = True)

	def __str__(self):
		return "state: {}, setting: {}, manual: {}, degree: {}".format(str(self.state), self.setting ,str(self.manual),str(self.degree))


class Setting(models.Model):
	name = models.CharField(max_length=100)
	min_humid = models.IntegerField(default=35)
	max_humid = models.IntegerField(default=55)
	min_temp = models.IntegerField(default=20)
	max_temp = models.IntegerField(default=30)

	def __str__(self):
		return "name: {}, humid: {}/{}, temp: {}/{}".format(self.name,self.min_humid,self.max_humid,self.min_temp,self.max_temp)
