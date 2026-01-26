# Executive Education: The New World of AI/ML

This repository is the source for the **Executive Education on AI, Data Science and Machine Learning** site, focused on what leaders need to understand to make good decisions in the **new world shaped by AI/ML**.

The course framing and many of the core ideas are **inspired by Neil D. Lawrence’s book _The Atomic Human_** (especially its emphasis on human limits and strengths: bandwidth, uncertainty, trust, and how we co-adapt with our tools).

- **Website**: built with Jekyll (GitHub Pages style)
- **Course content**: authored in `_lamd/` and compiled into site pages/slides

## What this course is

This is a short, executive-facing course that helps business leaders:

- build a practical mental model of what modern AI/ML can and can’t do
- understand how data quality, governance, privacy, and IP shape outcomes
- spot delivery risks early (teams, incentives, evaluation, project management)
- translate AI capability into strategy, operating model changes, and KPIs

It is explicitly grounded in themes developed in _The Atomic Human_, including:

- **uncertainty**: where models fail, how error propagates, and why governance matters
- **trust**: what you can safely delegate to machines, and what must remain a leadership responsibility
- **intent and incentives**: what systems optimise for vs what organisations *mean*

## Where the materials live

- **Source lectures**: `./_lamd/*.md`
- **Generated lecture pages**: `./_lectures/`
- **Generated slides**: `./slides/`

The `./_lamd/_lamd.yml` file controls paths and build options.

## Local development (website)

From the repo root:

```bash
bundle install
bundle exec jekyll serve
```

Then open the local server URL printed by Jekyll.

## Building course artefacts (lamd pipeline)

The `_lamd/compile.sh` script compiles the lecture stubs listed in `_lamd/lectures.csv`.

### Prerequisites

- `pandoc`
- `inkscape` (for some diagram conversions)
- a working Python (recommended: **Python 3.12**)

### Create a local venv for this repo

```bash
cd .
/opt/homebrew/bin/python3.12 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip setuptools wheel
```

### Install `lamd`

Preferred (from PyPI):

```bash
./.venv/bin/pip install almd
```

If you’re developing against a local checkout instead:

```bash
./.venv/bin/pip install -e ../lawrennd/lamd
```

### Compile the lectures

```bash
cd _lamd
PATH="$(pwd)/../.venv/bin:$PATH" ./compile.sh
```

## License / reuse

Unless otherwise stated in individual files, content is provided for teaching and internal course use; reuse should preserve attribution.

