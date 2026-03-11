"""
Chatbot Base - Lógica compartilhada
Consultor de Licitações - Versão Completa
Sem duplicação de código!
"""



class ChatbotLicitacao:
    """Classe base do chatbot - usada por todas as versões"""
    
    def __init__(self):
        # ========== CONFIGURAÇÕES (EDITE AQUI!) ==========
        self.horario_funcionamento = "Segunda a Sexta: 7h às 13h"
        self.telefone = "67 – 3246 - 8209"
        self.email = "licitacao@terenos.ms.gov.br"
        self.endereco = "Av. Dr. José Paniago, 119 Centro"
        self.site = "www.terenos.ms.gov.br"
    
    def processar_mensagem(self, mensagem):
        """Processa a mensagem do usuário"""
        mensagem = mensagem.lower().strip()
        
        # Saudação e Menu
        if any(palavra in mensagem for palavra in ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite', 'menu', 'iniciar', 'voltar']):
            return self.saudacao()
        
        # Opções numéricas do menu
        elif mensagem == '1':
            return self.o_que_e_licitacao()
        elif mensagem == '2':
            return self.tipos_licitacao()
        elif mensagem == '3':
            return self.como_participar()
        elif mensagem == '4':
            return self.documentos()
        elif mensagem == '5':
            return self.prazos()
        elif mensagem == '6':
            return self.recursos()
        elif mensagem == '7':
            return self.onde_consultar_editais()
        elif mensagem == '8':
            return self.lei_14133()
        elif mensagem == '9':
            return self.mei_pequenas_empresas()
        elif mensagem == '#':
            return self.duvidas_frequentes()
        elif mensagem == '0':
            return self.atendente()
        
        # Palavras-chave inteligentes
        elif 'horário' in mensagem or 'horario' in mensagem or 'contato' in mensagem:
            return self.horario()
        elif 'pregão' in mensagem or 'pregao' in mensagem:
            return self.info_pregao()
        elif 'concorrência' in mensagem or 'concorrencia' in mensagem:
            return self.info_concorrencia()
        elif 'dispensa' in mensagem or 'inexigibilidade' in mensagem:
            return self.contratacao_direta()
        elif 'documento' in mensagem or 'certidão' in mensagem or 'certidao' in mensagem:
            return self.documentos()
        elif 'prazo' in mensagem:
            return self.prazos()
        elif 'recurso' in mensagem or 'impugnação' in mensagem or 'impugnacao' in mensagem:
            return self.recursos()
        elif 'lei' in mensagem or '14133' in mensagem or '8666' in mensagem:
            return self.lei_14133()
        elif 'mei' in mensagem or 'microempresa' in mensagem or 'epp' in mensagem:
            return self.mei_pequenas_empresas()
        elif 'edital' in mensagem or 'editais' in mensagem:
            return self.onde_consultar_editais()
        elif 'proposta' in mensagem:
            return self.como_fazer_proposta()
        elif 'cadastro' in mensagem or 'fornecedor' in mensagem:
            return self.cadastro()
        
        # Mensagem não compreendida
        else:
            return self.mensagem_nao_entendida()
    
    # ========================================
    # MENU E INFORMAÇÕES BÁSICAS
    # ========================================
    
    def saudacao(self):
        """Menu principal"""
        return f"""🏛️ Bem-vindo ao Setor de Licitação
Prefeitura Municipal de Terenos/MS

Tire suas dúvidas sobre licitações!

📚 CONCEITOS BÁSICOS*
1 - O que é licitação?
2 - Tipos e modalidades
3 - Como participar

📄 DOCUMENTAÇÃO E PROCESSO*
4 - Documentos necessários
5 - Prazos importantes
6 - Recursos e impugnação
7 - Onde consultar editais

📖 LEGISLAÇÃO E REGRAS
8 - Lei 14.133/2021
9 - MEI e Pequenas Empresas

*❓ AJUDA
# - Dúvidas frequentes
0 - Falar com atendente

💡 Ou digite palavras-chave:
"pregão", "documentos", "prazo", "MEI", "cadastro"

Digite o número ou palavra-chave."""
    
    def horario(self):
        """Horário e contato"""
        return f"""🕐 *HORÁRIO E CONTATO*

📅 {self.horario_funcionamento}

📞 *Telefone:* {self.telefone}
📧 *E-mail:* {self.email}
📍 *Endereço:* {self.endereco}
🌐 *Site:* {self.site}

⚠️ Não atendemos sábados, domingos e feriados.

Digite *menu* para voltar."""
    
    # ========================================
    # CONCEITOS FUNDAMENTAIS
    # ========================================
    
    def o_que_e_licitacao(self):
        """Explica o que é licitação"""
        return """📚 *O QUE É LICITAÇÃO?*

DEFINIÇÃO:
Processo que a Administração Pública usa para escolher a melhor proposta para contratar obras, serviços e compras.

OBJETIVOS:
✓ Garantir igualdade de oportunidades
✓ Selecionar a melhor proposta
✓ Obter o melhor preço
✓ Assegurar transparência

PRINCÍPIOS:
• Legalidade
• Impessoalidade
• Moralidade
• Publicidade
• Eficiência

*QUEM PODE PARTICIPAR?*
✅ Empresas (ME, EPP, grandes)
✅ MEI
✅ Cooperativas

*BENEFÍCIOS:*
✓ Competição justa
✓ Melhores preços
✓ Oportunidades iguais
✓ Transparência

💡 Digite "2" para conhecer os tipos!

Digite *menu* para voltar."""
    
    def tipos_licitacao(self):
        """Tipos e modalidades"""
        return """📊 *TIPOS DE LICITAÇÃO*
*(Lei 14.133/2021)

1️⃣ PREGÃO (Mais comum)
• Bens e serviços comuns
• Menor preço
• Processo rápido

2️⃣ CONCORRÊNCIA
• Grandes obras
• Serviços complexos
• Processo mais rigoroso

3️⃣ CONCURSO
• Trabalhos técnicos/artísticos
• Julgamento por comissão

4️⃣ LEILÃO
• Venda de bens públicos
• Maior lance vence

5️⃣ DIÁLOGO COMPETITIVO
• Inovação e tecnologia
• Negociação permitida

CONTRATAÇÃO DIRETA:

📌 DISPENSA:
• Emergência
• Pequenos valores (até R$ 100 mil obras, R$ 50 mil outros)

📌 INEXIGIBILIDADE:
• Fornecedor exclusivo
• Serviços especializados

💡 Digite "pregão" ou "dispensa" para detalhes!

Digite *menu* para voltar."""
    
    def info_pregao(self):
        """Detalhes sobre pregão"""
        return """⚡ *PREGÃO - DETALHES*

O QUE É:
Modalidade mais rápida para bens e serviços comuns.

*COMO FUNCIONA:*

1️⃣ Publicação do edital
2️⃣ Apresentação de propostas (min. 8 dias)
3️⃣ Disputa de lances (ao vivo)
4️⃣ Habilitação do vencedor
5️⃣ Adjudicação

TIPOS:
🖥️ *Eletrônico* - pela internet
🏢 *Presencial* - na sede do órgão

VANTAGENS:
✅ Rapidez
✅ Economia
✅ Transparência

CRITÉRIO:
💰 Sempre MENOR PREÇO

Digite menu para voltar."""
    
    def info_concorrencia(self):
        """Detalhes sobre concorrência"""
        return """🏗️ *CONCORRÊNCIA - DETALHES*

O QUE É:
Modalidade para obras e serviços de grande porte.

QUANDO USAR:
• Obras complexas
• Grandes valores
• Serviços especializados

CRITÉRIOS:
• Menor preço
• Técnica e preço
• Melhor técnica

FASES:
1️⃣ Publicação (min. 30 dias)
2️⃣ Habilitação de TODOS
3️⃣ Abertura de propostas
4️⃣ Julgamento técnico
5️⃣ Homologação

CARACTERÍSTICAS:
⏱️ Processo mais longo
📋 Documentação rigorosa
🎯 Análise técnica detalhada

Digite (menu) para voltar."""
    
    def contratacao_direta(self):
        """Dispensa e inexigibilidade"""
        return """🚨 CONTRATAÇÃO DIRETA*
(Sem Licitação)

1️⃣ DISPENSA*

Casos permitidos:
💰 Pequenos valores:
• Obras: até R$ 100.000
• Outros: até R$ 50.000

🚨 Emergência:
• Risco à segurança
• Urgência comprovada
• Prazo: até 180 dias

2️⃣ INEXIGIBILIDADE*

Quando é impossível licitar:
🏆 Fornecedor exclusivo
👨‍🏫 Serviços especializados
🎭 Profissionais consagrados

IMPORTANTE:
⚠️ Exige justificativa detalhada
⚠️ Deve ser publicada
⚠️ Fiscalização rigorosa

Digite (menu) para voltar."""
    
    # ========================================
    # COMO PARTICIPAR
    # ========================================
    
    def como_participar(self):
        """Passo a passo para participar"""
        return f"""✅ *COMO PARTICIPAR*

*PASSO A PASSO:*

1️⃣ ENCONTRE EDITAIS*
🌐 {self.site}
📧 {self.email}

2️⃣ BAIXE O EDITAL*
📄 Gratuito
• Leia com atenção
• Verifique prazos

3️⃣ PREPARE DOCUMENTOS*
📋 Habilitação completa
💡 Digite "4" para lista!

4️⃣ ELABORE PROPOSTA*
💰 Calcule custos
• Não ultrapasse valor máximo
• Inclua TODOS os custos

5️⃣ PROTOCOLE*
⏰ Dentro do prazo
• Envelope lacrado (presencial)
• Upload (eletrônico)

6️⃣ ACOMPANHE*
📺 Sessão pública
• Participe de lances

7️⃣ SE VENCER*
🎉 Assine contrato (3 dias)

📞 Dúvidas? {self.telefone}

Digite *menu* para voltar."""
    
    # ========================================
    # DOCUMENTAÇÃO
    # ========================================
    
    def documentos(self):
        """Documentos necessários"""
        return """📄 *DOCUMENTOS NECESSÁRIOS PARA LICITAÇÃO*

*Pessoa Jurídica:*
✓ CNPJ atualizado
✓ Contrato Social ou Estatuto
✓ Certidão Negativa de Débitos Federal
✓ Certidão de Regularidade do FGTS
✓ Certidão Negativa Trabalhista (CNDT)
✓ Alvará de funcionamento
✓ Atestado de capacidade técnica

*Pessoa Física:*
✓ CPF e RG
✓ Comprovante de residência
✓ Certidões negativas
✓ Registro profissional (se aplicável)

⚠️ Importante: Todos os documentos devem estar dentro do prazo de validade!

💡 Para fazer cadastro, digite cadastro ou 3

Digite *menu* para voltar."""
    
    # ========================================
    # PRAZOS E RECURSOS
    # ========================================
    
    def prazos(self):
        """Prazos importantes"""
        return """⏱️ *PRAZOS IMPORTANTES*

ANTES DA LICITAÇÃO:

📅 IMPUGNAÇÃO:
• 3 dias ÚTEIS antes da abertura
• Qualquer pessoa pode

📅 ESCLARECIMENTO:
• 3 dias ÚTEIS antes
• Resposta obrigatória

DURANTE:

📅 PROPOSTAS:
• Pregão: mínimo 8 dias úteis
• Concorrência: mínimo 30 dias

📅 RECURSOS:
• 3 dias ÚTEIS após decisão
• Fundamentado por escrito

📅 CONTRARRAZÕES:
• 3 dias ÚTEIS após recurso

*APÓS VENCER:*

📅 CONTRATO:
• Assinar em 3 dias

REGRAS:
✅ Dias ÚTEIS (exceto sábado/domingo/feriado)
✅ Contagem: dia seguinte à publicação
✅ Recurso SUSPENDE processo

⚠️ Perder prazo = perder direito!*

Digite *menu* para voltar."""
    
    def recursos(self):
        """Como recorrer"""
        return f"""⚖️ *RECURSOS E IMPUGNAÇÃO*

1️⃣ IMPUGNAÇÃO DO EDITAL

Quando: Edital tem ilegalidades
Quem: Qualquer pessoa
Prazo: 3 dias ÚTEIS antes

2️⃣ RECURSO ADMINISTRATIVO*

Quando cabe:
• Habilitação/inabilitação
• Julgamento de propostas
• Anulação

*Prazo:* 3 dias ÚTEIS após

Como fazer:
📧 {self.email}
📍 {self.endereco}

Conteúdo:
• Identificação
• Número do processo
• Razões fundamentadas
• Documentos

Efeito: SUSPENDE processo

3️⃣ CONTRARRAZÕES*

Outros podem se manifestar
Prazo: 3 dias ÚTEIS

DICAS:
✅ Seja objetivo
✅ Fundamente bem
✅ Junte provas
✅ Respeite prazos

📞 Dúvidas: {self.telefone}

Digite (menu) para voltar."""
    
    # ========================================
    # LEGISLAÇÃO
    # ========================================
    
    def lei_14133(self):
        """Lei 14.133/2021"""
        return """📖 LEI 14.133/2021*
(Nova Lei de Licitações)

O QUE MUDOU:

✅ UNIFICAÇÃO
Substituiu 3 leis antigas:
• 8.666/93
• 10.520/02
• 12.462/11

PRINCIPAIS NOVIDADES:

1️⃣ Planejamento obrigatório
2️⃣ Pregão como regra
3️⃣ Diálogo competitivo
4️⃣ Contratação integrada
5️⃣ Sustentabilidade
6️⃣ Transparência

PRINCÍPIOS:
• Legalidade
• Impessoalidade
• Moralidade
• Publicidade
• Eficiência
• Economicidade

VALORES DISPENSA:
💰 Obras: até R$ 100.000
💰 Outros: até R$ 50.000

ACRÉSCIMOS:
📊 Até 25% do valor

VIGÊNCIA:
📅 Desde 01/04/2021

🌐 Consulte: planalto.gov.br

Digite (menu) para voltar."""
    
    # ========================================
    # MEI E PEQUENAS EMPRESAS
    # ========================================
    
    def mei_pequenas_empresas(self):
        """Benefícios MEI/ME/EPP"""
        return """👥 *MEI, ME E EPP*

✅ PODEM PARTICIPAR!

*ENQUADRAMENTO:*
🏪 MEI: até R$ 81 mil/ano
🏢 ME: até R$ 360 mil/ano
🏭 EPP: R$ 360 mil a R$ 4,8 milhões/ano

BENEFÍCIOS (LC 123/2006):

1️⃣ EMPATE FICTO
Proposta até 10% acima?
• Pode IGUALAR
• E GANHAR!

2️⃣ LICITAÇÕES EXCLUSIVAS
Até R$ 80.000
• Só para ME/EPP

3️⃣ COTAS RESERVADAS
25% em grandes licitações

4️⃣ REGULARIZAÇÃO POSTERIOR
Certidões com restrição?
• 5 dias para regularizar
• Após ser declarado vencedor

COMO COMPROVAR:
📋 Declaração de enquadramento
📋 MEI: CCMEI válido

ATENÇÃO:
⚠️ Qualificação técnica: mesmas exigências!
⚠️ Declaração falsa = crime!

EXEMPLO:
Menor: R$ 100.000
Sua (ME): R$ 105.000
✅ Empate ficto! Pode igualar e ganhar!

Digite (menu) para voltar."""
    
    # ========================================
    # INFORMAÇÕES COMPLEMENTARES
    # ========================================
    
    def onde_consultar_editais(self):
        """Onde encontrar editais"""
        return f"""📢 *ONDE CONSULTAR EDITAIS*

*CANAIS OFICIAIS:*

🌐 SITE
{self.site}
• Seção "Licitações"
• Download gratuito
• Atualizações diárias

📧 E-MAIL
{self.email}
• Solicite edital específico
• Tire dúvidas

📞 TELEFONE
{self.telefone}
• Informações
• Status de processos

📍 PRESENCIAL
{self.endereco}
🕐 {self.horario_funcionamento}
• Cópia gratuita

📰 DIÁRIO OFICIAL
• Avisos de abertura
• Resultados
• Homologações

O QUE VOCÊ ENCONTRA:
📋 Objeto detalhado
📋 Especificações técnicas
📋 Valor estimado
📋 Prazos
📋 Documentação exigida
📋 Modelo de proposta
📋 Anexos

⚠️ TODOS GRATUITOS!

PRAZOS:
📅 Pregão: mín. 8 dias
📅 Concorrência: mín. 30 dias

Digite *menu* para voltar."""
    
    def como_fazer_proposta(self):
        """Como elaborar proposta"""
        return """💰 *COMO FAZER PROPOSTA*

PASSO A PASSO:

1️⃣ LEIA O EDITAL*
📋 Com atenção total!

2️⃣ CALCULE CUSTOS*
Inclua TUDO:
• Materiais
• Mão de obra
• Encargos (INSS, FGTS)
• Impostos
• Transporte
• Lucro

⚠️ Não esqueça nada!

3️⃣ USE MODELO DO EDITAL
📄 Preencha corretamente:
• Dados da empresa
• Valores (unitário/total)
• Validade (mín. 60 dias)
• Prazo de entrega

4️⃣ VERIFIQUE LIMITES
⚠️ Não ultrapasse valor máximo
⚠️ Não seja inexequível (muito baixo)

5️⃣ ANEXE
📎 Planilha detalhada
📎 Cronograma
📎 Declarações

6️⃣ APRESENTE
📧 Eletrônico: upload
📮 Presencial: envelope lacrado

ERROS COMUNS:
❌ Proposta acima do máximo
❌ Esquecer de assinar
❌ CNPJ diferente
❌ Rasuras
❌ Falta de informações

DICAS:
✅ Seja competitivo
✅ Seja realista
✅ Seja claro
✅ Seja pontual

Digite *menu* para voltar."""
    
    def cadastro(self):
        """Cadastro de fornecedores"""
        return f"""📝 *CADASTRO DE FORNECEDORES*

COMO FAZER:

📧 Envie os documentos por e-mail:
{self.email}

📋 DOCUMENTOS NECESSÁRIOS:

Pessoa Jurídica:
✓ CNPJ atualizado
✓ Contrato Social ou Estatuto
✓ Certidão Negativa de Débitos Federal
✓ Certidão de Regularidade do FGTS
✓ Certidão Negativa Trabalhista (CNDT)
✓ Alvará de funcionamento
✓ Atestado de capacidade técnica

Pessoa Física:
✓ CPF e RG
✓ Comprovante de residência
✓ Certidões negativas
✓ Registro profissional (se aplicável)

⚠️ Importante:* Todos os documentos devem estar dentro do prazo de validade!

⏱️ Prazo de análise:* até 5 dias úteis

📄 Após aprovação:*
Você receberá o CRC (Certificado de Registro Cadastral) por e-mail

RENOVAÇÃO:
🔄 30 dias antes do vencimento

📞 Dúvidas? {self.telefone}

Digite (menu) para voltar."""
    
    # ========================================
    # DÚVIDAS FREQUENTES
    # ========================================
    
    def duvidas_frequentes(self):
        """Perguntas frequentes"""
        return f"""❓ *DÚVIDAS FREQUENTES*

1. O que é licitação?
Processo para escolher melhor proposta.

2. Qualquer empresa pode?
✅ SIM! Desde que atenda exigências.

3. MEI pode participar?
✅ SIM! Com benefícios especiais.

4. É pago?
❌ NÃO! Edital é gratuito.

5. Preciso estar cadastrado?*
❌ NÃO obrigatório, mas facilita.

6. Posso impugnar edital?*
✅ SIM! Até 3 dias antes.

7. Diferença pregão x concorrência?*
Pregão: rápido, bens comuns
Concorrência: obras complexas

8. E se minha certidão vencer?*
⚠️ Precisa renovar! Sempre válida.

9. Posso desistir após vencer?*
❌ NÃO! Sofre sanções.

10. Quanto tempo até assinar?*
3 dias após convocação.

11. MEI tem vantagens?*
✅ SIM! Empate ficto, cotas, etc.

12. Onde consulto editais?*
🌐 {self.site}
📧 {self.email}

Mais dúvidas?
📞 {self.telefone}
📧 {self.email}

Digite *menu* para voltar."""
    

    def cadastro(self):
        """Como fazer cadastro de fornecedor"""
        return f"""📝 *COMO FAZER O CADASTRO*

O cadastro é feito pela nossa equipe!

*PASSO 1:* Envie os documentos necessários por e-mail
📧 {self.email}

*PASSO 2:* Nossa equipe irá analisar seus documentos

*PASSO 3:* Aguarde o retorno
⏱️ Prazo: até 2 dias úteis

*PASSO 4:* Você receberá um e-mail confirmando que o cadastro foi aprovado!

📄 *Documentos necessários:*
Digite *4* no menu para ver a lista completa

💡 *Dica:* Envie os documentos digitalizados (PDF ou imagens) para agilizar o processo!

📞 *Dúvidas?* Ligue: {self.telefone}

Digite *menu* para voltar às opções."""
    
    def atendente(self):
        """Falar com atendente"""
        return f"""👤 *FALAR COM ATENDENTE*

Para atendimento personalizado:

📞 Ligue: {self.telefone}
🕐 {self.horario_funcionamento}

📧 E-mail: {self.email}
⏱️ Respondemos em até 24 horas

📍 Atendimento presencial:
{self.endereco}
{self.horario_funcionamento}

⚠️ Para atendimento presencial, recomendamos agendar pelo telefone.

Digite *menu* para voltar."""

    def atendente(self):
        """Falar com atendente"""
        return f"""👤 *FALAR COM ATENDENTE*

Para atendimento personalizado:

📞 Ligue: {self.telefone}
🕐 {self.horario_funcionamento}

📧 E-mail: {self.email}
⏱️ Respondemos em até 24 horas

📍 Atendimento presencial:
{self.endereco}
{self.horario_funcionamento}

⚠️ Para atendimento presencial, recomendamos agendar pelo telefone.

Digite *menu* para voltar."""
    
    def mensagem_nao_entendida(self):
        """Resposta padrão"""
        return """❌ Desculpe, não entendi.

💡 VOCÊ PODE:

*Digitar números:*
1 - O que é licitação?
2 - Tipos e modalidades
3 - Como participar
4 - Documentos
5 - Prazos
6 - Recursos
7 - Onde consultar editais
8 - Lei 14.133
9 - MEI/EPP
# - Dúvidas frequentes
0 - Atendente

Ou palavras-chave:
"pregão", "documentos", "prazo", "MEI", "recurso"

Digite *menu* para opções!"""
