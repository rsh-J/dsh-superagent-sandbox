"""Small string helpers, used as a work item for the sandbox agent."""

import re

_NON_SLUG_CHARS = re.compile(r"[^a-z0-9]+")


def slugify(title: str) -> str:
    """Turn a title into a lowercase, hyphen-separated slug.

    Runs of non-alphanumeric characters collapse into a single hyphen, and
    hyphens are never kept at either end.

    >>> slugify("DeepSeek  Harness  rocks!")
    'deepseek-harness-rocks'
    """
    return _NON_SLUG_CHARS.sub("-", title.lower()).strip("-")


def truncate(text: str, limit: int) -> str:
    """Shorten text to at most `limit` characters, ending with an ellipsis when cut.

    >>> truncate("abcdef", 4)
    'abc…'
    >>> truncate("abc", 4)
    'abc'
    """
    if len(text) <= limit:
        return text
    if limit <= 0:
        return ""
    return text[:limit - 1] + "…"
