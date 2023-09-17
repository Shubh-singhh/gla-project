from django.db import models

class Feedback(models.Model):
    title = models.CharField(max_length=30)
    # email = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.title
