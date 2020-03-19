#!/bin/bash

BRANCH_REGEX=""
GIT_SSH_COMMAND="ssh -i $PWD/mirror_key"
for repo in repos/*; do
  pushd $repo
  git fetch origin
  git fetch mirror
  git push mirror 
  # Push to origin
  git branch -a | grep -e "$BRANCH_REGEX" | xargs --no-run-if-empty git push origin
  popd
done
