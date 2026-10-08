# PLAN (ЛР1)

Ниже поэтапный план реализации ЛР1 без реализации ЛР2/ЛР3.

## Stage 0 — Foundation (текущий)

**Deliverables**
- Структура репозитория и `lab1` package scaffold.
- Единая документация требований/решений/статуса.
- Базовый CI (`pytest` + `ruff`).

**Acceptance criteria**
- Репозиторий устанавливается в editable-режиме.
- Smoke tests и lint проходят локально/в CI.

**Required tests**
- `pytest lab1/tests -q`
- `ruff check lab1/src lab1/tests`

**Depends on**
- Нет.

## Stage 1 — Automatic collection

**Deliverables**
- Модуль автоматического сбора документов.
- Обнаружение новых/изменённых документов.
- Персистентный state и защита от дублей.
- Повторяемый запуск и обработка ошибок.

**Acceptance criteria**
- Повторный запуск без новых данных не дублирует документы.
- Изменённые документы переобрабатываются предсказуемо.
- Ошибки источника логируются и не разрушают state.

**Required tests**
- Unit tests на change detection/state.
- Интеграционный smoke-test на повторный запуск.

**Depends on**
- Stage 0.

## Stage 2 — Preprocessing and indexing

**Deliverables**
- Очистка/нормализация текста.
- Чанкинг + метаданные chunk/document.
- Индексация embeddings в vector store.

**Acceptance criteria**
- Каждый chunk имеет воспроизводимый ID и метаданные источника.
- Индекс строится повторяемо на одном и том же входе.

**Required tests**
- Unit tests на chunking/metadata.
- Smoke-test построения индекса на маленьком fixture-наборе.

**Depends on**
- Stage 1.

## Stage 3 — Retrieval pipeline

**Deliverables**
- Поиск Top-K кандидатов.
- Эксперименты по Top-K с сохранением результатов.

**Acceptance criteria**
- Retrieval возвращает ранжированный список с оценками/метаданными.
- Результаты экспериментов сохраняются в trackable формате.

**Required tests**
- Unit tests на retrieval API.
- Регрессионные тесты формата результатов.

**Depends on**
- Stage 2.

## Stage 4 — Reranking and filtering

**Deliverables**
- Reranking кандидатов.
- Фильтрация контекста по порогу/правилам.
- Сравнение с/без reranking/filtering.

**Acceptance criteria**
- Параметры reranking/filtering настраиваются конфигом.
- Сравнение зафиксировано в воспроизводимых отчётах.

**Required tests**
- Unit tests на пороговую фильтрацию и stable ordering.

**Depends on**
- Stage 3.

## Stage 5 — Answer generation

**Deliverables**
- Генерация ответа по найденному контексту.
- Отказ при недостаточном контексте.
- Ссылки на источники в ответе.

**Acceptance criteria**
- При низкой уверенности система отказывается отвечать корректно.
- Ответы содержат ссылки на использованные источники.

**Required tests**
- Unit/integration tests на формат ответа и refusal policy.

**Depends on**
- Stage 4.

## Stage 6 — Evaluation and experiments

**Deliverables**
- Набор оценочных вопросов (целевой ориентир: >=30).
- Протокол и метрики retrieval/answer quality.
- Серия staged-экспериментов и обоснование решений.

**Acceptance criteria**
- Эксперименты воспроизводимы и сохранены.
- Для финальной конфигурации есть обоснование trade-offs.

**Required tests**
- Проверка схемы датасета/результатов.
- Скрипт(ы) повторного прогона метрик.

**Depends on**
- Stage 5.

## Что обязательно vs рекомендовано

- **Обязательно:** рабочий RAG, автоматический сбор, retrieval, reranking/filtering, генерация, evaluation.
- **Рекомендовано:** полный набор экспериментов (2+ embeddings, 2+ LLM/prompt и т.д.).
- Допускаются альтернативы, если они явно аргументированы в отчёте.
