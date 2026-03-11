"""
Teste do Chatbot no Terminal
Permite testar o bot localmente antes do deploy
"""

import sys
sys.path.append('../app')

from chatbot_base import ChatbotLicitacao


def main():
    print("\n" + "="*70)
    print("🤖 TESTE DO CHATBOT DE LICITAÇÕES - TERENOS/MS")
    print("="*70)
    print("Digite suas mensagens para testar o bot")
    print("Digite 'sair' para encerrar")
    print("="*70 + "\n")
    
    bot = ChatbotLicitacao()
    
    # Mostrar menu inicial
    print("Bot:", bot.saudacao())
    print()
    
    while True:
        try:
            mensagem = input("Você: ")
            
            if mensagem.lower() in ['sair', 'exit', 'quit']:
                print("\n👋 Até logo! Obrigado por testar o chatbot.")
                break
            
            resposta = bot.processar_mensagem(mensagem)
            print(f"\nBot: {resposta}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}\n")


if __name__ == "__main__":
    main()
