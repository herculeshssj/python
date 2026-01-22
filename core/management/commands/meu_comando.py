from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Exemplo: imprime mensagem com timestamp'

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
        nome = options['nome']
        vezes = options['vezes']
        now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(vezes):
            self.stdout.write(f'[{now}] Olá, {nome}! ({i+1}/{vezes})')
        # Exemplo de erro:
        # self.stderr.write('Algo deu errado')
        # Para retornar código de saída:
        # return 0
