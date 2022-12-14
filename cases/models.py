from django.db import models

from location_field.models.plain import PlainLocationField

# Create your models here.
class Charge(models.Model):
    charge = models.CharField('List Of Charges', max_length=1000)
    classes = models.CharField('Crime Class', max_length=64)

    def __str__(self) -> str:
        return str(self.charge+ ', '+self.classes)

class Defendant(models.Model):
    firstName = models.CharField('Defendant First Name', max_length=32, null=True, blank=True)
    lastName = models.CharField('Defendant Last Name', max_length=32, null=True, blank=True)
    middleName = models.CharField('Middle Initial', max_length=32, default= ' ', blank=True)
    DOB = models.DateField(null=True, blank = True)
    age = models.IntegerField('Defendant Age', blank=True, null=True)
    race = models.CharField('Defendant Race', max_length=260)
    #gender = models.CharField('Defendant Gender', max_length=1)
    email = models.EmailField('Defendant Email Address', max_length=64, blank=True)
    #totalConvictions = models.IntegerField('Total Number Of Convictions Defendant Has Had')
    
    def __str__(self):
        return str(self.lastName + ', ' + self.firstName + ' ' + self.middleName + ', ' + str(self.DOB))
    
class DefendantGroup(models.Model):
    name = models.CharField('Defendant Group Name', max_length=128)
    members = models.ManyToManyField(Defendant)
    county = models.CharField('Defendant Group County', max_length=120, null=True, blank=True)
    def __str__(self):
        return ','.join([c.name for c in self.members.all()])

class Judge(models.Model):
    lastName = models.CharField( 'Judge Last Name', max_length=32, null=True, blank=True)
    firstName =  models.CharField('Judge First Name', max_length=260, null=True, blank=True)
    middleName = models.CharField('Middle Name', max_length=32, default=' ')
    DOB = models.DateField(null=True, blank=True)
    age = models.IntegerField('Judge Age')
    gender = models.CharField('Judge Gender', max_length=1)
    email = models.EmailField('Judge Email Address', max_length=64, blank=True)
    #totalCases = models.IntegerField('Total Number Of Cases Judge Has Presided Over')

    def __str__(self):
        return str(self.lastName + ', ' + self.firstName + ' ' + self.middleName)

class JudgeGroup(models.Model):
    name = models.CharField('Defendant Group Name', max_length=128)
    members = models.ManyToManyField(Judge)
    county = models.CharField('Judge Group County', max_length=120, null=True, blank=True)
    def __str__(self):
        return ','.join([c.name for c in self.members.all()])

class Case(models.Model):
    defendant = models.ForeignKey(Defendant, on_delete=models.SET_NULL, null=True, blank=True)
    judge = models.ForeignKey(Judge, on_delete=models.SET_NULL, null=True, blank=True)
    county = models.CharField('Case County', max_length=120, null=True, blank=True)
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

class Prison(models.Model):
    name = models.CharField('Prison Name', max_length=32)
    county = models.CharField(max_length=64)
    location = PlainLocationField(based_fields= ('city'), zoom=7)
    security = models.CharField("Security", max_length=50, default='N.A')

    def __str__(self):
        return str(self.name + ', ' + self.county)

class Conviction(models.Model):
    DIN = models.CharField('Departmental Identification Number', max_length=7)
    defendant = models.ForeignKey(Defendant, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    facility = models.ForeignKey(Prison, on_delete=models.SET_NULL, null=True, blank=True)
    charges = models.ManyToManyField(Charge)
    incarcerationEnd = models.DateField('Date of Imprisonment', blank=True, null=True)
    sentenceStart = models.DateField("Date Sentencing Starts", blank=True, null=True)
    sentenceEnd = models.DateField("Release Date", blank=True, null = True)
    def __str__(self):
        return str(self.defendant)

# def get_defendants(self):
# return ' ,'.join([c.members for c in self.defendantGroup])
