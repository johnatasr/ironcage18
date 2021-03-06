from .base import *  # flake8: noqa

# A custom setting for creating full URLs in links in emails
DOMAIN = 'http://testserver'

# Disable sending Slack messaages in tests
SLACK_BACKEND = 'django_slack.backends.TestBackend'

# Admins for mailing errors to
ADMINS = ['admin@example.com']

# Don't spam logs to the console
LOGGING['loggers']['']['handlers'].remove('console')
