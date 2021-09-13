#!/bin/bash
docker build -t sb-exec:latest .
if [ $# -ne 1 ]; then
    echo "test case file is required"
    exit 1
fi
docker run --rm -ti -v $(pwd)/credentials.txt:/app/credentials.txt -v $(pwd)/testcases:/app/testcases sb-exec $1