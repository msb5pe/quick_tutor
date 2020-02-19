""" V1: Login with Google works """


from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
<<<<<<< Updated upstream
    token = models.CharField(max_length=200, primary_key=True)
    last_signin = models.DateTimeField('Last sign-in')
=======
    
>>>>>>> Stashed changes
