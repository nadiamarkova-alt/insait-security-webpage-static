from django.db import models


class ResearchTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='research_topics/', blank=True, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    class Category(models.TextChoices):
        FACULTY = 'faculty', 'Faculty'
        PHD = 'phd', 'PhD Candidates'
        VISITORS = 'visitors', 'Visitors & Collaborators'

    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    topic = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.PHD,
    )
    photo = models.ImageField(upload_to='members/')
    personal_website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=500)
    year = models.IntegerField()
    conference = models.TextField(blank=True, null=True)
    paper_link = models.URLField()
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
