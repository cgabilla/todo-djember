# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Invitation(models.Model):
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)    
    email = models.EmailField(max_length=70)
 
    class JSONAPIMeta:
        resource_name = "invitations"
