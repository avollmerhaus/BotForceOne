BotForceOne
===

Just another irc bot.
Based on the python [irc3 library](https://github.com/gawel/irc3)

Copy and review example config, then run the bot using either the dev or prod methods.

## Dev environment

### Using poetry
If poetry is not packaged for your environment, you can run it from a virtualenv.

The next 2 sections assume your shell is at the repo root.

#### Installation
```shell
poetry install
```

This will create a new virtualenv as a subfolder of `~/.cache/pypoetry/virtualenvs/`.
Sources from the repo are included dynamically in the virtualenv, so you can edit your code without re-creating the virtualenv.

#### Running the bot
```shell
poetry run irc3 config.ini
```

## Prod environment

FIXME: add documentation
