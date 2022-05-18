# -*- coding: utf-8 -*-
import sys
import os

from django.db.utils import ProgrammingError
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-u','--user',
            action='store',
            dest='user',
            default=False,
            help="UserName"
        )
        parser.add_argument(
            '-p','--pass',
            action='store',
            dest='pass',
            default=False,
            help="Password"
        )
       

    def handle(self, *args, **options):
        
        
        if not options.get('user'):
            self.stderr.write("username flag required '--user'")
            return
        if not options.get('pass'):
            self.stderr.write("pass flag required '--pass'")
            return
        username = options.get('user')
        password = options.get('pass')
        if User.objects.filter(username=username).count() > 0:
            self.stdout.write('User already exists.')
            sys.exit()

        try:
            User.objects.create_user(
                username,
                username+'@gmsl.gov.ye',
                password)
        except ProgrammingError:  # Signals fail when `kc` database
            pass                  # doesn't exist yet.
        except Exception as e:
            self.stdout.write('User could not be created.\n'
                              'Error: {}'.format(str(e)))

        if User.objects.filter(username=username).count() > 0:
            self.stdout.write('Superuser successfully created.')

