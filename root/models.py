from django.db import models

# Create your models here.


class State(models.Model):
    state = models.CharField(max_length=10, default='on')
    using_setting = models.CharField(max_length=100, default = '')

    def __str__(self):
    	return "state: " + self.state + ", setting: " + str(self.using_setting)


class Setting(models.Model):
	humid_threshold = models.IntegerField(default=50)
	temp_threshold = models.IntegerField(default=50)
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return "name: " + self.name + ", humid_threshold: " + str(self.humid_threshold) +\
				", temp_threshold: " + str(self.temp_threshold)

