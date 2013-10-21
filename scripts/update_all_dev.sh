#!/bin/bash

git pull
tx pull
./scripts/create_api_docs.py $HOME/dev/python/inasafe
./scripts/create_impact_function_docs.py $HOME/dev/python/inasafe
./scripts/pre_translate.sh
./scripts/create_transifex_resources.sh
./scripts/post_translate.sh
