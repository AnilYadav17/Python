"""
Text transformation and normalization routines.
"""

import re
import unicodedata


def camel_to_snake(text: str) -> str:
    """Convert camelCase or PascalCase string to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", text)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def snake_to_camel(text: str, pascal: bool = False) -> str:
    """Convert snake_case string to camelCase or PascalCase."""
    components = [c for c in text.split("_") if c]
    if not components:
        return ""
    if pascal:
        return "".join(x.capitalize() for x in components)
    return components[0] + "".join(x.capitalize() for x in components[1:])


def slugify(text: str) -> str:
    """Normalize string, remove non-ASCII characters, and convert spaces/symbols to hyphens."""
    # Normalize unicode (NFKD decomposes accents)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Lowercase and replace non-alphanumeric characters with a single hyphen
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[-\s]+", "-", text)


def truncate_words(text: str, num_words: int, suffix: str = "...") -> str:
    """Truncate text after a given number of words, appending suffix if truncated."""
    words = text.split()
    if len(words) <= num_words:
        return text
    return " ".join(words[:num_words]) + suffix
