from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
# Create your views here.
from .models import State,Setting
from .tables import SettingTable, StateTable

def api(request):
	# pwm staet 10-45
	state = State.objects.all()[0]

	if(state.manual == True or request.method == 'GET' ):
		return HttpResponse(state.state)
	
	elif(request.method == 'POST'):
		settings = Setting.objects.all()
		setting = settings[0]
		if(len(state.using_setting) > 0 ):
			for s in settings:
				if(s.name == state.using_setting):
					setting = s
					break
		
		Changestate = 0
		isExtreme = False
		inputs = {}

		for e in request.body.decode('utf-8').split('&'):
			key,val = e.split("=")
			inputs[key] = val

		new_state = state.state
		if('humidity' in inputs.keys()):			
			print('humid')
			try:
				val_humid = int(inputs['humidity'])
				state.humid = val_humid
				if(val_humid > setting.humid_threshold):
					if(state.state == "on"):
						Changestate += 1
				else:
					if(state.state == "off"):
						Changestate += 1
				
				if( abs(val_humid-setting.humid_threshold) >= extreme_humid):
					isExtreme = True

			except ValueError:
				print('type error')

		
		if('temperature' in inputs.keys()):
			print('temp')
			try:
				val_temp = int(inputs['temperature'])
				state.temp = val_temp
				if(val_temp < setting.humid_threshold):
					if(state.state == "on"):
						Changestate += 1
				else:
					if(state.state == "off"):
						Changestate += 1

				if( abs(val_temp-setting.temp_threshold) > extreme_temp):
					isExtreme = True

			except ValueError:
				print('type error')

		if(Changestate == 2 or isExtreme):
			if(state.state == "on"):
				state.state = "off"
			else:
				state.staet = "on"

		state.save()
		return HttpResponse(state.state)

def index(request):
	state = State.objects.all()
	settings = Setting.objects.filter(name=state[0].setting)
#	RequestConfig(request).configure(StateTable(state))
	context = {
		'state' : state[0],
		'state_table' : StateTable(state),
		'settings' : SettingTable(settings),
    }
	return render(request, 'root/index.html', context)



def toggle(request):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('')
