#!/bin/bash

git pull
tx pull
./scripts/create_api_docs.py 
./scripts/create_impact_function_docs.py
./scripts/pre_translate.sh
./scripts/create_transifex_resources.sh
./scripts/post_translate.sh
