#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebP1.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DEMOPROJECT.settings')
>>>>>>> 5aea44f6da8ae60b66f5b9fa4fd7146c0a02ed9f
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
<<<<<<< HEAD
        ) from exc
=======
        )(exc)
>>>>>>> 5aea44f6da8ae60b66f5b9fa4fd7146c0a02ed9f
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
