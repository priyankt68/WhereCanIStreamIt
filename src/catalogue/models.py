# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Platform(models.Model):
    """ model for storing which platform the catalogue belongs to. There will be crawlers for each
    of the platform.

    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=2083)

    # platform_logo
    # paid_subscription_called

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    """

    """

    genre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.genre


class Category(models.Model):
    """ whether it's a movie or show

    """

    category = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category


class Catalogue(models.Model):
    """

    """
    title = models.CharField(max_length=555)
    slug = models.CharField(max_length=255)
    # https://support.microsoft.com/en-in/help/208427/maximum-url-length-is-2-083-characters-in-internet-explorer
    url = models.URLField(max_length=2083)
    platform = models.ForeignKey(Platform, related_name='catalogues', on_delete=models.PROTECT)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.title
