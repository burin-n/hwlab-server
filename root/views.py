from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
# Create your views here.
from .models import State,Setting
from .tables import SettingTable, StateTable

def api(request):
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
		
		inputs = request.body.decode('utf-8').split('&')
		Changestate = False

		name,val = inputs[0].split('=')
		name1 = ''
		val1 = -1
		if(len(inputs) > 1 ):
			name1,val1 = inputs[1].split('=')
		val_humid = -1
		val_temp = -1

		if(name == 'humidity'):
			val_humid = val
		elif(name1 == 'humidity'):
			val_humid = val1

		if(name == 'temperature'):
			val_temp = val
		elif(name1 == 'temperature'):
			val_temp = val1

		if(val_humid != -1):			
			try:
				val_humid = int(val_humid)
				if(val_humid > setting.humid_threshold):
					if(state.state == "on"):
						Changestate = True
						state.state = "off"
				else:
					if(state.state == "off"):
						Changestate = True
						state.state = "on"
			except ValueError:
				print('type error')

		
		if(val_temp != -1 and not Changestate):
			try:
				val_temp = int(val_temp)
				if(val_temp > setting.humid_threshold):
					if(state.state == "on"):
						Changestate = True
						state.state = "off"
				else:
					if(state.state == "off"):
						Changestate = True
						state.state = "on"
			except ValueError:
				print('type error')

		if(val_humid != -1 ):
			state.humid = val_humid
		if(val_temp != -1 ):
			state.temp = val_temp
		state.save()
		return HttpResponse(state.state)

def index(request):
	settings = Setting.objects.all()
	state = State.objects.all()
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
