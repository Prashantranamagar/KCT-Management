from django.db import models

class Cordinator(models.Model):
	name= models.CharField(max_length=25)
	phone_no = models.CharField(max_length=20)
	email = models.EmailField(null=True)

	def __str__(self):
		return self.name

class Stream(models.Model):
	name= models.CharField(max_length=25)
	cordinator = models.OneToOneField(Cordinator, on_delete=models.RESTRICT)
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=25)
	age = models.IntegerField()
	dob = models.DateField()
	email = models.EmailField()
	reg_no = models.CharField(max_length=20, default='123')
	stream =models.ForeignKey(Stream, on_delete=models.RESTRICT, null=True)
	def __str__(self):
		return self.name


class Club(models.Model):
	name = models.CharField(max_length=20)
	club_email = models.EmailField()
	student = models.ManyToManyField(Student, related_name = 'student_club')
	def __str__(self):
		return self.name