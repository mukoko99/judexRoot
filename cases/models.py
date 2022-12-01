from django.db import models

# Create your models here.
class Case(models.Model):
    defendant = models.ForeignKey(Defendant, on_delete=models.SET_NULL, null=True, blank=True)
    judge = models.ForeignKey(Judge, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField('Case Region', max_length=120, null=True, blank=True)
    jury = models.CharField(max_length=1, default='F', blank=True)
    charge = models.ManyToManyField(Charge)
    sentence = models.IntegerField('Sentence In Years', blank=True, default=0)
    bail = models.IntegerField('Bail Amount In Dollars', blank=True, default=0)
    defendantGroup = models.ForeignKey(DefendantGroup, blank= True, null= True, on_delete=models.SET_NULL)
    judgeGroup = models.ForeignKey(JudgeGroup, blank= True, null= True, on_delete=models.SET_NULL)
    status = models.CharField('Case Status', max_length=16, null = True, blank = True)

    def get_charges(self):
        return ','.join([c.charge for c in self.charge.all()])
    def __str__(self) -> str:
        return str('This case id is {}, defendant(s) are {}, and the judge(s) are {}'.format(self.id, self.defendant, self.judge))

class Charge(models.Model):
    charge = models.CharField('List Of Charges', max_length=1000)
    classes = models.CharField('Crime Class', max_length=64)

    def __str__(self) -> str:
        return str(self.charge)

class Convict(models.Model):
    DIN = models.CharField('Departmental Identification Number', max_length=7)
    firstName = models.CharField('First Name', max_length=32)
    lastName = models.CharField('Last Name', max_length=32)
    DOB = models.DateField()
    Age = models.IntegerField('Age')
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length = 32)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    status = models.CharField(max_length=32)
    facility = models.ForeignKey(Prison, on_delete=models.SET_NULL, null=True, blank=True)
    #charge = models.ManyToManyField(Charge)
=======
=======
>>>>>>> parent of 46ffde1 (Updated for Optimal Functionality)
=======
>>>>>>> parent of 46ffde1 (Updated for Optimal Functionality)

class Defendant(models.Model):
    firstName = models.CharField('Defendant First Name', max_length=32, null=True, blank=True)
    lastName = models.CharField('Defendant Last Name', max_length=32, null=True, blank=True)
    DOB = models.DateField(null=True, blank = True)
    age = models.IntegerField('Defendant Age')
    race = models.CharField('Defendant Race', max_length=260)
    gender = models.CharField('Defendant Gender', max_length=1)
    email = models.EmailField('Defendant Email Address', max_length=64, blank=True)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 46ffde1 (Updated for Optimal Functionality)
=======
>>>>>>> parent of 46ffde1 (Updated for Optimal Functionality)
=======
>>>>>>> parent of 46ffde1 (Updated for Optimal Functionality)

    def __str__(self):
        return str(self.lastName + ' ' + self.firstName)

    #totalConvictions = models.IntegerField('Total Number Of Convictions Defendant Has Had')
    def __str__(self):
        return str(self.lastName + ' ' + self.firstName)

class DefendantGroup(models.Model):
    name = models.CharField('Defendant Group Name', max_length=128)
    members = models.ManyToManyField(Defendant)
    region = models.CharField('Defendant Group Region', max_length=120, null=True, blank=True)
    def __str__(self):
        return ','.join([c.name for c in self.members.all()])

class Judge(models.Model):
    lastName = models.CharField( 'Judge Last Name', max_length=32, null=True, blank=True)
    firstName =  models.CharField('Judge First Name', max_length=260, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    age = models.IntegerField('Judge Age')
    gender = models.CharField('Judge Gender', max_length=1)
    email = models.EmailField('Judge Email Address', max_length=64, blank=True)
    #totalCases = models.IntegerField('Total Number Of Cases Judge Has Presided Over')

    def __str__(self):
        return str(self.lastName + ' ' + self.firstName)

class JudgeGroup(models.Model):
    name = models.CharField('Defendant Group Name', max_length=128)
    members = models.ManyToManyField(Judge)
    region = models.CharField('Judge Group Region', max_length=120, null=True, blank=True)
    def __str__(self):
        return ','.join([c.name for c in self.members.all()])

    # def get_defendants(self):
    #     return ' ,'.join([c.members for c in self.defendantGroup])