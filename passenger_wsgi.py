"""
WSGI config for mdmorris_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import sys, os
#cwd = os.getcwd()
#sys.path.append(cwd)
#sys.path.append(cwd + '/source')
#INTERP = os.path.expanduser("~/virtualenv/sites_mdmorris/3.5/bin/python")

#if sys.executable !- INTERP: os.execl(INTERP, INTERP, *sys.argv)

#sys.path.insert(0, '$HOME/virtualenv/sites_mdmorris/3.5/bin')
#sys.path.insert(0, '$HOME/virutalenv/sites_mdmorris/3.5/lib/python3.5/site-packages/django')
#sys.path.insert(0, '$HOME/virtualenv/sites_mdmorris/3.5/lib/python3.5/site-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mdmorris_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
