#import imp
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE","mdmorris_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#sys.path.insert(0, os.path.dirname(__file__))

#wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
#application = wsgi.application
