#!/bin/bash

git pull
tx pull
./scripts/create_api_docs.py $HOME/dev/python/inasafe
./scripts/create_impact_function_docs_stable.py
./scripts/pre_translate_stable.sh en id
./scripts/post_translate_stable.sh
