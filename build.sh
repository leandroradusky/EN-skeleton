#!/bin/bash
set -eo pipefail

# This will load the script from this repository. Make sure to point to a specific commit so the build continues to work
# event if breaking changes are introduced in this repository
source <(curl -s https://raw.githubusercontent.com/matiasgarciaisaia/ci-docker-builder/4c399de5c7d7c761ea7e5d88e08f9d078da820de/build.sh)

# Prepare the build
dockerSetup

# Write a VERSION file for api exposure
echo $VERSION > VERSION

# Build and push the Docker image
dockerBuildAndPush -d backend
