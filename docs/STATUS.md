# STATUS

## Текущий факт состояния

Подготовлен только фундамент репозитория для ЛР1. Полный RAG pipeline ещё не реализован.

## Выполненные работы

- Создана базовая структура документации (`docs/*`) для единого контекста.
- Добавлены короткие инструкции для AI-ассистентов.
- Создан минимальный Python scaffold `lab1` c CLI и smoke-тестами.
- Добавлен CI workflow для `ruff` и `pytest`.
- Обновлён `.gitignore` под Python/RAG-артефакты и локальные секреты.
- Добавлен `.env.example` только с комментариями.

## Фактически запущенные проверки

1. Установка dev-окружения:
   - `python -m pip install -e "./lab1[dev]"` ✅
2. Тесты:
   - `pytest lab1/tests -q` ✅ (3 passed)
3. Линтинг:
   - `ruff check lab1/src lab1/tests` ✅
4. Ручная проверка CLI:
   - `python -m pad_rag.cli --version` ✅
   - `python -m pad_rag.cli status` ✅

## Ограничения / блокеры

- Выбор провайдера генерации и финальных моделей не утверждён владельцем.
- Реализация функциональных модулей ЛР1 (collection/retrieval/reranking/generation/evaluation) ещё не начата.
