#!/usr/bin/env python3
"""
M9 TTS Generator - Озвучка без API ключей!
Использует Edge TTS (бесплатно, без регистрации)

Установка:
    pip install edge-tts

Запуск:
    python3 tts_generator.py
"""

import asyncio
import csv
import os
import sys
from pathlib import Path

# Русские голоса Edge TTS
RUSSIAN_VOICES = {
    'dmitri': 'ru-RU-DmitryNeural',      # Мужской, теплый
    'svetlana': 'ru-RU-SvetlanaNeural',  # Женский
    'alina': 'ru-RU-AlinaNeural',        # Женский, молодой
}

# Голоса по умолчанию для ролей
ROLE_VOICES = {
    'Narrator': 'ru-RU-DmitryNeural',
    'Zhanna': 'ru-RU-AlinaNeural',
    'Dasha': 'ru-RU-SvetlanaNeural',
    'John': 'ru-RU-DmitryNeural',
    'MasterOfWorld': 'ru-RU-DmitryNeural',
    'Ted': 'ru-RU-DmitryNeural',
}


async def generate_speech(text: str, voice: str, output_file: str):
    """Генерирует речь через Edge TTS"""
    import edge_tts
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"  ✅ Создано: {output_file}")


async def main():
    # Папки
    script_dir = Path(__file__).parent
    queue_file = script_dir / "tts_queue.csv"
    output_dir = script_dir / "audio" / "narration"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not queue_file.exists():
        print(f"❌ Файл не найден: {queue_file}")
        return
    
    print("🎙 M9 TTS Generator (Edge TTS)")
    print("=" * 50)
    
    # Читаем CSV
    with open(queue_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    total = len(rows)
    print(f"📝 Найдено {total} фрагментов для озвучки\n")
    
    # Генерируем
    for i, row in enumerate(rows, 1):
        role = row.get('role', 'Narrator')
        text = row.get('text', '')
        outfile = row.get('outfile', f'part_{i}.wav')
        
        # Выбираем голос
        voice = ROLE_VOICES.get(role, 'ru-RU-DmitryNeural')
        
        output_path = output_dir / outfile
        
        print(f"[{i}/{total}] {role}: {text[:50]}...")
        
        try:
            await generate_speech(text, voice, str(output_path))
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
        
        # Небольшая пауза между запросами
        await asyncio.sleep(0.5)
    
    print("\n" + "=" * 50)
    print(f"✅ Озвучка завершена! Файлы в: {output_dir}")
    print("🎬 Можно приступать к монтажу!")


if __name__ == "__main__":
    asyncio.run(main())
