# Contributing to this Project

- [Contributing to this Project](#contributing-to-this-project)
  - [Installing/Updating Dependencies](#installingupdating-dependencies)

## Installing/Updating Dependencies

This project uses a pyproject.toml with pinned versions. That being said usually when we're running our automated actions they use the included `requirements.txt`.

To update version use the command: `python -m piptools compile --ugrade --extra dev`
