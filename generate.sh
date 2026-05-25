#!/usr/bin/env bash
set -e

echo "Running export:swagger in backend..."
cd ../AVCI-CMS-Backend
npm run export:swagger
cd ../avci-cms-sdk-python

echo "Generating Python models from openapi.json..."
poetry run datamodel-codegen --input ../AVCI-CMS-Backend/openapi.json --input-file-type openapi --output avcicms/models.py

echo "Generation complete!"
