#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Set the default Django settings module for the 'library_management' project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings')
    
    try:
        # Import the execute_from_command_line function from Django's core management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError if Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command line with the provided arguments
    execute_from_command_line(sys.argv)

# Entry point to run the administrative tasks when the script is executed
if __name__ == '__main__':
    main()
