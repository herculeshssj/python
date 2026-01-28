from django.core.management.base import BaseCommand
from migratedbs.services.migrate_dbs import MigrateDBs

class Command(BaseCommand):
    help = 'Migra conteúdo entre bancos de dados diferentes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nome',
            type=str,
            help='Nome a ser impresso',
            default='Mundo'
        )
        parser.add_argument(
            '-n', '--vezes',
            type=int,
            help='Número de vezes',
            default=1
        )

    def handle(self, *args, **options):
        migrate_dbs = MigrateDBs()
        migrate_dbs.migrate()