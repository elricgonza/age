#!/usr/bin/python3.8

import sys
import logging
import platform

print('------------------------prev-activate---------------------------------------------<<')
print ('location-virt-env-python: ' + sys.prefix)
print ('vers-python: ' + platform.python_version())
print (sys.path)
print('--------------------------------------------------------------------->>')

activate_this = '/var/www/flasks/age/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flasks/age/")

print('--------------------------post-activate------------------------------<<')
print ('location-virt-env-python: ' + sys.prefix)
print ('vers-python: ' + platform.python_version())
print(sys.path)
print('--------------------------------------------------------------------->>')


from age import app as application

print('---ok---')
#application.secret_key = 'Add your secret key'
