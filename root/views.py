from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
# Create your views here.
from .models import State,Setting
from .tables import SettingTable, StateTable
# pwm state 10-45
MAX_SERVO = 40
MIN_SERVO = 12
SERVO_RANGE = MAX_SERVO - MIN_SERVO

def api(request):

	state = State.objects.all()[0]

	if(request.method == 'GET' ):
		return HttpResponse("1"*state.state)
	
	elif(request.method == 'POST'):
		settings = Setting.objects.all()
		setting = settings[0]
		if(len(state.setting) > 0 ):
			for s in settings:
				if(s.name == state.setting):
					setting = s
					break
		
		isExtreme = False
		inputs = {}
		N = 0
		humid_pwm = 0
		temp_pwm = 0

		print(request.body.decode('utf-8').split('&'))
		for e in request.body.decode('utf-8').split('&'):
			key,val = e.split("=")
			inputs[key] = val

		if('humidity' in inputs.keys()):			
			try:
				val_humid = int(inputs['humidity'])
				state.humid = val_humid

				humid_range = (setting.max_humid - setting.min_humid)//2
				center = (setting.min_humid+setting.max_humid)/2
				distant = abs(val_humid - center)

				if(distant >= humid_range):
					isExtreme = True
				else:
					humid_pwm = (SERVO_RANGE*(humid_range-distant))/humid_range
				N+=1
						
			except ValueError:
				print('type error')

		
		if('temperature' in inputs.keys()):
			try:
				val_temp = int(inputs['temperature'])
				state.temp = val_temp

				temp_range = (setting.max_temp - setting.min_temp)//2
				center = (setting.max_temp + setting.min_temp)/2
				distant = abs(val_temp - center)
				
				if(distant >= temp_range):
					isExtreme = True
				else:
					temp_pwm = (SERVO_RANGE*(temp_range-distant))/temp_range
				N+=2

			except ValueError:
				print('type error')

		if(not state.manual and N>0):
			if(isExtreme):
				state.state = MIN_SERVO
			else:
				deg = int(humid_pwm+temp_pwm)//N	
				if(state.degree == True):
					state.state = deg + 12
				else:
					state.state = MAX_SERVO


		state.save()

		return HttpResponse("1"*state.state)

def index(request):
	state = State.objects.all()
	settings = Setting.objects.filter(name=state[0].setting)
	deg = ((state[0].state-10)*180)//SERVO_RANGE
	deg = max(0,min(deg,180))
	text = ''
	if(deg == 0):
		text = "Close"
	else:
		text = "Open {} degrees".format(deg)


	
	context = {
		'text' : text,
		'state' : state[0],
		'state_table' : StateTable(state),
		'settings' : SettingTable(settings),
    }
	return render(request, 'root/index.html', context)