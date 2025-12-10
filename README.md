# Hacker News Crawler

## Обзор проекта
Асинхронный веб-поисковик для Hacker News (news.ycombinator.com) с хранилищем данных.  

## Особенности

- Асинхронный обход с использованием `aiohttp`
- Анализ основных новостей и комментариев
- Хранение данных в SQLite с помощью `aiosqlite`

## Установка

```bash
git clone https://github.com/AlexandrGor13/homework_hn_crawler.git
cd crawler
pip install -r requirements.txt
```

## Использование
### Запуск crawler (непрерывный режим):

```bash
python main.py
```

### Один цикл обхода:

```bash
python main.py --once
```

### Показать последние 5 сохраненных новостей:

```bash
python main.py --show 5
```

