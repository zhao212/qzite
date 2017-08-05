from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class msg(models.Model):
    sender = models.ForeignKey('auth.User')
    receiver = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    sent_time = models.DateTimeField(default = timezone.now)
    is_read = models.BooleanField(default = False)

    def hasread(self):
        self.is_read = True
        self.save()

    def sendmsg(self):
        self.sent_time = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("mymsg:msginbox")

    def __str__(self):
        return self.title
