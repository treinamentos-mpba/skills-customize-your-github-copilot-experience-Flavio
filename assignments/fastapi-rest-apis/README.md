# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Criar a aplicação e listar tarefas

#### Descrição
Complete o código inicial para criar uma API de tarefas e disponibilizar uma rota que liste as tarefas armazenadas em memória. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `python starter-code.py`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com o título `Task API`.
- Implementar `GET /tasks` para retornar as tarefas como uma lista JSON.
- Permitir testar a rota e explorar a documentação interativa em `/docs`.

### 🛠️ Criar tarefas pela API

#### Descrição
Adicione uma rota para criar tarefas. Use um modelo Pydantic para validar os dados enviados no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Definir os campos `title` (texto) e `completed` (booleano, padrão `false`) no modelo de entrada.
- Implementar `POST /tasks` para validar os dados e armazenar uma nova tarefa.
- Atribuir um identificador único à tarefa e responder com o registro criado e o código de status `201`.

### 🛠️ Consultar, atualizar e remover tarefas

#### Descrição
Complete a API com rotas para consultar, substituir e remover uma tarefa pelo identificador. Use a documentação interativa para testar o ciclo completo.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa ou responder com `404` quando ela não existir.
- Implementar `PUT /tasks/{task_id}` para atualizar os dados da tarefa existente e responder com `404` quando o identificador não for encontrado.
- Implementar `DELETE /tasks/{task_id}` para remover a tarefa, responder com `204` em caso de sucesso e com `404` quando ela não existir.