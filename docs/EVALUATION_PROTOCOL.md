# EVALUATION PROTOCOL (ЛР1)

## 1) Цель

Оценивать качество retrieval и итоговых ответов RAG-системы на воспроизводимом наборе вопросов.

## 2) Схема датасета вопросов

Минимальная структура (JSON/CSV):

- `question_id` — стабильный ID.
- `question_text` — текст вопроса.
- `question_type` — `factual | multi_document | contextual | unanswerable`.
- `expected_answer` — эталонный краткий ответ/критерий правильности.
- `expected_source_refs` — список ожидаемых источников (документ/секция/URL).
- `notes` — дополнительные условия проверки.

Целевой ориентир: >=30 вопросов суммарно (рекомендация задания).

## 3) Разметка релевантности для retrieval

Для каждого `(question, chunk)`:
- `relevance_label`:
  - `2` — напрямую отвечает на вопрос,
  - `1` — частично полезен,
  - `0` — нерелевантен.

Дополнительно:
- `annotator` (кто размечал),
- `annotation_comment` (пояснение при спорных случаях).

## 4) Метрики retrieval

- Recall@K
- Precision@K
- MRR (Mean Reciprocal Rank)
- nDCG@K (при наличии graded relevance)

Сохранять значения по категориям вопросов и в aggregate.

## 5) Метрики answer generation

- Answer correctness (по рубрике/эталону, бинарно или шкала).
- Refusal quality для `unanswerable` вопросов.
- Source attribution correctness (корректность ссылок на источники).

При наличии ручной оценки:
- `judge_label`, `judge_comment`, `evidence_refs`.

## 6) Формат результатов

- Табличные результаты по каждому эксперименту (`experiments/results/`).
- Конфиг эксперимента (`experiments/configs/`) должен ссылаться на датасет и параметры запуска.
- Каждая таблица содержит:
  - `experiment_id`
  - `timestamp`
  - ключевые параметры
  - retrieval и answer метрики

## 7) Staged experiment plan (без полного комбинаторного перебора)

1. **Baseline**: один способ chunking + один embedding + Top-K без reranking.
2. **Chunking stage**: фиксируем остальное, сравниваем варианты chunk/overlap.
3. **Embedding stage**: сравниваем минимум 2 embedding-подхода на лучшем chunking.
4. **Top-K stage**: подбор K на выбранной паре chunking+embedding.
5. **Reranking/filtering stage**: сравнение с/без reranking и порогов фильтрации.
6. **Generation stage**: сравнение минимум 2 prompt и (по возможности) 2 LLM/mode.
7. **Final selection**: фиксируем итоговую конфигурацию и rationale.

## 8) Воспроизводимость

- Все эксперименты запускаются из версионируемых конфигов.
- Датасет вопросов и схема разметки версионируются.
- Любые пропуски/невыполненные эксперименты явно документируются с причиной.
