from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Gismu(models.Model):
    valsi = models.CharField(max_length=5)     # the gismu itself
    smuni = models.TextField()                 # old definition

    def __unicode__(self):
        return self.valsi

class Proposal(models.Model):
    gismu  = models.ForeignKey(Gismu) # one gismu has many proposals
    prenu  = models.ForeignKey(User)  # who introduced this proposal
    klesi  = models.IntegerField(     # type of proposal
                                 choices = ((1,  'No action'),
                                            (2, 'Delete gismu'),
                                            (3, 'Alter place structure'),
                                            (4, 'Create new gismu')),
                                 default = 1)
    mapti  = models.IntegerField(     # past usage compatibility rating
                              choices = ((1, 'Unknown'),
                                         (2, 'Does not break past usage'),
                                         (3, 'Breaks past usage, but unlikely to cause confusion'),
                                         (4, 'Breaks past usage, and likely to cause confusion')),
                              default = 1)
    cmene  = models.TextField()       # title of proposal
    velcki = models.TextField()       # introduction / opening arguments

    def __unicode__(self):
        return '(%s) %s' % (self.gismu, self.cmene)


admin.site.register(Gismu)
admin.site.register(Proposal)

