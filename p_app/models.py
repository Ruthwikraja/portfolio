import datetime
import errno
import os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    role = models.CharField(max_length=50)
    role_description = models.TextField(blank=False)
    birthday = models.DateField(blank=True, null=True)
    degree = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    description = models.TextField(blank=False,null=True)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role
    def get_age(self):
        age = datetime.date.today()-self.birthday
        return int((age).days/365.25)

class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    proficiency = models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])


    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    name = models.CharField(max_length=50, null=True)
    link = models.URLField(max_length=200)
    category = models.CharField(max_length=20,null=True, choices=[
        ('app', 'App'),
        ('web', 'Web')
    ])


    def __str__(self):
        return f'Portfolio {self.name}'

class ImageFile(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)  # New field
    def _get_upload_path(self, filename):
        return os.path.join('portfolio', self.portfolio.name, filename)

    image = models.ImageField(upload_to=_get_upload_path)

#Interests
class Interests(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20,null=True, choices=[
        ('technical', 'Technical'),
        ('general', 'General')
    ])

    class Meta:
        verbose_name_plural = 'Interests'

    def __str__(self):
        return self.name
    
#Resume
class Summary(models.Model):
    name = models.CharField(max_length=50, null=True)
    summary = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    degree = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return self.degree
    
class Experience(models.Model):
    position = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20, blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    job_role = models.CharField(max_length=250, blank=True)
    responsibilities = models.TextField(blank=True)
    technical_skills = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
    
    def __str__(self):
        return self.company_name
    def res(self):
        return self.responsibilities.splitlines()
    def tech(self):
        return self.technical_skills.splitlines()

class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=155)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.email
