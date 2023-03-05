from django.db import models


class Units(models.Model):
    name = models.CharField(max_length=50)


class Tasks(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)  # тема
    task = models.TextField()  # условие


class Tests(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)  # тема
    question = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    correct = models.TextField()
    radio = models.TextField(default="r1")


