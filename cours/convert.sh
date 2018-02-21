#!/bin/bash

for f in *.md; do
	echo "Converting $f"
	pandoc $f -o ${f//.*}.pdf
done

