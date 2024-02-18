import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for Database...')
        db_connection = False

        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 3 seconds...')
                time.sleep(3)

        self.stdout.write('Database is available!')
