import argparse
import os
from pathlib import Path
from typing import List

import requests


API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "meta-llama/llama-3-70b-instruct"
DEFAULT_LANGUAGES = ["de", "en"]


def translate_text(content: str, target_lang: str, model: str, api_key: str) -> str:
    """Translate markdown *content* to *target_lang* using OpenRouter.

    Args:
        content: The markdown content to translate.
        target_lang: Target language code (e.g., 'de', 'en').
        model: OpenRouter model identifier.
        api_key: OpenRouter API key.

    Returns:
        Translated markdown content.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful translator. Translate the user's markdown "
                    "into the requested language while keeping markdown and YAML "
                    "front matter intact."
                ),
            },
            {
                "role": "user",
                "content": f"Translate the following markdown to {target_lang}:\n\n{content}",
            },
        ],
        "temperature": 0.2,
    }
    response = requests.post(API_URL, headers=headers, json=data, timeout=60)
    response.raise_for_status()
    result = response.json()
    return result["choices"][0]["message"]["content"]


def process_file(path: Path, root: Path, languages: List[str], model: str, api_key: str, out_dir: Path) -> None:
    """Translate a single Markdown *path* and write results under *out_dir*.

    Args:
        path: Path to the markdown file to translate.
        root: Root directory of the documentation.
        languages: List of target language codes.
        model: OpenRouter model identifier.
        api_key: OpenRouter API key.
        out_dir: Base output directory for translations.
    """
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(root)
    for lang in languages:
        translated = translate_text(text, lang, model, api_key)
        out_file = out_dir / lang / relative
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(translated, encoding="utf-8")
        print(f"Wrote {out_file}")


def main() -> None:
    """
    Main entry point for translating Markdown documentation using OpenRouter.

    Parses command-line arguments for the translation process, including the input
    directory of Markdown documents, target languages, OpenRouter model, and output
    directory. Then, iterates over the input directory, processing each Markdown file
    using the provided arguments.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Translate Markdown documentation using OpenRouter")
    parser.add_argument("--docs-dir", default="vitepress-atc-docs", help="Directory containing markdown docs")
    parser.add_argument("--languages", default=",".join(DEFAULT_LANGUAGES), help="Comma separated target languages")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenRouter model to use")
    parser.add_argument("--out-dir", default="translated-docs", help="Base output directory for translations")

    args = parser.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    docs_dir = Path(args.docs_dir)
    out_dir = Path(args.out_dir)
    languages = [l.strip() for l in args.languages.split(",") if l.strip()]

    for md_file in docs_dir.rglob("*.md"):
        process_file(md_file, docs_dir, languages, args.model, api_key, out_dir)


if __name__ == "__main__":
    main()