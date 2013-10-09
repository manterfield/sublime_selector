from __future__ import unicode_literals
import re


ALPHA_NUM = 'alphanumeric'
TITLIFY = 'title'
SLUGIFY = 'slugify'
WRAP = 'wrap'
CLASSIFY = 'class'


def alpha_num(text):
    """Remove non alphanumeric characters from the text."""
    return re.sub(r'[^a-zA-Z0-9]', '', text)


def slugify(text):
    """Prepare string for use as a URL."""
    slug = re.sub(r'[^a-z0-9]', '-', text.lower())
    return re.sub(r'[-]+', '-', slug).strip('-')


def title(text):
    """Convert to title case."""
    return text.title()


def classify(text):
    """Convert string to classname style."""
    class_name = text.title()
    return re.sub(r'[^a-zA-Z0-9]', '', class_name)


def wrap(text, open_tag, close_tag):
    """Wrap the text in tags... or anything really."""
    return ''.join((open_tag, text, close_tag, ))