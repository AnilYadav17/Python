"""
Validation routines for common data formats.
"""

import re
from urllib.parse import urlparse

# RFC 5322 compliant simplified regex pattern
EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)
SLUG_REGEX = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def is_valid_email(email: str) -> bool:
    """Return True if email string matches standard email formatting."""
    if not isinstance(email, str) or len(email) > 320:
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str, require_scheme: bool = True) -> bool:
    """Return True if URL is syntactically valid with HTTP/HTTPS scheme."""
    if not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url.strip())
        if require_scheme:
            return parsed.scheme in ("http", "https") and bool(parsed.netloc)
        return bool(parsed.netloc or parsed.path)
    except ValueError:
        return False


def is_valid_slug(slug: str) -> bool:
    """Return True if slug contains only lowercase alphanumeric characters and single hyphens."""
    if not isinstance(slug, str) or not slug:
        return False
    return bool(SLUG_REGEX.match(slug))
