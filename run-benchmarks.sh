#!/usr/bin/env bash

programs=(binary-trees fannkuch-redux fasta regex-redux spectral-norm)

if [[ "$1" == "--large-args" ]]; then
    args=(21 12 25000000 "< rr-input5000000.txt" 5500)
elif [[ "$#" -eq 0 ]]; then
    args=(10 7 1000 "< rr-input1000.txt" 100)
else
    echo "Invalid arguments"
    exit 1
fi

mkdir -p benchmarks/json

for i in {0..4}; do
    hyperfine -r 50 -w 10 "hush src/hush/${programs[i]}.hsh ${args[i]}" "python src/python/${programs[i]}.py ${args[i]}" --export-json benchmarks/json/${programs[i]}.json
done
