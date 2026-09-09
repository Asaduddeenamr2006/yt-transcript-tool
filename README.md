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

## Requirements

* Python 3.9 or newer
* Git
* pipx **or** Python `venv`

## Installation

### Option 1 — Using pipx (Recommended)

`pipx` installs the application in an isolated Python environment while making the `yttext` command available globally.

First, install `pipx` using your distribution's package manager or follow the official pipx installation instructions.

Then clone the repository:

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool
```

Install `yttext`:

```bash
pipx install .
```

After installation:

```bash
yttext --help
```

### Option 2 — Using a Python virtual environment

If you don't have `pipx`, you can use Python's built-in virtual environment support.

Clone the repository:

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the package:

```bash
python -m pip install .
```

The `yttext` command is now available while the virtual environment is active.

Test the installation:

```bash
yttext --help
```

To leave the virtual environment:

```bash
deactivate
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

By default, TXT transcripts include timestamps.

To disable them:

```bash
yttext "VIDEO_URL" --no-timestamps
```

### Preserve formatting

```bash
yttext "VIDEO_URL" --preserve-formatting
```

## Examples

Fetch an English transcript:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID" --language en
```

Fetch an Arabic transcript:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID" --language ar
```

Save as JSON:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID" --format json
```

Save to a custom location without timestamps:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID" \
    --output ~/Documents/transcript.txt \
    --no-timestamps
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

`yttext` uses the `youtube-transcript-api` Python library to retrieve available transcripts from YouTube videos.

The tool processes the transcript and saves it in the selected output format.

## Error Handling

If a transcript cannot be retrieved, the CLI provides possible reasons, such as:

* The video does not have an available transcript.
* The selected language is unavailable.
* YouTube changed something that affects transcript access.

You can try another language with:

```bash
yttext "VIDEO_URL" --language LANGUAGE
```

## Development

Clone the repository:

```bash
git clone https://github.com/Asaduddeenamr2006/yt-transcript-tool.git
cd yt-transcript-tool
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

Run the CLI:

```bash
yttext "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Project Structure

```text
yt-transcript-tool/
├── yttext/
│   ├── __init__.py
│   └── cli.py
├── yttext.py
├── PKGBUILD
├── .SRCINFO
├── pyproject.toml
├── LICENSE
├── README.md
└── .gitignore
```

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.

## Repository

GitHub:

https://github.com/Asaduddeenamr2006/yt-transcript-tool
