from rest_framework import serializers

class Student(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


    def create(self , validate_data):
        return Student.objects.create(**validate_data)