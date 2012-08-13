#!/home1/grupohus/.local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicci.settings")
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
