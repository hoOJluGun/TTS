import os
import re
import asyncio
import argparse
from pathlib import Path

from telethon import TelegramClient
from telethon.errors import UserAlreadyParticipantError
from telethon.tl.functions.channels import JoinChannelRequest


def parse_channel_identifier(raw: str) -> str:
    """
    Accepts '@user', 'user', 'https://t.me/user', or invite link, and normalizes.
    Returns a string suitable for Telethon's get_entity/join.
    """
    raw = raw.strip()
    # t.me links
    m = re.match(r"https?://t\.me/(.+)", raw)
    if m:
        return m.group(1)
    # @username
    if raw.startswith("@"):
        return raw[1:]
    return raw


async def ensure_joined(client: TelegramClient, channel: str, try_join: bool) -> object:
    entity = await client.get_entity(channel)
    # Optionally attempt to join public channels
    if try_join:
        try:
            await client(JoinChannelRequest(entity))
        except UserAlreadyParticipantError:
            pass
        except Exception:
            # Joining might fail for private/invite-only channels; ignore
            pass
    return entity


async def export_channel_messages(
    channel: str,
    output_path: Path,
    separator: str = "\n\n",
    include_meta: bool = False,
    try_join: bool = False,
):
    api_id = int(os.environ.get("TELEGRAM_API_ID", "0"))
    api_hash = os.environ.get("TELEGRAM_API_HASH")
    session = os.environ.get("TELEGRAM_SESSION", "telegram_session")

    if not api_id or not api_hash:
        raise SystemExit(
            "Missing TELEGRAM_API_ID/TELEGRAM_API_HASH env vars. Get them from https://my.telegram.org"
        )

    channel_norm = parse_channel_identifier(channel)

    # Create parent dirs
    output_path.parent.mkdir(parents=True, exist_ok=True)

    async with TelegramClient(session, api_id, api_hash) as client:
        entity = await ensure_joined(client, channel_norm, try_join)

        # Write progressively to avoid high memory usage
        count = 0
        with output_path.open("w", encoding="utf-8") as f:
            async for msg in client.iter_messages(entity, reverse=True):  # oldest -> newest
                text = msg.message or ""
                if not text:
                    # Fallback to caption if any
                    if getattr(msg, "caption", None):
                        text = msg.caption or ""
                if not text:
                    # Skip non-text messages
                    continue
                if include_meta:
                    meta = f"[id:{msg.id} | date:{msg.date.isoformat()}]"
                    f.write(meta + "\n")
                f.write(text)
                f.write(separator)
                count += 1
                if count % 500 == 0:
                    print(f"Wrote {count} messages so far…")

        print(f"Done. Wrote {count} messages to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Export all text messages from a Telegram channel to a single Markdown file"
        )
    )
    parser.add_argument(
        "channel",
        help="Channel username, @username, https://t.me/username, or invite link",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="channel_export.md",
        help="Output Markdown file path (default: channel_export.md)",
    )
    parser.add_argument(
        "--separator",
        default="\n\n",
        help="Text separator to insert between messages (default: blank line)",
    )
    parser.add_argument(
        "--include-meta",
        action="store_true",
        help="Prepend each message with basic metadata (id, date)",
    )
    parser.add_argument(
        "--try-join",
        action="store_true",
        help="Attempt to join the channel first (public channels only)",
    )

    args = parser.parse_args()

    output_path = Path(args.output)
    asyncio.run(
        export_channel_messages(
            channel=args.channel,
            output_path=output_path,
            separator=args.separator,
            include_meta=args.include_meta,
            try_join=args.try_join,
        )
    )


if __name__ == "__main__":
    main()

