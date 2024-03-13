from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid

class CustomUserManager(UserManager) :
  def _create_user(self, email,password, **extra_fields):
    if not email:
      raise ValueError('You must provide a valid email address')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    # if extra_fields.get('is_staff') is not True:
    #     raise ValueError('Superuser must have is_staff=True.')
    # if extra_fields.get('is_superuser') is not True:
    #     raise ValueError('Superuser must have is_superuser=True.')

    # return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, default='', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
      verbose_name = 'User'
      verbose_name_plural = 'Users'

    def get_short_name(self):
<<<<<<< HEAD

=======
>>>>>>> 66c78c6 (hehe)
      return self.email.split('@')[0]
#Workout model -alyssa
class Workout(models.Model):
    type = models.CharField(max_length=100)
    date_created = models.DateField()
    time = models.IntegerField()
    number_exercises = models.IntegerField()

#exercise model -alyssa
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    reps = models.IntegerField()
    weight = models.IntegerField()
    sets = models.IntegerField()    
    description = models.CharField(max_length=100)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


