
from rest_framework import serializers

from .models import Plugin, PluginParameter, PluginInstance, StringParameter
from .models import FloatParameter, IntParameter, BoolParameter

class PluginSerializer(serializers.HyperlinkedModelSerializer):
    parameters = serializers.HyperlinkedIdentityField(view_name='pluginparam-list')
    instances = serializers.HyperlinkedIdentityField(view_name='plugininst-list')
    
    class Meta:
        model = Plugin
        fields = ('url', 'id', 'name', 'type', 'parameters', 'instances')


class PluginParameterSerializer(serializers.HyperlinkedModelSerializer):
    plugin = serializers.HyperlinkedRelatedField(view_name='plugin-detail',
                                                 read_only=True)    
    class Meta:
        model = PluginParameter
        fields = ('url', 'name', 'type', 'optional', 'plugin')


class PluginInstanceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    plugin = serializers.HyperlinkedRelatedField(view_name='plugin-detail',
                                                 read_only=True)   
    class Meta:
        model = PluginInstance
        fields = ('url', 'owner', 'plugin')


class StringParameterSerializer(serializers.HyperlinkedModelSerializer):
    plugin_inst = serializers.HyperlinkedRelatedField(view_name='plugininst-detail',
                                                 read_only=True)
    plugin_param = serializers.HyperlinkedRelatedField(view_name='pluginparam-detail',
                                                 read_only=True)
    
    class Meta:
        model = StringParameter
        fields = ('url', 'value', 'plugin_inst', 'plugin_param')


class IntParameterSerializer(serializers.HyperlinkedModelSerializer):
    plugin_inst = serializers.HyperlinkedRelatedField(view_name='plugininst-detail',
                                                 read_only=True)
    plugin_param = serializers.HyperlinkedRelatedField(view_name='pluginparam-detail',
                                                 read_only=True)
    
    class Meta:
        model = IntParameter
        fields = ('url', 'value', 'plugin_inst', 'plugin_param')


class FloatParameterSerializer(serializers.HyperlinkedModelSerializer):
    plugin_inst = serializers.HyperlinkedRelatedField(view_name='plugininst-detail',
                                                 read_only=True)
    plugin_param = serializers.HyperlinkedRelatedField(view_name='pluginparam-detail',
                                                 read_only=True)
    
    class Meta:
        model = FloatParameter
        fields = ('url', 'value', 'plugin_inst', 'plugin_param')


class BoolParameterSerializer(serializers.HyperlinkedModelSerializer):
    plugin_inst = serializers.HyperlinkedRelatedField(view_name='plugininst-detail',
                                                 read_only=True)
    plugin_param = serializers.HyperlinkedRelatedField(view_name='pluginparam-detail',
                                                 read_only=True)
    
    class Meta:
        model = BoolParameter
        fields = ('url', 'value', 'plugin_inst', 'plugin_param')
