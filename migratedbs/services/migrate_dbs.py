import logging
from time import sleep
from migratedbs.models import Address, Employee, Employee, Person, Person, PersonMySQL

log = logging.getLogger(__name__)

class MigrateDBs:

    def _calculate_age(self, person: PersonMySQL):
        return person.computed_age()


    def _handle_person_data(self, person: PersonMySQL):
        return {
            'name': person.name,
            'birth_date': person.birth_date,
            'age_persisted': self._calculate_age(person),
        }   


    def _handle_employee_data(self, person: PersonMySQL):
        return {
            'salary': person.salary,
            'company': person.company,
            'sector': person.sector,
            'registry_number': person.registry_number,
        }


    def _handle_address_data(self, person: PersonMySQL):
        return {
            'address_name': person.address,
            'address_number': person.address_number,
            'district': person.district,
            'city': person.city,
            'state': person.state,
            'country': person.country,
            'post_code': person.post_code,
        }


    def migrate(self):
        log.info('Lendo dados da tabela Person no banco MariaDB:')
        log.info('**********************************************')
        
        persons = PersonMySQL.using_mariadb().all()
        for person in persons:
            log.info(f'{person.id} - {person.name} - {person.registry_number} - {person.birth_date} - {person.salary}')
            # Criar ou atualizar Person
            person_obj, created = Person.objects.using('postgres').update_or_create(
                id=person.id,
                defaults=self._handle_person_data(person)
            )
            
            # Criar ou atualizar Employee
            employee_obj, created = Employee.objects.using('postgres').update_or_create(
                person=person_obj,
                defaults=self._handle_employee_data(person)
            )
            
            # Criar ou atualizar Address (se houver campos de endereço)
            # Ajuste conforme seus campos reais
            address_obj, created = Address.objects.using('postgres').update_or_create(
                person=person_obj,
                defaults=self._handle_address_data(person)
            )

            sleep(1)  # Simula algum tempo de processamento
            log.info('Registro gravado na base PostgreSQL')
        
        log.info('Migração concluída com sucesso!')