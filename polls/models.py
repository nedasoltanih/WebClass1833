from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField("date published")
    number = models.IntegerField(default=0)
    lang = models.CharField(max_length=2,default="en",choices=[("en", "English"),("fa", "Farsi"),("ar", "Arabic")])
    qslug = models.SlugField(max_length=200,null=True,blank=True,unique=True,editable=False)

    def __str__(self):
        return self.question_text

    def is_first_question(self):
        return self.number == 1


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    part_email = models.EmailField(default="", help_text="Enter your email", editable=False)

