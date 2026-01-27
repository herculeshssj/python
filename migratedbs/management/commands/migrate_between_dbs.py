from django.core.management.base import BaseCommand
from django.utils import timezone

from migratedbs.models import Person

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
        print('Lendo dados da tabela Person no banco MariaDB:')
        print('**********************************************')
        persons = Person.using_mariadb().all()
        for person in persons:
            print(f'{person.id} - {person.name} - {person.registry_number} - {person.birth_date} - {person.salary}')


        # nome = options['nome']
        # vezes = options['vezes']
        # now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        # for i in range(vezes):
        #     self.stdout.write(f'[{now}] Olá, {nome}! ({i+1}/{vezes})')
        # Exemplo de erro:
        # self.stderr.write('Algo deu errado')
        # Para retornar código de saída:
        # return 0
