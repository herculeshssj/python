import logging
from time import sleep, perf_counter
from migratedbs.models import Address, Employee, Employee, Person, Person, PersonMySQL, RicProcessados

log = logging.getLogger(__name__)

class MigrateRIC:

    def migrate(self):
        # Aqui entra a lógica específica para migrar os dados do RIC
        log.info('Iniciando migração dos dados do RIC...')
        start = perf_counter()

        ricList = RicProcessados.using_ric().all()
        for ric in ricList:
            log.info(f'Processando RIC: {ric.num_ric}/{ric.ano_ric} - Origem: {ric.origem}')
            
            # Aqui entra o processamento dos dados


            log.info(f'RIC {ric.num_ric}/{ric.ano_ric} origem ({ric.origem}) processado com sucesso.')

        elapsed = perf_counter() - start

        h, rem = divmod(elapsed, 3600)
        m, s = divmod(rem, 60)        

        log.info(f'Tempo total de migração dos dados do RIC: {elapsed:.2f} segundos / {int(h)}h {int(m)}m {s:.2f}s')
        log.info('Migração concluída com sucesso!')