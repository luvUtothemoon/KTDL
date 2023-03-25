import sys

def delete_cols_with_missing_values(_file, threshold_pct, new_file):
    # Read file and save to list
    with open(_file) as f:
        rows = f.readlines()
    a = []
    for i in rows:
        a.append(i.strip().split(','))

    # Calculate the threshold number of missing data
    threshold = int(len(a) * threshold_pct)

    # Delete column with missing data exceeding threshold
    res = []
    for i in range(len(a[0])):
        col = [row[i] for row in a]
        missing = col.count('')
        if missing <= threshold:
            res.append(col)

    # Transpose the filtered contents to get the columns back into rows
    res = [list(x) for x in zip(*res)]

    # Write data to CSV file
    with open(new_file, 'w') as f:
        for i in res:
            f.write(','.join(i) + '\n')

print("Successfull!!")

delete_cols_with_missing_values(sys.argv[1], float(sys.argv[2]), sys.argv[3])

