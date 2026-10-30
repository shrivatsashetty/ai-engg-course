# uv 

An extremely fast Python package and project manager, written in Rust.

## References:
* [uv docs](https://docs.astral.sh/uv/)
* [uv environment guides](https://tiangolo.com/guides/virtual-environments/)

## Installation

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Projects

uv manages project dependencies and environments, with support for lockfiles, workspaces, and more, similar to rye or poetry:

```sh
# The uv init command initializes a new Python project in the specified directory by creating the necessary configuration files and structure to get started.
uv init example

cd example

# Install `ruff` package
# Python linter and code formatter written in Rust
# In the Projects section, it is used alongside uv to automatically check Python code for errors and stylistic issues (uv run ruff check).
uv add ruff

# run fuff checks
uv run ruff check

# The uv lock command generates or updates the project's lockfile (which locks down the exact dependency versions to ensure reproducible builds across environments) based on the dependencies declared in your project configuration. Equivalent to `package-lock.json` in Node.js projects.
uv lock

# The uv sync command updates the project's local environment (virtual environment) to match the exact locked dependencies specified in the lockfile, installing any missing packages or removing unneeded ones. Equivalent to the `npm init` command used in Node.js projects
uv sync
```

