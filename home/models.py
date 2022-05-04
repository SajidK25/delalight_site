# Create your models here.
from django.db import models
from django.utils import timezone

class AboutHome(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.text)


class Testimonial(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text='Name')
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    publishedDate = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return str(self.text)


class Team(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text='Name')
    title = models.CharField(max_length=200, help_text='Title')
    create_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='uploads/')
    text = models.TextField()
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return (self.title)


class AboutUs(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    boldtext = models.TextField()
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return (self.text)


class Expertise(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return (self.text)


class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Title')
    name = models.CharField(max_length=200, help_text='Name', blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    createDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return (self.text)

