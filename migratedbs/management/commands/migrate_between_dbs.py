from django.core.management.base import BaseCommand
from migratedbs.services.migrate_dbs import MigrateDBs
from migratedbs.services.migrate_ric import MigrateRIC

class Command(BaseCommand):
    help = 'Migra conteúdo entre bancos de dados diferentes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--example',
            action='store_true',
            help='Executa migração de exemplo'
        )
        parser.add_argument(
            '--ric',
            action='store_true',
            help='Executa migração dos dados do RIC'
        )

    def handle(self, *args, **options):
        try:
            migrate_dbs = MigrateDBs()
            migrate_ric = MigrateRIC()
            if options['example']:
                self.stdout.write(self.style.SUCCESS('Executando migração de exemplo...'))
                migrate_dbs.migrate()
            elif options['ric']:
                self.stdout.write(self.style.SUCCESS('Executando migração dos dados do RIC...'))
                migrate_ric.migrate()
            else:
                self.stdout.write(self.style.WARNING('Use --example ou --ric'))
                
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Erro durante a migração: {e}'))
            return