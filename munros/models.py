# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Munro(models.Model):
    class Meta:
        db_table = 'munros'

    name = models.TextField()
    gaelic_name = models.TextField(null=True, blank=True)
    heightm = models.IntegerField()
    heightf = models.IntegerField()
    grid_letters = models.CharField(max_length=2, db_column='map')
    altmap = models.CharField(max_length=2, blank=True, null=True)
    grid = models.CharField(max_length=2)
    easting = models.IntegerField()
    northing = models.IntegerField()
    trigpoint = models.BooleanField()

    def __unicode__(self):
        return self.name


class Hiker(models.Model):
    class Meta:
        db_table = 'hikers'

    name = models.TextField()

    def __unicode__(self):
        return self.name


class Walk(models.Model):
    class Meta:
        db_table = 'walks'

    hiker = models.ForeignKey(Hiker)
    munro = models.ForeignKey(Munro)
    time = models.IntegerField()

    def __unicode__(self):
        return "{0} minute walk up {1} by {2}".format(
            self.time, self.munro, self.hiker)
