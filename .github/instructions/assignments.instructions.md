---
description: "Instruções para usar ao criar ou editar arquivos Markdown de tarefas, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos Markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos Markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- Cada tarefa deve ser criada como um arquivo `README.md` dentro da pasta correspondente em `assignments/`.
- Não remova nem pule seções do template.

## 2. Orientação das Seções

Os cabeçalhos devem usar exatamente os textos do template, incluindo os emojis. Não traduza nem altere os cabeçalhos.

- `# 📘 Atividade: [Título da Atividade]` — Use um título curto e descritivo.
- `## 🎯 Objetivo` — Escreva de 1 a 2 frases sobre o que o aluno aprenderá ou construirá.
- `## 📝 Tarefas` — Inclua uma seção para cada tarefa, usando a estrutura abaixo:
  - `### 🛠️ [Título da Tarefa]` — Use um título específico e orientado à ação.
  - `#### Descrição` — Explique claramente o que o aluno deve fazer.
  - `#### Requisitos` — Liste resultados ou funcionalidades esperadas em itens objetivos e verificáveis.
- Inclua exemplos de entrada e saída em blocos de código quando forem úteis.

Não inclua seções extras, a menos que solicitado explicitamente.