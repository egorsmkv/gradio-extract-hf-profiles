---
title: Extract HF profiles
emoji: 🛠️
colorFrom: green
colorTo: gray
sdk: docker
app_file: app.py
pinned: false
sdk_version: 4.39.0
---

## Install

```shell
uv venv --python 3.10

source .venv/bin/activate

uv pip install -r requirements.txt

# in development mode
uv pip install -r requirements-dev.txt
```

## Build image

```shell
docker build -t extract-hf-profiles .
```

## Run

```shell
docker run -it --rm -p 8888:7860 extract-hf-profiles
```
