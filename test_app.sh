#!/bin/bash

set -e

echo "Running test.."

curl -s -f http://192.168.57.17:5000/ || { echo "/endpoint failed"; exit 1; }


echo "All endpoints responded successfully!"

