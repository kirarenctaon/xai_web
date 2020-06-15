from django.db import models

#NEWS&INFO##########################################################################################################################
class Notice(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentk = models.TextField()
    image = models.CharField(max_length=100)

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    link = models.TextField()
    image = models.CharField(max_length=100)

#RESEARCH##########################################################################################################################
class AutoNews(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    content = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    prediction = models.TextField()
    image_raw = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_predict = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_first = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_second = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_third = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    report_pdf = models.FileField(upload_to='AutomaticNews/%Y/%m/%d')

class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    journal = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)

class Patent(models.Model):
    title = models.CharField(max_length=100)
    inventor = models.CharField(max_length=45)
    nation = models.CharField(max_length=45)
    date = models.DateField()
    number = models.TextField()

class RelatedProject(models.Model):
    title = models.CharField(max_length=200, null=True)
    Institutions = models.CharField(max_length=45)
    Authors = models.CharField(max_length=200, null=True)
    Publication_title = models.CharField(max_length=200, null=True)
    Publication_link = models.CharField(max_length=200, null=True)
    Related_link = models.CharField(max_length=200, null=True)
    Sourcecode =models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='RelatedProject/')

class CompanyList(models.Model):
    company_kor = models.TextField()
    company_eng = models.TextField()
