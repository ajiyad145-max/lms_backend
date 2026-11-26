from rest_framework import serializers
from module_management.models import Module

class ModuleSerializer(serializers.ModelSerializer):
    
    # module_count=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Module
        fields="__all__"
        read_only_fields=["id","course","order","slug","created_at","updated_at"]

        # def get_module_count(self,obj):
        #     return Module.objects.filter(course=obj).count()