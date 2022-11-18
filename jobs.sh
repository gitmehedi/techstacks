#!/bin/bash
set -B                  # enable brace expansion
for i in {1..1000}; do
  curl "http://localhost:5500/create-job/job-data-${i}"
done