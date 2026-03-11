## 🏛️ Chatbot de Licitações - Prefeitura de Terenos/MS
Assistente virtual inteligente para desburocratizar o acesso a informações sobre processos licitatórios da Prefeitura Municipal de Terenos/MS.

## 📖 Sobre o Projeto
Este chatbot foi desenvolvido para automatizar o atendimento ao cidadão e aos fornecedores, fornecendo respostas rápidas sobre a Nova Lei de Licitações (Lei 14.133/2021). Ele funciona como uma camada de transparência ativa, permitindo que qualquer interessado consulte documentos, prazos e modalidades de licitação diretamente pelo Telegram.

## 🛠️ Tecnologias Utilizadas
Linguagem: Python.
Interface: Telegram Bot API (via python-telegram-bot ou similar).
Infraestrutura/Cloud: Railway.
Metodologia: Reconhecimento de palavras-chave e menu interativo contextualizado.

## ✨ Funcionalidades Principais
📂 Consultas de Licitação
✅ Guia da Lei 14.133/2021: Explicações sobre a Nova Lei de Licitações.
✅ Modalidades: Informações sobre Pregão, Concorrência e Dispensa.
✅ Checklist de Documentos: Lista necessária para habilitação de fornecedores.
✅ Portal da Transparência: Links diretos para editais e anexos.

## 🧠 Inteligência e UX
Menu Interativo: Navegação guiada para facilitar o uso por usuários leigos.
Respostas Contextualizadas: Identificação de intenções para dúvidas frequentes.
Suporte MEI/ME/EPP: Seção dedicada aos benefícios garantidos por lei para pequenos negócios.
## 🚀 Estrutura de Pastas
Plaintext
chatbot-licitacoes/
├── app/                  # Lógica central do bot e integração com Telegram
├── config/               # Gerenciamento de variáveis de ambiente
├── tests/                # Scripts de validação e testes unitários
├── requirements.txt      # Dependências do projeto
└── Procfile              # Configuração de runtime para o Railway

## ⚙️ Configuração e Deploy
1. Requisitos
Python 3.10 ou superior.
Um TELEGRAM_TOKEN (obtido via @BotFather).

2. Instalação Local
Bash
git clone https://github.com/seu-usuario/chatbot-licitacoes.git
cd chatbot-licitacoes
pip install -r requirements.txt

3. Deploy no Railway
Este projeto está configurado para deploy contínuo no Railway:
Conecte seu repositório ao painel do Railway.
Adicione as Variáveis de Ambiente (Environment Variables) necessárias.
O deploy será feito automaticamente a cada git push.
📞 Contato Institucional
Setor: Departamento de Licitações - Terenos/MS.
Telefone: (67) 3389-6654.
E-mail: licitacao@terenos.ms.gov.br.
Horário: Segunda a Sexta, das 07h às 13h.

## 📝 Licença e Desenvolvedor
Desenvolvido por George Emmanuel como solução de automação para o setor público.
Versão: 2.0 (Migração para Telegram).
Status: Em produção.
Deseja que eu escreva também um pequeno guia de como criar as variáveis de ambiente no Railway para esse bot?

# BY 
George Guedes