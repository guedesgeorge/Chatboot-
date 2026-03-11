# 🏛️ Chatbot de Licitações - Terenos/MS

Assistente virtual para tirar dúvidas sobre processos licitatórios da Prefeitura Municipal de Terenos/MS.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Deploy](#deploy)
- [Configuração](#configuração)
- [Testes](#testes)

---

## 📖 Sobre o Projeto

Chatbot desenvolvido para automatizar o atendimento e fornecer informações sobre licitações da Prefeitura Municipal de Terenos/MS via WhatsApp.

**Tecnologias:**
- Python 3.x
- Flask (servidor web)
- Twilio (integração WhatsApp)
- Railway (hospedagem)

---

## ✨ Funcionalidades

### Informações sobre Licitações:
✅ O que é licitação  
✅ Tipos e modalidades (Pregão, Concorrência, etc.)  
✅ Como participar de licitações  
✅ Documentos necessários  
✅ Prazos importantes  
✅ Recursos e impugnações  
✅ Lei 14.133/2021 (Nova Lei)  
✅ Benefícios para MEI/ME/EPP  
✅ Onde consultar editais  
✅ Cadastro de fornecedores  
✅ Dúvidas frequentes  

### Inteligência:
🧠 Reconhece palavras-chave  
🧠 Menu interativo  
🧠 Respostas contextualizadas  

---

## 📁 Estrutura do Projeto

```
chatbot-licitacoes/
│
├── app/                          # Aplicação principal
│   ├── bot_twilio.py            # Servidor Flask + Twilio
│   └── chatbot_base.py          # Lógica do chatbot
│
├── config/                       # Configurações
│   └── config.py                # Configurações centralizadas
│
├── tests/                        # Testes
│   └── testar_local.py          # Teste no terminal
│
├── docs/                         # Documentação
│   └── (vazio - para futuras docs)
│
├── requirements.txt              # Dependências Python
├── Procfile                      # Configuração Railway
└── README.md                     # Este arquivo
```

---

## 🚀 Instalação

### 1. Clone o projeto (ou baixe os arquivos)

```bash
cd /Users/georgeemannuel/Downloads
# Copie a pasta chatbot-licitacoes para este diretório
```

### 2. Instale as dependências

```bash
cd chatbot-licitacoes
pip3 install -r requirements.txt
```

---

## 💻 Como Usar

### Testar Localmente (Terminal)

```bash
cd tests
python3 testar_local.py
```

Você verá o menu e poderá conversar com o bot diretamente no terminal!

### Rodar o Servidor Local

```bash
cd app
python3 bot_twilio.py
```

O servidor estará disponível em: `http://localhost:5000`

---

## 🌐 Deploy (Railway)

### 1. Fazer login no Railway

```bash
railway login --browserless
# Use o código que aparecer
```

### 2. Link com o projeto

```bash
cd chatbot-licitacoes
railway link
# Selecione: genuine-connection → proactive-essence → production
```

### 3. Deploy

```bash
railway up
```

### 4. Verificar URL

O Railway fornecerá uma URL pública, exemplo:
```
https://pleasant-spirit-production-6737.up.railway.app
```

### 5. Configurar Webhook no Twilio

No painel Twilio:
- URL: `https://SEU-DOMINIO.up.railway.app/whatsapp`
- Método: POST

---

## ⚙️ Configuração

### Editar Informações de Contato

Edite o arquivo: `app/chatbot_base.py`

```python
self.horario_funcionamento = "Segunda a Sexta: 8h às 17h"
self.telefone = "(67) 3389-6654"
self.email = "licitacao@terenos.ms.gov.br"
self.endereco = "Rua Principal, 100 - Centro, Terenos/MS"
self.site = "www.terenos.ms.gov.br"
```

### Configurações Avançadas

Edite: `config/config.py`

---

## 🧪 Testes

### Teste no Terminal

```bash
cd tests
python3 testar_local.py
```

### Teste no WhatsApp (Twilio Sandbox)

1. Envie mensagem para: `+1 415 523 8886`
2. Digite: `join characteristic-melody`
3. Aguarde confirmação
4. Teste: `oi`, `documentos`, `cadastro`, etc.

---

## 📞 Contato - Prefeitura de Terenos/MS

- **Telefone:** (67) 3389-6654
- **E-mail:** licitacao@terenos.ms.gov.br
- **Endereço:** Rua Principal, 100 - Centro, Terenos/MS
- **Site:** www.terenos.ms.gov.br
- **Horário:** Segunda a Sexta: 8h às 17h

---

## 📝 Comandos Úteis

### Atualizar bot no Railway:
```bash
cd chatbot-licitacoes
railway up
```

### Ver logs do Railway:
```bash
railway logs
```

### Testar localmente:
```bash
cd tests && python3 testar_local.py
```

### Rodar servidor local:
```bash
cd app && python3 bot_twilio.py
```

---

## 🛠️ Manutenção

### Adicionar nova funcionalidade:

1. Edite `app/chatbot_base.py`
2. Adicione novo método
3. Adicione condição em `processar_mensagem()`
4. Teste localmente
5. Deploy no Railway

### Atualizar informações:

1. Edite variáveis em `__init__()` do `chatbot_base.py`
2. Deploy no Railway

---

## 📄 Licença

Desenvolvido para a Prefeitura Municipal de Terenos/MS.

---

## 🆘 Suporte

Em caso de problemas:
1. Verifique os logs: `railway logs`
2. Teste localmente primeiro
3. Verifique configurações do Twilio
4. Entre em contato com o desenvolvedor

---

**Versão:** 2.0  
**Última atualização:** 2026  
**Base Legal:** Lei 14.133/2021
