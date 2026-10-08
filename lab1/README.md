# lab1

Каркас для ЛР1 по RAG в рамках курса PAD.

На этом этапе:
- есть только структура пакета и CLI-заглушка;
- нет реализации полного RAG pipeline.

## Быстрый старт

```bash
python -m pip install -e "./lab1[dev]"
python -m pad_rag.cli --version
python -m pad_rag.cli status
pytest tests -q
ruff check src tests
```
