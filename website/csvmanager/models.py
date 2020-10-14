from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    university_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.name

class CSVFile(models.Model):
    STATUS = (
        ('Idle', 'Idle'),
        ('Processing', 'Processing'),
        ('Done', 'Done'),
    )
    NETWORK = (
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200, null=True)
    csv = models.FileField(upload_to='%Y/%m/%d/', null=True)
    network = models.CharField(max_length=60, null=True, choices=NETWORK)
    status = models.CharField(max_length=60, null=True, choices=STATUS)

    def __str__(self):
        return self.title
    