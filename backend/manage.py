#!/usr/bin/env python

import os
import sys

from project.settings.base import DEBUG


def main():
    if DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.production")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
