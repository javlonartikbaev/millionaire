from django.db import models


class Variants(models.Model):
    variants = models.JSONField(default=list)

    def __str__(self):
        return ', '.join(self.variants)


class Question(models.Model):
    LEVEL_CHOICES = [("1", "One"), ("2", "Two"),
                     ("3", "Three"), ("4", "Four"),
                     ("5", "Five"), ("6", "Six"),
                     ("7", "Seven"), ("8", "Eight"),
                     ("9", "Nine"), ("10", "Ten"), ]
    question_name = models.CharField(max_length=255)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, )
    variants_id = models.ForeignKey(Variants, on_delete=models.CASCADE)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"{self.question_name} - Variants: {self.variants_id}"
