from audioop import reverse
from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=255)
    ects = models.IntegerField(default=3, null=True, blank=True)

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=255)
    lecture = models.ForeignKey(Lecture)
    date = models.DateField()
    downloads = models.IntegerField(default=0)
    semester = models.ForeignKey('Semester')

    def __str__(self):
        return str(self.lecture) + " - " + str(self.semester)

    def get_absolute_url(self):
        return reverse('exam_detail', args=[self.id])

class Semester(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name