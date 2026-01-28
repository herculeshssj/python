from django.core.management.base import BaseCommand
from django.utils import timezone
from time import sleep, time
from migratedbs.models import Person, Employee, Address, PersonMySQL

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
        persons = PersonMySQL.using_mariadb().all()
        for person in persons:
            print(f'{person.id} - {person.name} - {person.registry_number} - {person.birth_date} - {person.salary}')

            # Criar ou atualizar Person
            person_obj, created = Person.objects.using('postgres').update_or_create(
                id=person.id,
                defaults={
                    'name': person.name,
                    'birth_date': person.birth_date,
                }
            )
            
            # Criar ou atualizar Employee
            employee_obj, created = Employee.objects.using('postgres').update_or_create(
                person=person_obj,
                defaults={
                    'salary': person.salary,
                    'company': person.company,
                    'sector': person.sector,
                    'registry_number': person.registry_number,
                }
            )
            
            # Criar ou atualizar Address (se houver campos de endereço)
            # Ajuste conforme seus campos reais
            address_obj, created = Address.objects.using('postgres').update_or_create(
                person=person_obj,
                defaults={
                    'address_name': person.address,
                    'address_number': person.address_number,
                    'district': person.district,
                    'city': person.city,
                    'state': person.state,
                    'country': person.country,
                    'post_code': person.post_code,
                }
            )

            sleep(5)  # Simula algum tempo de processamento
            print('Registro gravado na base PostgreSQL')
        
        print('Migração concluída com sucesso!')


