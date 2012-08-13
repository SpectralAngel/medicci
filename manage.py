#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    
    _root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.insert(0, _root_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medicci.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
