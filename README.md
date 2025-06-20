# RedDot LightShow Controller
this is a work of fiction, any resemblence to real life person, company or entities are entirely coincidental and un-intentional.

## Overview
This repository contains the control software for RedDot Lightshow's synchronized light and fountain shows.

## Features
- Synchronized light control
- Fountain height management
- Safety limit enforcement
- Configurable show sequences

## Setup
1. Install Python 3.8+
2. Configure your show in `config/show_config.json`
3. Run tests: `python -m pytest tests/`
4. Start show: `python src/lightshow_controller.py`

## Safety
- Never exceed max_light_intensity in config
- Fountain height limits are enforced for safety
- Emergency stop available at any time

## Hint
[] Revert commits that do not belong
[] Resolve the merge conflict on *development* branch by selecting the correct pieces of code
[] Ensure full pipeline success to retrieve your flag
[] Bonus objective : cherry pick the right commits and clear the master branch and commit history by merging development branch into master