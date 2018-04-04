#!/bin/bash
# print all allowed methods
curl -s -I $1 | awk '{if(/Allow:/) print substr($0, index($0,$2))}'
