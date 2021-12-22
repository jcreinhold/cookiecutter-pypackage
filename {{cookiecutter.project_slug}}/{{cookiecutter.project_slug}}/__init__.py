"""Top-level package for {{ cookiecutter.project_name }}."""

import logging

__title__ = "{{ cookiecutter.project_name }}"
__description__ = "{{ cookiecutter.project_short_description }}"
__url__ = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"
__license__ = "{{ cookiecutter.open_source_license }}"
__copyright__ = "Copyright {% now 'local', '%Y' %} {{ cookiecutter.full_name }}"

logging.getLogger(__name__).addHandler(logging.NullHandler())
