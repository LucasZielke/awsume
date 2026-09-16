# Installation and Quick Start

## Pre-Requisites

- Awsume requires Python 3.5 or greater.
- Awsume can be installed via pip, so make sure that the location that pip installs binaries is included on your `PATH` environment variable.

## Installation

::: warning
Homebrew is not an officially supported method of installing awsume
:::

The officially-recommended way to install awsume is via [pipx](https://pypa.github.io/pipx/)

Awsume can be installed via one of the following commands:

```
pipx install awsume
pip install awsume
```

### Extra Features

Awsume uses Python's [extras_require](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies) to add additional functionality with different dependencies.

- `awsume[saml]` - Install dependencies required to support SAML assertion handling
- `awsume[fuzzy]` - Install dependencies required to support fuzzy profile name matching
- `awsume[console]` - Install the [awsume-console-plugin](https://github.com/trek10inc/awsume-console-plugin) with awsume

## Alias Setup

If you're running on a unix-like system, you must have an alias setup for awsume, that may or may not look something like this:

```bash
alias awsume=". awsume"
```

After installing awsume, run `awsume-configure` to add this alias (and the
autocomplete script) to your shell's login file, such as `~/.bash_profile`,
`~/.bashrc`, `$ZDOTDIR/.zshenv`, your fish functions, or your PowerShell
profile:

```bash
awsume-configure
```

Once it finishes, restart your terminal or re-source your login file.

`awsume-configure` will detect your installed shells automatically. To target
a specific shell instead, pass `--shell`, e.g. `awsume-configure --shell bash`.
You can skip the alias setup by setting `AWSUME_SKIP_ALIAS_SETUP` in your
environment. If you'd rather configure things by hand, add the alias yourself
and see the `awsume-configure` guide [here](../utilities/awsume-configure.md)
for the details of each component.

## Quick Usage

Once you have your alias setup, awsume can now work.

Run the following command and you'll be able to execute commands and run scripts with that profile's credentials.

```bash
awsume <profile_name>
```

Read more about awsume's usage [here](./usage.md).
