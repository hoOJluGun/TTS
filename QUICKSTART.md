# 🎬 M9 PRODUCTION - ИНСТРУКЦИЯ ПО СБОРКЕ

## БЫСТРЫЙ СТАРТ

### 1. Подготовка папок

На рабочем столе создай папку `M9_Movie` и внутри:
```
M9_Movie/
├── audio/
│   ├── narration/    # Озвучка
│   └── music/        # Музыка
├── visual/
│   └── images/       # Картинки
└── export/           # Готовый фильм
```

---

### 2. ОЗВУЧКА (Audio)

**Вариант А: Бесплатно за 10 минут**
1. Открой https://ttsfree.com/text-to-speech/Russian/
2. Скопируй текст из `tts_queue.csv` (колонка `text`)
3. Нажми Convert → Download
4. Сохрани в `audio/narration/`

**Вариант Б: ElevenLabs (качественнее)**
1. Зарегистрируйся https://elevenlabs.io
2. Скопируй API ключ
3. Запусти скрипт `tts_elevenlabs.py` (нужен Python)

**Вариант В: Edge TTS (бесплатно, без регистрации)**
```bash
pip install edge-tts
python3 edge_tts_example.py
```

---

### 3. ВИЗУАЛ (Images)

**Промпты готовы в `visual/art_queue.csv`**

Используй:
1. **Midjourney** (Discord) — лучше всего
2. **Leonardo.ai** — бесплатно
3. **Stable Diffusion** — локально
4. **DALL-E** — через OpenAI

Пример промпта из файла:
```
Vintage 1980s Soviet apartment, Zaporizhzhia, 8th floor, sunlit room, thick carpet, warm afternoon light, nostalgic atmosphere, 35mm film grain, cinematic
```

---

### 4. МУЗЫКА

Бесплатно:
- https://pixabay.com/ru/music/
- https://mixkit.co/free-music/

Скачай:
- 1 intro (короткий)
- 1 основная (спокойная)
- 1 финал (эмоциональная)

---

### 5. МОНТАЖ

Программы:
- **DaVinci Resolve** (бесплатно) ⭐
- **Final Cut Pro** (если есть)
- **iMovie** (встроенный)

**Порядок:**
1. Создай новый проект
2. Импортируй озвучку
3. Добавь картинки (каждая картинка = 5-10 сек)
4. Добавь музыку (уменьши громкость)
5. Экспортируй MP4

---

## ЧТО ВКЛЮЧЕНО

| Файл | Описание |
|------|----------|
| `tts_queue.csv` | Полный текст для озвучки (33 сцены) |
| `roles_map.csv` | Роли и голоса |
| `visual/art_queue.csv` | 20 промптов для AI-картинок |
| `build_m9.sh` | Скрипт проверки системы |

---

## КАК ПОЛУЧИТЬ ГОТОВЫЙ ВИДЕО-РЯД

После генерации картинок и озвучки:

1. Открой DaVinci Resolve
2. Создай timeline 1920x1080
3. Перетащи озвучку на timeline
4. Добавь картинки под озвучку
5. В конце добавь музыку
6. Export → MP4

---

## СРОКИ

| Этап | Время |
|------|-------|
| Озвучка | 30-60 мин |
| Картинки (AI) | 1-2 часа |
| Музыка | 15 мин |
| Монтаж | 1-2 часа |
| **ИТОГО** | **3-5 часов** |

---

## ПОДДЕРЖКА

Если нужна помощь с конкретным этапом — пиши!
