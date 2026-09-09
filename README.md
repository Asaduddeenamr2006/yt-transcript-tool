# yttext

A lightweight command-line tool for fetching and saving YouTube video transcripts.

## Features

* Fetch transcripts from YouTube videos
* Accept YouTube URLs or video IDs
* Support multiple preferred transcript languages
* Save transcripts as TXT or JSON
* Optional timestamps for TXT output
* Optional formatting preservation
* Simple and lightweight CLI

## Installation

### From GitHub

Clone the repository:

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool
```

Install with `pipx`:

```bash
pipx install .
```

Or install with pip:

```bash
pip install .
```

## Usage

Fetch a transcript using a YouTube URL:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID"
```

You can also provide the video ID directly:

```bash
yttext "VIDEO_ID"
```

By default, the transcript is saved as:

```text
VIDEO_ID_transcript.txt
```

## Options

### Choose a language

```bash
yttext "VIDEO_URL" --language en
```

Multiple languages can be specified:

```bash
yttext "VIDEO_URL" --language en --language ar
```

### Choose an output file

```bash
yttext "VIDEO_URL" --output ~/Downloads/transcript.txt
```

### Save as JSON

```bash
yttext "VIDEO_URL" --format json
```

### Disable timestamps

```bash
yttext "VIDEO_URL" --no-timestamps
```

### Preserve formatting

```bash
yttext "VIDEO_URL" --preserve-formatting
```

## Command Reference

```text
yttext VIDEO

-l, --language LANGUAGE
    Preferred transcript language.
    Can be used multiple times.

-o, --output OUTPUT
    Output file path.

--format {txt,json}
    Output format. Default: txt.

--no-timestamps
    Do not include timestamps in TXT output.

--preserve-formatting
    Preserve supported HTML formatting.

-h, --help
    Show help message and exit.
```

## Requirements

* Python 3.9+
* youtube-transcript-api

## Development

Clone the repository:

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

## Project Structure

```text
yt-transcript-tool/
├── yttext/
│   ├── __init__.py
│   └── cli.py
├── yttext.py
├── PKGBUILD
├── pyproject.toml
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.

## Repository

GitHub:

https://github.com/Asaduddeenamr2006/yt-transcript-tool
