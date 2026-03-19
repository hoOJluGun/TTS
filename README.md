# 🎬 M9 Movie Production - Книга Президента США

## Описание

Полный продакшн-пакет для создания фильма из книги "Книга президента США, которого не было".

## Структура

```
m9-vault/
├── audio-player.html    # Аудио-плеер (открой в браузере и слушай!)
├── tts_queue.csv        # Полный текст для озвучки (33 сцены)
├── roles_map.csv        # Роли и голоса
├── visual/
│   └── art_queue.csv   # Промпты для AI-картинок
├── tools/
│   └── tts_generator.py # Генератор озвучки (Edge TTS)
├── build_m9.sh         # Скрипт сборки
└── QUICKSTART.md       # Инструкция
```

## Быстрый старт

### 1. Слушать книгу (прямо сейчас!)

Просто открой `audio-player.html` в браузере и нажми "ВЕСЬ ФИЛЬМ"!

### 2. Озвучка

```bash
pip install edge-tts
python3 tools/tts_generator.py
```

### 3. Картинки

Используй промпты из `visual/art_queue.csv` в:
- Midjourney
- Leonardo.ai
- Stable Diffusion

### 4. Монтаж

Склей в DaVinci Resolve или Final Cut Pro.

## Автор

- Telegram: @your_telegram
- GitHub: github.com/hoOJluGun

## Лицензия

MIT
