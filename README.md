# Flask Chatbot API

Este é um projeto básico de uma API em Flask para integrar e gerenciar provedores de chatbot de forma dinâmica. Atualmente, o projeto suporta múltiplos provedores, como OpenAI, mas é facilmente extensível para novos provedores.

---

## 📋 Funcionalidades

- Rota para interação com um chatbot (`/api/chat`).
- Estrutura modular usando blueprints.
- Suporte dinâmico para diferentes provedores de IA (OpenAI, etc.).
- Fácil configuração e expansão.

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) 3.9+
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI API](https://platform.openai.com/docs/)

---

## 📂 Estrutura do Projeto

```plaintext
app/
├── __init__.py          # Inicialização do Flask
├── chatapi.py           # Provedores para o ChatAPI
├── chatbot.py           # Blueprint para a rota de chatbot
.env                     # Configurações do ambiente
requirements.txt         # Dependências do projeto
README.md                # Documentação do projeto
```

## 🚀 Configuração e Execução
Siga os passos abaixo para rodar o projeto:

### 1. Clonar o Repositório
Clone este repositório para a sua máquina local:
```bash
git clone https://github.com/vmsou/flask-chatbot-api.git
cd flask-chatbot-api
```

### 2. Criar Ambiente Virtual
Crie e ative um ambiente virtual:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Linux/MacOS)
source venv/bin/activate

# Ativar o ambiente (Windows)
venv\Scripts\activate
```

### 3. Instalar Dependências
Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis (substitua pelos seus valores reais):
```bash
OPENAI_API_KEY=sua-chave-aqui
```

### 5. Rodar o Servidor
Execute o servidor Flask:
```bash
flask run
```
O servidor estará rodando em http://127.0.0.1:5000.

## 🧪 Testando a API
Endpoint `/api/chat`
Descrição: Envia uma mensagem para o chatbot e retorna a resposta.

- URL: `/api/chat`
- Método: `POST`
- Body: JSON
```json
{
  "message": "Olá, tudo bem?"
}
```
- Resposta: JSON
```json
{
  "message": "Tudo bem! Como posso te ajudar?"
}
```

### Teste com cURL
Use o cURL para testar o endpoint:
```bash
curl -X POST http://127.0.0.1:5000/api/chat \
-H "Content-Type: application/json" \
-d '{"message": "Olá, tudo bem?"}'
```

### Teste com Thunder Client (VSCode)
1. Instale a extensão Thunder Client.
2. Crie uma nova requisição:
- Método: `POST`
- URL: `http://127.0.0.1:5000/api/chat`
- Body:
```json
{
  "message": "Olá, teste!"
}
```
3. Clique em "Send"

## ⚙️ Adicionando Novos Provedores
Para adicionar um novo provedor:
1. Crie uma nova classe que herda de `ChatAPI` em `chatapi.py`.
2. Implemente o método `reply`.
3. Adicione a lógica do novo provedor no método `get` da classe `ChatAPIProvider`.

## 🛡️ Contribuição
Sinta-se à vontade para contribuir com melhorias e novos recursos! Faça um fork deste repositório, crie sua branch e envie um pull request.

## 📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
