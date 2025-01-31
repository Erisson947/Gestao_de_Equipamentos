from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') #1
app = Celery('core') #2
app.config_from_object('django.conf:settings', namespace='CELERY') #3
app.autodiscover_tasks() #4