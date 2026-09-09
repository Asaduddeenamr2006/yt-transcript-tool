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
* Works on Linux, macOS, and Windows

## Installation

### With pipx (recommended)

One command, straight from GitHub — no cloning needed:

```bash
pipx install git+https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
```

Don't have `pipx`? Follow the [pipx installation guide](https://pipx.pypa.io/latest/installation/), then run the command above.

### With uv

```bash
uv tool install git+https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
```

### With pip

Inside a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

pip install git+https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
```

### From a cloned repository

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool

pipx install .
```

### Update

```bash
pipx upgrade yttext
```

### Uninstall

```bash
pipx uninstall yttext
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

Specify a preferred transcript language:

```bash
yttext "VIDEO_URL" --language en
```

Multiple languages can be specified:

```bash
yttext "VIDEO_URL" --language en --language ar
```

### Choose an output file

Save the transcript to a specific location:

```bash
yttext "VIDEO_URL" --output ~/Downloads/transcript.txt
```

### Save as JSON

```bash
yttext "VIDEO_URL" --format json
```

### Disable timestamps

By default, TXT transcripts include timestamps. To disable them:

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

## How It Works

`yttext` uses the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) library to retrieve available transcripts from YouTube videos.

The tool processes the transcript and saves it in the selected output format.

## Error Handling

If a transcript cannot be retrieved, the CLI prints possible reasons, such as:

* The video does not have an available transcript.
* The selected language is unavailable.
* YouTube changed something that affects transcript access.

You can try another language with:

```bash
yttext "VIDEO_URL" --language LANGUAGE
```

## Requirements

* Python 3.9+ (handled automatically by pipx or uv)
* youtube-transcript-api (installed automatically)

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
├── pyproject.toml
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.
