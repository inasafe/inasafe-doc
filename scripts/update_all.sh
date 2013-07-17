#!/bin/bash

git pull
tx pull
./scripts/gen_rst
./scripts/pre_translate.sh
./scripts/create-transifex-resources.sh
./scripts/post_translate.sh 
