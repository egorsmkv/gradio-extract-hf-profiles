import gradio as gr

from bs4 import BeautifulSoup

# Config
concurrency_limit = 5

# Load model
title = "Extract HF profiles from HTML snippet"

description_head = f"""
# {title}

## Overview

This space is a simple helper to parse HTML snippet to extract HF profiles.
""".strip()


def inference(text, progress=gr.Progress()):
    if not text:
        raise gr.Error("Please paste your HTML snippet.")

    gr.Info("Starting working", duration=2)

    soup = BeautifulSoup(text, features="html.parser")

    progress(0, desc="Working...")

    links = []

    for item in progress.tqdm(soup.find_all('a')):
        div_class = ' '.join(item.get('class'))
        if div_class == 'flex items-center gap-2':
            links.append(item)

    profiles = {}
    for link in links:
        hf_url = f'https://huggingface.co{link["href"]}'
        profile_name = link.text.replace('· ', '').strip()

        profiles[profile_name] = hf_url

    results = []

    for profile_name, hf_url in profiles.items():
        results.append(hf_url)

    result = '\n'.join(results)

    gr.Info("Finished!", duration=2)

    return result


demo = gr.Blocks(
    title=title,
    analytics_enabled=False,
    theme=gr.themes.Base(),
)

with demo:
    gr.Markdown(description_head)

    gr.Markdown("## Usage")

    result_text = gr.Textbox(
        label="Links",
        lines=5,
    )

    text = gr.Textbox(label="HTML", autofocus=True)

    gr.Button("Extract").click(
        inference,
        concurrency_limit=concurrency_limit,
        inputs=text,
        outputs=result_text,
    )

if __name__ == "__main__":
    demo.queue()
    demo.launch()
