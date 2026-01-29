from django.db import models, connections
from datetime import date

class PersonMySQL(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.PositiveSmallIntegerField()
    registry_number = models.CharField(max_length=20, unique=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    company = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    address_number = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=60, default='Brazil')
    post_code = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Person'
        managed = False
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.registry_number})'

    def computed_age(self):
        if not self.birth_date:
            return None
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    @classmethod
    def using_mariadb(cls):
        """
        Helper to obtain a QuerySet that will read from the 'mariadb' DB connection.
        Uso: Person.using_mariadb().filter(...)
        """
        return cls.objects.using('mariadb')

import uuid
from datetime import date
from django.db import models

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age_persisted = models.PositiveSmallIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "person"
        indexes = [
            models.Index(fields=["name"], name="idx_person_name"),
        ]

    def __str__(self):
        return self.name

    @property
    def age(self) -> int | None:
        if not self.birth_date:
            return None
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.OneToOneField(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employee",
    )
    registry_number = models.CharField(max_length=100, unique=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    company = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    hired_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee"
        indexes = [
            models.Index(fields=["registry_number"], name="idx_employee_registry"),
        ]

    def __str__(self):
        return f"{self.registry_number} - {self.person.name if self.person else 'N/A'}"


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    address_name = models.CharField(max_length=255)
    address_number = models.CharField(max_length=50)
    district = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Brazil")
    post_code = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "address"
        indexes = [
            models.Index(fields=["person"], name="idx_address_person"),
        ]

    def __str__(self):
        return f"{self.address_name}, {self.address_number} - {self.city or ''}"

# ----------------------------
# Tabelas do RIC
# ----------------------------

class TipoRequerimento(models.Model):
    nom_tipo_requerimento = models.CharField(max_length=50)
    sigla_tipo_requerimento = models.CharField(max_length=3)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()  # use auto_now=True se quiser atualizar automaticamente
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_tipo_requerimento'
        verbose_name = 'Tipo de Requerimento'
        verbose_name_plural = 'Tipos de Requerimento'

    def __str__(self):
        return f'{self.sigla_tipo_requerimento} - {self.nom_tipo_requerimento}'


class OrigemRequerimento(models.Model):
    nom_orig_requerimento = models.CharField(db_column='nom_origem_requerimento', max_length=50)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_origem_requerimento'
        verbose_name = 'Origem do Requerimento'
        verbose_name_plural = 'Origens do Requerimento'

    def __str__(self):
        return self.nom_orig_requerimento


class StatusRequerimento(models.Model):
    nom_status_requerimento = models.CharField(max_length=50)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_status_requerimento'
        verbose_name = 'Status do Requerimento'
        verbose_name_plural = 'Status dos Requerimentos'

    def __str__(self):
        return self.nom_status_requerimento


class TipoAutor(models.Model):
    nom_tipo_autor = models.CharField(max_length=50)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_tipo_autor'
        verbose_name = 'Tipo de Autor'
        verbose_name_plural = 'Tipos de Autor'

    def __str__(self):
        return self.nom_tipo_autor


class TematicaRequerimento(models.Model):
    nom_tematica_requerimento = models.CharField(max_length=50)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_tematica_requerimento'
        verbose_name = 'Temática do Requerimento'
        verbose_name_plural = 'Temáticas do Requerimento'

    def __str__(self):
        return self.nom_tematica_requerimento


class EtapaFluxo(models.Model):
    nom_etapa_fluxo = models.CharField(max_length=30)
    nom_alias = models.CharField(max_length=30)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_etapa_fluxo'
        verbose_name = 'Etapa do Fluxo'
        verbose_name_plural = 'Etapas do Fluxo'

    def __str__(self):
        return self.nom_etapa_fluxo


class TipoResposta(models.Model):
    nom_tipo_resposta = models.CharField(max_length=50)
    nom_alias = models.CharField(max_length=50)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_tipo_resposta'
        verbose_name = 'Tipo de Resposta'
        verbose_name_plural = 'Tipos de Resposta'

    def __str__(self):
        return self.nom_tipo_resposta


# ----------------------------
# Autor e relacionamentos
# ----------------------------

class Autor(models.Model):
    tipo_autor = models.ForeignKey(
        TipoAutor,
        on_delete=models.PROTECT,
        db_column='tipo_autor_id',
        related_name='autores'
    )
    nom_autor = models.CharField(max_length=200)
    nom_alias = models.CharField(max_length=200)
    partido = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    flg_desativado = models.BooleanField(default=False)
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nom_autor


# ----------------------------
# Requerimento
# ----------------------------

class Requerimento(models.Model):
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    num_requerimento = models.IntegerField()
    ano_requerimento = models.IntegerField()

    tipo_requerimento = models.ForeignKey(
        TipoRequerimento, on_delete=models.PROTECT, db_column='tipo_requerimento_id', related_name='requerimentos'
    )
    origem_requerimento = models.ForeignKey(
        OrigemRequerimento, on_delete=models.PROTECT, db_column='origem_requerimento_id', related_name='requerimentos'
    )
    status_requerimento = models.ForeignKey(
        StatusRequerimento, on_delete=models.PROTECT, db_column='status_requerimento_id', related_name='requerimentos'
    )

    num_oficio = models.TextField()
    data_recebimento_pr = models.DateField()
    prazo_final_resposta_cn = models.DateField()

    processo_sei_envio_cc = models.CharField(max_length=35)
    processo_sei_resposta_cc = models.CharField(max_length=35)

    dsc_objeto_requerimento = models.TextField()

    tematica = models.ForeignKey(
        TematicaRequerimento, on_delete=models.PROTECT, db_column='tematica_id', related_name='requerimentos'
    )

    # Comentado como JSON no script: usar JSONField
    unidades_consultadas = models.JSONField()

    status_congresso = models.TextField()
    ementa = models.TextField()
    andamento_cc = models.TextField()

    etapa_fluxo = models.ForeignKey(
        EtapaFluxo, on_delete=models.PROTECT, db_column='etapa_fluxo_id', related_name='requerimentos',
        null=True, blank=True
    )

    prazo_etapa = models.TextField(null=True, blank=True)
    dsc_resumo = models.TextField(null=True, blank=True)
    dsc_observacoes = models.TextField(null=True, blank=True)

    data_resposta_demandante = models.DateField()
    tipo_resposta = models.ForeignKey(
        TipoResposta, on_delete=models.PROTECT, db_column='tipo_resposta_id', related_name='requerimentos'
    )

    link_congresso = models.TextField(null=True, blank=True)
    link_inteiro_teor = models.TextField(null=True, blank=True)

    # ManyToMany através da tabela de junção com campos extras
    autores = models.ManyToManyField('Autor', through='RequerimentoAutor', related_name='requerimentos')

    class Meta:
        db_table = 'ric_requerimento'
        verbose_name = 'Requerimento'
        verbose_name_plural = 'Requerimentos'
        indexes = [
            models.Index(fields=['ano_requerimento', 'num_requerimento']),
        ]

    def __str__(self):
        return f'{self.num_requerimento}/{self.ano_requerimento}'


class RequerimentoAutor(models.Model):
    requerimento = models.ForeignKey(
        Requerimento, on_delete=models.CASCADE, db_column='requerimento_id', related_name='autores_vinculos'
    )
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, db_column='autor_id', related_name='requerimentos_vinculos'
    )
    dat_atualizacao = models.DateTimeField()
    flg_ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'ric_requerimento_autor'
        verbose_name = 'Autor do Requerimento'
        verbose_name_plural = 'Autores do Requerimento'

    def __str__(self):
        return f'{self.requerimento} - {self.autor}'