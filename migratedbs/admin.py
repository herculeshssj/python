from django.contrib import admin

# Register your models here.
from .models import (
    Person, Employee, Address,
    TipoRequerimento, OrigemRequerimento, StatusRequerimento,
    TipoAutor, TematicaRequerimento, EtapaFluxo, TipoResposta,
    Autor, Requerimento, RequerimentoAutor
)

# Modelos básicos
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'age', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('registry_number', 'person', 'company', 'salary')
    list_filter = ('company', 'sector', 'hired_at')
    search_fields = ('registry_number', 'person__name')
    readonly_fields = ('id', 'created_at', 'updated_at')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'city', 'state', 'person')
    list_filter = ('city', 'state', 'country')
    search_fields = ('address_name', 'city')
    readonly_fields = ('id', 'created_at', 'updated_at')

# Modelos de Configuração RIC
@admin.register(TipoRequerimento)
class TipoRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('sigla_tipo_requerimento', 'nom_tipo_requerimento', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_tipo_requerimento', 'sigla_tipo_requerimento')

@admin.register(OrigemRequerimento)
class OrigemRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('nom_orig_requerimento', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_orig_requerimento',)

@admin.register(StatusRequerimento)
class StatusRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('nom_status_requerimento', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_status_requerimento',)

@admin.register(TipoAutor)
class TipoAutorAdmin(admin.ModelAdmin):
    list_display = ('nom_tipo_autor', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_tipo_autor',)

@admin.register(TematicaRequerimento)
class TematicaRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('nom_tematica_requerimento', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_tematica_requerimento',)

@admin.register(EtapaFluxo)
class EtapaFluxoAdmin(admin.ModelAdmin):
    list_display = ('nom_etapa_fluxo', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_etapa_fluxo',)

@admin.register(TipoResposta)
class TipoRespostaAdmin(admin.ModelAdmin):
    list_display = ('nom_tipo_resposta', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado')
    search_fields = ('nom_tipo_resposta',)

# Modelos principais
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nom_autor', 'tipo_autor', 'partido', 'uf', 'flg_ativo')
    list_filter = ('flg_ativo', 'flg_desativado', 'tipo_autor', 'uf')
    search_fields = ('nom_autor', 'partido')
    readonly_fields = ('dat_atualizacao',)

@admin.register(Requerimento)
class RequerimentoAdmin(admin.ModelAdmin):
    list_display = ('num_requerimento', 'ano_requerimento', 'tipo_requerimento', 'status_requerimento', 'flg_ativo')
    list_filter = ('flg_ativo', 'tipo_requerimento', 'status_requerimento', 'etapa_fluxo')
    search_fields = ('num_requerimento', 'num_oficio')
    readonly_fields = ('dat_atualizacao',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('num_requerimento', 'ano_requerimento', 'tipo_requerimento', 'origem_requerimento')
        }),
        ('Status', {
            'fields': ('status_requerimento', 'etapa_fluxo', 'flg_ativo')
        }),
        ('Datas', {
            'fields': ('data_recebimento_pr', 'prazo_final_resposta_cn', 'data_resposta_demandante', 'dat_atualizacao')
        }),
        ('Descrição', {
            'fields': ('dsc_objeto_requerimento', 'dsc_resumo', 'dsc_observacoes')
        }),
    )

@admin.register(RequerimentoAutor)
class RequerimentoAutorAdmin(admin.ModelAdmin):
    list_display = ('requerimento', 'autor', 'flg_ativo')
    list_filter = ('flg_ativo', 'requerimento__ano_requerimento')
    search_fields = ('requerimento__num_requerimento', 'autor__nom_autor')
    readonly_fields = ('dat_atualizacao',)