"""
WSGI config for studynet project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

python_path = os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        '.'
        )

apps_path = os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        './apps'
        )

lib_path = os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        './lib'
        )

sys.path.insert(0, python_path)
sys.path.insert(0, apps_path)
sys.path.insert(0, lib_path)

# Settings switching
if not os.environ.has_key('HEROKU'): os.environ['HEROKU'] = 'false'
if not os.environ.has_key('PLSMLAB'): os.environ['PLSMLAB'] = 'false'
if os.environ['HEROKU'] == "true":
    if os.environ['HEROKU_VERSION'] == "staging":
        settings_location = "studynet.configs.heroku_staging.settings"
    elif os.environ['HEROKU_VERSION'] == "production":
        settings_location = "studynet.configs.heroku.settings"
elif os.environ['PLSMLAB'] == 'true':
    settings_location = "studynet.configs.plsmlab.settings"
else:
    settings_location = "studynet.configs.common.settings"
print "Using setting: %s" % settings_location
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_location)

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
