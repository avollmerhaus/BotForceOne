BotForceOne
===

Just another irc bot.
Based on the python [irc3 library](https://github.com/gawel/irc3)

Review the example config, then run the bot like this:
```shell

```

## Dev environment

### Using poetry
If poetry is not packaged for your environment, you can run it from a virtualenv.

#### Installation
From the repo root:
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
