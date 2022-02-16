#!/bin/bash -e

# set color variables
COLOR_REST="$(tput sgr0)"
COLOR_GREEN="$(tput setaf 2)"
COLOR_MAGENTA="$(tput setaf 5)"
COLOR_LIGHT_BLUE="$(tput setaf 81)"

# Set up precommit hooks (this actually needs to happen outside of docker!)
echo "$COLOR_LIGHT_BLUE 🧑‍🔧 Setting up pre-commit... $COLOR_REST"
pip3 install --upgrade pip
pip3 install pre-commit
pre-commit install -f
echo "$COLOR_LIGHT_BLUE ✨ pre-commit is now configured! $COLOR_REST"

echo "$COLOR_LIGHT_BLUE 🧑‍🔧 Building Docker images... $COLOR_REST"
docker-compose build
echo "$COLOR_LIGHT_BLUE ✨ 🐳 Docker images built! $COLOR_REST"
