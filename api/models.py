from django.db import models

# Students
class Student(models.Model):
    name = models.CharField(max_length=24, blank=False, null=True, default=None)
    email = models.EmailField(max_length=24, blank=False, null=True, default=None)
    group = models.CharField(max_length=24, blank=True, null=True, default=None)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"