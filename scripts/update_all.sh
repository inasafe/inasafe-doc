#!/bin/bash

git pull
./scripts/gen_rst
./scripts/pre_translate.sh
./scripts/create-transifex-resources.sh
./scripts/post_translate.sh 
