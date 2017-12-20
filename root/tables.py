import django_tables2 as tables
from .models import Setting, State
import itertools

class SettingTable(tables.Table):
    class Meta:
        model = Setting
        fields = ('name','min_humid','max_humid','min_temp','max_temp')
        template = 'django_tables2/bootstrap.html'

class StateTable(tables.Table):
    class Meta:
        model = State
        fields = ('state','humid','temp','setting','manual','degree')
        template = 'django_tables2/bootstrap.html'
