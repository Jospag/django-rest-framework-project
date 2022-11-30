from django.test import TestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username="user01")
token = Token.objects.create(user=user)
print(token.key)
# Create your tests here.
