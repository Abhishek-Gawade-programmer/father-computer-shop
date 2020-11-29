#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
'''
virtualenv ../shop_website_env/

source ../shop_website_env/Scripts/activate
cd shop_website_root
winpty python manage.py runserver
winpty python manage.py createsuperuser
winpty python shop_website_root/manage.py runserver
deactivate
'''



if __name__ == '__main__':
    main()
