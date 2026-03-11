"""
Configurações do Chatbot de Licitações
Centralize todas as configurações aqui
"""


class Config:
    """Configurações gerais do chatbot"""
    
    # ========== INFORMAÇÕES DE CONTATO ==========
    HORARIO_FUNCIONAMENTO = "Segunda a Sexta: 7h às 13h"
    TELEFONE = "(67) 3246-8209"
    EMAIL = "licitacao@terenos.ms.gov.br"
    ENDERECO = "Av Dr José Paniago, 119 - Centro, Terenos/MS"
    SITE = "www.terenos.ms.gov.br"
    
    # ========== CONFIGURAÇÕES DO SERVIDOR ==========
    DEBUG = True  # Mude para False em produção
    PORT = 5000   # Porta padrão (Railway usa variável PORT)
    
    # ========== CONFIGURAÇÕES DO BOT ==========
    BOT_NAME = "Assistente de Licitações"
    MUNICIPIO = "Terenos/MS"
    
    # ========== MENSAGENS PERSONALIZADAS ==========
    MENSAGEM_BOAS_VINDAS = "Bem-vindo ao Setor de Licitação"
    MENSAGEM_DESPEDIDA = "Obrigado por utilizar nosso assistente!"
    
    # ========== VALORES DE LICITAÇÃO (Lei 14.133/2021) ==========
    DISPENSA_OBRAS = 100000  # R$ 100.000
    DISPENSA_OUTROS = 50000  # R$ 50.000
    
    # ========== PRAZOS PADRÃO ==========
    PRAZO_IMPUGNACAO = 3  # dias úteis
    PRAZO_RECURSO = 3     # dias úteis
    PRAZO_CONTRATO = 3    # dias consecutivos
    PRAZO_PREGAO = 8      # dias úteis
    PRAZO_CONCORRENCIA = 30  # dias corridos
    
    # ========== MEI/EPP ==========
    MEI_FATURAMENTO_MAX = 81000        # R$ 81 mil/ano
    ME_FATURAMENTO_MAX = 360000        # R$ 360 mil/ano
    EPP_FATURAMENTO_MAX = 4800000      # R$ 4,8 milhões/ano
    EMPATE_FICTO_PERCENTUAL = 10       # 10%
    COTA_RESERVADA_PERCENTUAL = 25     # 25%
    
    @classmethod
    def get_info(cls):
        """Retorna informações do chatbot"""
        return {
            'nome': cls.BOT_NAME,
            'municipio': cls.MUNICIPIO,
            'telefone': cls.TELEFONE,
            'email': cls.EMAIL,
            'site': cls.SITE,
        }


class Messages:
    """Mensagens padrão do sistema"""
    
    NAO_ENTENDIDO = "Desculpe, não entendi sua mensagem."
    ERRO_SISTEMA = "Ocorreu um erro. Por favor, tente novamente."
    FORA_HORARIO = "Estamos fora do horário de atendimento."
    
    @staticmethod
    def contato_formatado(config):
        """Formata informações de contato"""
        return f"""
        📞 Telefone: {config.TELEFONE}
        📧 E-mail: {config.EMAIL}
        📍 Endereço: {config.ENDERECO}
        🌐 Site: {config.SITE}
        """
