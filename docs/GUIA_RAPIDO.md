# 🚀 GUIA RÁPIDO - Chatbot Licitações

## ⚡ Início Rápido

### 1️⃣ Testar Localmente
```bash
cd chatbot-licitacoes/tests
python3 testar_local.py
```

### 2️⃣ Rodar Servidor
```bash
cd chatbot-licitacoes/app
python3 bot_twilio.py
```
Acesse: http://localhost:5000

### 3️⃣ Deploy no Railway
```bash
cd chatbot-licitacoes
railway up
```

---

## 📝 Comandos Principais

### Testar
```bash
cd tests
python3 testar_local.py
```

### Rodar Local
```bash
cd app
PORT=5001 python3 bot_twilio.py
```

### Deploy
```bash
railway up
```

### Ver Logs
```bash
railway logs
```

---

## 🔧 Editar Informações

### Arquivo: `app/chatbot_base.py`

Linha 12-16:
```python
self.telefone = "(67) 3389-6654"
self.email = "licitacao@terenos.ms.gov.br"
self.endereco = "Rua Principal, 100 - Centro, Terenos/MS"
```

Salve e faça deploy:
```bash
railway up
```

---

## 📞 Webhook Twilio

URL do webhook:
```
https://SEU-DOMINIO.up.railway.app/whatsapp
```

Método: POST

---

## 🧪 Testar no WhatsApp

1. Enviar para: +1 415 523 8886
2. Digite: `join characteristic-melody`
3. Teste: `oi`

---

## 📁 Estrutura Simplificada

```
chatbot-licitacoes/
├── app/
│   ├── bot_twilio.py      ← Servidor principal
│   └── chatbot_base.py    ← Lógica do bot (EDITE AQUI)
├── tests/
│   └── testar_local.py    ← Testes
├── requirements.txt
└── Procfile
```

---

## ✅ Checklist Deploy

- [ ] Editou informações em `chatbot_base.py`
- [ ] Testou localmente (`testar_local.py`)
- [ ] Fez login no Railway (`railway login --browserless`)
- [ ] Linkou projeto (`railway link`)
- [ ] Deploy (`railway up`)
- [ ] Configurou webhook no Twilio
- [ ] Testou no WhatsApp

---

## 🆘 Problemas Comuns

**Bot não responde?**
- Verifique logs: `railway logs`
- Confirme webhook está correto
- Teste localmente primeiro

**Erro de importação?**
- Verifique se está na pasta correta
- Instale dependências: `pip3 install -r requirements.txt`

**Porta em uso (5000)?**
- Use outra porta: `PORT=5001 python3 bot_twilio.py`

---

**Dúvidas? Consulte o README.md completo!**
