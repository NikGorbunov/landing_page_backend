from rest_framework import serializers

from contacts.models import Contact, Project


class OngoingProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'image', 'size', 'project_type')


class PreviousProjectSerializer(serializers.ModelSerializer):
    date_of_completion = serializers.DateTimeField(required=True)

    class Meta:
        model = Project
        fields = ('project_name', 'image', 'size', 'project_type', 'date_of_completion')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'number', 'message')
