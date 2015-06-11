#!/bin/bash

git pull
tx pull
./scripts/create_api_docs.py $HOME/dev/python/inasafe-dev
./scripts/pre_translate_stable.sh en id
./scripts/post_translate_stable.sh
