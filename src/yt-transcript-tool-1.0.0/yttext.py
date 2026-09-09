#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(value: str) -> str:
    """Extract a YouTube video ID from a URL or accept a raw video ID."""
    value = value.strip()

    # Raw YouTube video ID
    if re.fullmatch(r"[\w-]{11}", value):
        return value

    parsed = urlparse(value)
    hostname = (parsed.hostname or "").lower()

    # https://youtu.be/VIDEO_ID
    if hostname in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.strip("/").split("/")[0]

        if video_id:
            return video_id

    # youtube.com URLs
    if hostname.endswith("youtube.com"):

        # https://www.youtube.com/watch?v=VIDEO_ID
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [None])[0]

            if video_id:
                return video_id

        # https://www.youtube.com/shorts/VIDEO_ID
        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/shorts/", 1)[1].split("/", 1)[0]

        # https://www.youtube.com/embed/VIDEO_ID
        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/embed/", 1)[1].split("/", 1)[0]

    raise ValueError("Could not find a valid YouTube video ID.")


def format_timestamp(seconds: float) -> str:
    """Convert seconds into HH:MM:SS or MM:SS."""
    total_seconds = max(0, int(seconds))

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return f"{minutes:02d}:{seconds:02d}"


def clean_text(text: str) -> str:
    """Normalize whitespace."""
    return " ".join(text.split())


def fetch_transcript(
    video_id: str,
    languages: list[str],
    preserve_formatting: bool = False,
):
    """Fetch a transcript using youtube-transcript-api."""
    api = YouTubeTranscriptApi()

    return api.fetch(
        video_id,
        languages=languages,
        preserve_formatting=preserve_formatting,
    )


def save_txt(
    transcript,
    output_file: Path,
    timestamps: bool = True,
):
    """Save transcript as a TXT file."""
    lines = []

    for entry in transcript:
        text = clean_text(entry.text)

        if not text:
            continue

        if timestamps:
            timestamp = format_timestamp(entry.start)
            lines.append(f"[{timestamp}] {text}")
        else:
            lines.append(text)

    output_file.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def save_json(transcript, output_file: Path):
    """Save transcript as JSON."""
    data = []

    for entry in transcript:
        data.append(
            {
                "text": entry.text,
                "start": entry.start,
                "duration": entry.duration,
            }
        )

    output_file.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def build_parser():
    parser = argparse.ArgumentParser(
        prog="yttext",
        description="Download and save YouTube video transcripts.",
    )

    parser.add_argument(
        "video",
        help="YouTube URL or 11-character video ID",
    )

    parser.add_argument(
        "-l",
        "--language",
        action="append",
        dest="languages",
        help=(
            "Preferred transcript language. "
            "Can be used multiple times."
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file path.",
    )

    parser.add_argument(
        "--format",
        choices=["txt", "json"],
        default="txt",
        help="Output format. Default: txt",
    )

    parser.add_argument(
        "--no-timestamps",
        action="store_true",
        help="Do not include timestamps in TXT output.",
    )

    parser.add_argument(
        "--preserve-formatting",
        action="store_true",
        help="Preserve supported HTML formatting.",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        video_id = extract_video_id(args.video)

        languages = args.languages or ["en"]

        print(f"Video ID: {video_id}")
        print(f"Languages: {', '.join(languages)}")
        print("Fetching transcript...")

        transcript = fetch_transcript(
            video_id=video_id,
            languages=languages,
            preserve_formatting=args.preserve_formatting,
        )

        # Determine output file
        if args.output:
            output_file = Path(args.output)
        else:
            extension = "json" if args.format == "json" else "txt"

            output_file = Path(
                f"{video_id}_transcript.{extension}"
            )

        # Create parent directory if needed
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Save transcript
        if args.format == "json":
            save_json(
                transcript,
                output_file,
            )
        else:
            save_txt(
                transcript,
                output_file,
                timestamps=not args.no_timestamps,
            )

        print(f"Transcript saved to: {output_file}")

        return 0

    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    except Exception as error:
        print(
            f"Failed to fetch transcript: {error}",
            file=sys.stderr,
        )

        print(
            "\nPossible reasons:",
            file=sys.stderr,
        )

        print(
            "- The video does not have an available transcript.",
            file=sys.stderr,
        )

        print(
            "- The selected language is unavailable.",
            file=sys.stderr,
        )

        print(
            "- YouTube changed something that affects transcript access.",
            file=sys.stderr,
        )

        print(
            "\nTry another language using --language.",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
