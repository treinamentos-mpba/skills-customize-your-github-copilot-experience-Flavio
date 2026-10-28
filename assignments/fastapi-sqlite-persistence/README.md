# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Atualize uma API de tarefas feita com FastAPI para armazenar os dados em um banco SQLite, em vez de mantê-los apenas na memória. Você praticará a criação de tabelas, consultas SQL parametrizadas e operações CRUD com dados persistentes.

## 📝 Tarefas

### 🛠️ Criar o banco e a tabela de tarefas

#### Descrição
Complete a função `initialize_database` no código inicial para criar a tabela `tasks` quando o servidor iniciar. Use o módulo `sqlite3`, que já faz parte da biblioteca padrão do Python, e mantenha o arquivo do banco na pasta da atividade.

#### Requisitos
O programa concluído deve:

- Criar a tabela `tasks` com `id` inteiro autoincrementado, `title` obrigatório e `completed` inteiro com valor padrão `0`.
- Usar `CREATE TABLE IF NOT EXISTS` para que iniciar o servidor novamente não apague os dados existentes.
- Criar o arquivo `tasks.db` na pasta da atividade.

### 🛠️ Salvar e listar tarefas no SQLite

#### Descrição
Implemente as rotas para criar e listar tarefas usando o banco. Teste a API em `/docs`, crie algumas tarefas e reinicie o servidor para verificar se os registros continuam disponíveis.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para salvar uma tarefa e `GET /tasks` para listar as tarefas salvas.
- Usar consultas SQL parametrizadas, como `?`, para incluir valores recebidos pela API.
- Retornar cada tarefa como JSON com `id`, `title` e `completed`, convertendo o valor inteiro armazenado no SQLite em booleano.
- Responder à criação com o código de status `201`.

### 🛠️ Completar o CRUD com persistência

#### Descrição
Atualize as rotas de consulta, atualização e remoção para operar diretamente no SQLite. Teste cada rota com identificadores existentes e inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e responder com `204` em caso de sucesso.
- Responder com `404` quando uma tarefa não existir, sem alterar outros registros.
