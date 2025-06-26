# Display the total number of rows (excluding header)
tail -n +2 output.csv | wc -l

# Display the first 5 rows (excluding header)
tail -n +2 output.csv | head -5

# Display the frequency/count of each unique value in the third column (excluding header)
tail -n +2 output.csv | cut -d',' -f2 | sort | uniq -c | sort -nr

# Extract rows where the value in the third column equals "VALUE" (replace VALUE as needed)
awk -F',' '$2=="VALUE"' output.csv

# Display the header row
head -1 output.csv
