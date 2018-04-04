#!/bin/bash
# gets body size
curl -s -I $1 | awk '{if(/Content-Length:/) print $2}'
