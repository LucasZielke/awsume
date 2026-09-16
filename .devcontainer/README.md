# Dev Container

A minimal development container for awsume, built around
[uv](https://docs.astral.sh/uv/).

## What you get

- Python 3.11 (matches the project's minimum supported version)
- `uv` for dependency management, builds, and running tasks
- The AWS CLI
- VS Code set up with the Python and Ruff extensions, pytest test
  discovery, and format-on-save via Ruff

## Usage

Open the repository in VS Code and choose **Reopen in Container** (or use
the Dev Containers CLI). On first create, the container runs:

```
uv sync --all-extras --dev
```

which installs awsume (editable) plus the dev tooling into `.venv`.

Common commands:

```bash
uv run pytest test            # run the test suite
uv run ruff check .           # lint
uv run ruff format .          # format
uv build                      # build sdist + wheel
```

## Using your AWS credentials

By default the container does not mount your host AWS credentials, so it
builds cleanly even if you have no `~/.aws` directory. To share them, add a
bind mount to `devcontainer.json`:

```jsonc
"mounts": [
  "source=${localEnv:HOME}/.aws,target=/home/vscode/.aws,type=bind,readonly"
]
```

Or configure credentials inside the container with `aws configure`.
