Projeto Flask - Sistema de Gerenciamento de Leads
Este projeto é uma API desenvolvida com Flask para gerenciar leads em um sistema de propostas de seguro automotivo. O sistema é estruturado utilizando a arquitetura hexagonal, e inclui funcionalidades para adicionar leads, enviar propostas e agendar lembretes para leads não respondidos.

Estrutura do Projeto
O projeto é organizado da seguinte maneira:

Modelos (models): Define a estrutura de dados do projeto.

Lead: Representa um lead com os seguintes atributos:
id: Identificador único do lead (opcional).
email: Endereço de e-mail do lead.
name: Nome do lead.
proposal_sent: Flag indicando se a proposta foi enviada.
response_received: Flag indicando se a resposta foi recebida.
Repositórios (repositories): Responsável pela persistência e recuperação dos dados.

LeadRepository: Gerencia a lista de leads em memória e oferece métodos para salvar e buscar leads.
Serviços (services): Contém a lógica de negócio do sistema.

LeadService: Fornece métodos para adicionar leads, enviar propostas e agendar lembretes para leads não responsivos.
Controladores (controllers): Lida com a entrada de dados e interage com os serviços.

LeadController: Define métodos para endpoints da API que permitem enviar propostas e agendar lembretes.
Rotas (routes): Define os endpoints da API.

lead_routes: Inclui endpoints para enviar propostas (/send_proposal), agendar lembretes (/start_reminder) e uma rota de entrada (/) que retorna uma mensagem de boas-vindas.
Tarefas (tasks): Define tarefas assíncronas utilizando Celery.

send_reminder_email: Tarefa para enviar um e-mail de lembrete para o lead.
Configuração e Execução
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure as variáveis de ambiente:

FLASK_APP: Defina como run.py
FLASK_ENV: Defina como development
Configure a URL do broker do Celery e a chave da API do Parcelvoy no arquivo config.py.
Execute a aplicação:

bash
Copiar código
flask run
