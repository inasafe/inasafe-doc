#!/bin/bash

git pull
tx pull
./scripts/gen_rst_script.py
./scripts/gen_impfunc_doc.py
./scripts/pre_translate.sh
./scripts/create-transifex-resources.sh
./scripts/post_translate.sh 
