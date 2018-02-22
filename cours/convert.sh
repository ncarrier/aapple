#!/bin/bash

for f in *.md; do
	cat $f 
	echo \\newpage
done | pandoc -o apprendre_a_programmer_pour_les_enfants.pdf

