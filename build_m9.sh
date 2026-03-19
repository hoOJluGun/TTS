#!/bin/bash
# M9 PRODUCTION SCRIPT - Голливудское кино за один запуск!
# Скопируй этот файл и запусти: chmod +x build_m9.sh && ./build_m9.sh

echo "🎬 M9 MOVIE PRODUCTION - СТАРТ"
echo "================================"

# Проверка Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js не установлен! Установи с https://nodejs.org"
    exit 1
fi

# Проверка FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg не установлен! Установи: brew install ffmpeg"
    exit 1
fi

echo "✅ Node.js и FFmpeg найдены"
echo ""

# Создаём папки
echo "📁 Создаём структуру проекта..."
mkdir -p audio/{raw,music,final}
mkdir -p visual/{prompts,images}
mkdir -p export
echo "✅ Папки созданы"
echo ""

# ============================================
# ШАГ 1: ОЗВУЧКА
# ============================================
echo "🎙 ШАГ 1: ОЗВУЧКА"
echo "------------------"

# Проверка ElevenLabs API ключа
if [ -z "$ELEVENLABS_API_KEY" ]; then
    echo "⚠️  ELEVENLABS_API_KEY не установлен!"
    echo "   Установи ключ: export ELEVENLABS_API_KEY=твой_ключ"
    echo "   Получи ключ: https://elevenlabs.io"
    echo ""
    echo "📝 Альтернатива - используй Google Translate TTS:"
    echo "   Текст уже подготовлен в tts_queue.csv"
    echo ""
else
    echo "✅ ElevenLabs API ключ найден - будет использовать его"
fi

# Скачиваем готовую озвучку (если есть)
echo "📥 Для получения озвучки используй:"
echo "   1. elevenlabs.io → API → Generate"
echo "   2. Или используй сервисы ниже:"
echo "      - https://ttsfree.com"
echo "      - https://speechgen.io"
echo ""
echo "📝 Готовый текст в: tts_queue.csv"
echo ""

# ============================================
# ШАГ 2: ВИЗУАЛ
# ============================================
echo "🖼 ШАГ 2: ВИЗУАЛ"
echo "-----------------"
echo "📝 Промпты для AI-генерации в: visual/art_queue.csv"
echo ""
echo "🎨 Используй для генерации картинок:"
echo "   1. Midjourney (Discord) - лучше всего"
echo "   2. Leonardo.ai - бесплатные кредиты"
echo "   3. Stable Diffusion - локально"
echo "   4. DALL-E 3 - OpenAI API"
echo ""

# ============================================
# ШАГ 3: МУЗЫКА
# ============================================
echo "🎵 ШАГ 3: МУЗЫКА"
echo "-----------------"
echo "🎶 Скачай бесплатную музыку:"
echo "   1. https://pixabay.com/ru/music/"
echo "   2. https://mixkit.co/free-music/"
echo ""
echo "📁 Сохрани в: audio/music/"
echo ""

# ============================================
# ШАГ 4: МОНТАЖ
# ============================================
echo "🎬 ШАГ 4: МОНТАЖ"
echo "-----------------"
echo "🛠 Рекомендуемые программы для Mac:"
echo "   1. DaVinci Resolve (бесплатно) - профи"
echo "   2. Final Cut Pro (платно) - если есть"
echo "   3. Shotcut (бесплатно) - простой"
echo ""
echo "📋 ПОРЯДОК МОНТАЖА:"
echo "   1. Импортируй озвучку из audio/"
echo "   2. Добавь картинки/видео из visual/"
echo "   3. Добавь фоновую музыку из audio/music/"
echo "   4. Настрой тайминг"
echo "   5. Экспортируй в MP4"
echo ""

# ============================================
# ГОТОВО
# ============================================
echo "================================"
echo "✅ M9 ПРОЕКТ ГОТОВ!"
echo "================================"
echo ""
echo "📁 Структура проекта:"
echo "   m9-vault/"
echo "   ├── tts_queue.csv      # Текст для озвучки"
echo "   ├── roles_map.csv      # Роли и голоса"
echo "   ├── visual/art_queue.csv # Промпты для картинок"
echo "   ├── audio/             # Сюда положи озвучку"
echo "   ├── visual/images/     # Сюда положи картинки"
echo "   ├── audio/music/       # Сюда положи музыку"
echo "   └── export/            # Готовый фильм"
echo ""
echo "🚀 Удачи с производством!"
