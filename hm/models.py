from django.db import models

# Create your models here.
class instituicao_parceira(models.Model):
	
	nome = models.CharField(max_length=250)
	CNPJ = models.IntegerField(max_length=11)
	cidade = models.CharField(max_length=80)
	administradores_locais = models.CharFild(max_length=200)
	status = models.CharField(max_length = 80)
	 

class evento(models.Model):
	nome = models.CharField(max_length=200)
	data_inicio = models.DateFild()
	data_fim =	model.DateField()
	descricao = models.Charfield(max_length=300)
	instituicao_parceira = models.ForeignKey("instituicao_parceira") 
	#permitir_registros = models.Charfield(max_length = 250)
	instituicao_parceira = models.CharField(max_length=250)
	#insclritos
	#credenciados
	
class atividades(models.Model):
	Nome = models.CharField(max_length =250)
	descricao = models.CharField(max_length=300)
	evento = models.ForeignKey("evento") 
	
	duracao = models.TimeField(_(u"conversation time"))
	Inf_certificado = models.CharField(max_length = 300)
	inf_submissoes = models.ChaField(max_length = 300)
			...terminar...

class sessoes(models.Model)
	data=models.DateField()
	hora =models.TimeField(_(u"conversation time"), blank =True)
	hora_fim =models.TimeField(_(u"conversation time"), blank =True)
	atividades = models.OneToOneField("atividades")

class submissoes(models.Model)
	Participante = models.CharField(max_length = 250)
	Atividades = models.CharField(max_length = 300)
	linha = models. ChaField(max_length)
class inscritos(models.Model):
	"""pessoas inscritas

	"""
	
	
		