from rest_framework import serializers

from toys.models import Toy


class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Toy.objects.create(**validated_data)

    def update(self, instance, validate_date):
        instance.name = validate_date.get('name', instance.name)
        instance.description = validate_date.get('description', instance.description)
        instance.release_date = validate_date.get('release_date', instance.release_date)
        instance.toy_category = validate_date.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validate_date.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance