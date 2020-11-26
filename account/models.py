from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('custom', 'custom'),
    ('Prefer Not To Say', 'Prefer Not To Say'),
)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    gender = models.CharField(max_length=25, choices=GENDER, default='male')

    def __str__(self):
        return f'Profile for user {self.user.username}'
