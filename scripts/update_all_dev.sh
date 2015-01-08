#!/bin/bash

git pull
tx pull
./scripts/create_impact_function_docs.py
./scripts/pre_translate.sh
./scripts/pre_translate.sh en
./scripts/create_transifex_resources.sh
./scripts/post_translate.sh
