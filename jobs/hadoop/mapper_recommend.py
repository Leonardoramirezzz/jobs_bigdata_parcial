#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        # Parsear línea CSV
        fields = next(csv.reader([line]))
        recommended = fields[7].strip().lower()  # columna 'recommended'
        if recommended in ['true', 'false']:
            print(f"{recommended}\t1")
    except Exception:
        continue
