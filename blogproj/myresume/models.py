from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class res_basic(models.Model):
    user = models.OneToOneField('auth.User')
    first_name = models.CharField(max_length=150, verbose_name="First name")
    last_name = models.CharField(max_length=150, verbose_name="Last name")
    birthday = models.DateField(default = timezone.now)
    email = models.CharField(max_length=100,blank=True, null=True, verbose_name="email")
    phone = models.CharField(max_length=100,blank=True, null=True, verbose_name="phone")
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="address")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="city")
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name="state")
    zipcode = models.IntegerField(max_length=10, blank=True, null=True, verbose_name="zipcode")
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name="title")

    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.full_name()

class res_education(models.Model):
    user = models.ForeignKey('auth.User')
    education_name = models.CharField(max_length=150, verbose_name="school")
    degree = models.CharField(max_length=150,verbose_name="degree")
    major = models.CharField(max_length=150,blank=True, verbose_name="Major")
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.education_name

class res_project(models.Model):
    user = models.ForeignKey('auth.User')
    project_name = models.CharField(max_length=150, verbose_name="project name")

    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    description = models.TextField(verbose_name="project description")

    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.project_name

class res_work(models.Model):
    user = models.ForeignKey('auth.User')
    work_title = models.CharField(max_length=150, verbose_name="title")
    company_name = models.CharField(max_length=150, verbose_name="company")
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    description = models.TextField(verbose_name="project description")

    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.work_title

class res_skill(models.Model):
    user = models.ForeignKey('auth.User')
    skill_name = models.CharField(max_length=100, verbose_name="skill")
    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.skill_name

class res_award(models.Model):
    user = models.ForeignKey('auth.User')
    award_name = models.CharField(max_length=100, verbose_name="award")
    get_year = models.DateField(default = timezone.now, verbose_name="year")
    def get_absolute_url(self):
        return reverse("myresume:resumepage")

    def __str__(self):
        return self.award_name
