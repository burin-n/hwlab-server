import django_tables2 as tables
from .models import Setting, State
import itertools

class SettingTable(tables.Table):
    class Meta:
        model = Setting
        fields = ('name','humid_threshold','temp_threshold')
        template = 'django_tables2/bootstrap.html'

class StateTable(tables.Table):
    class Meta:
        model = State
        fields = ('state','humid','temp','manual','using_setting')
        template = 'django_tables2/bootstrap.html'
