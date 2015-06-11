#!/bin/bash

git pull
tx pull
./scripts/pre_translate_stable.sh
./scripts/pre_translate_stable.sh en
./scripts/create_transifex_resources.sh
./scripts/post_translate_stable.sh
