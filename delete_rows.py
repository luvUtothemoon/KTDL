import sys

def delete_rows_with_missing_values(_file, threshold_pct, new_file):
    # Read file and save to list
    with open(_file) as f:
        rows = f.readlines()
    a = []
    for i in rows:
        a.append(i.strip().split(','))

    # Calculate the threshold number of missing data
    threshold = int(len(a[0]) * threshold_pct)

    # Delete row with missing data exceeding threshold
    res = []
    for i in a:
        missing = i.count('')
        if missing <= threshold:
            res.append(i)

    # Write data to CSV file
    with open(new_file, 'w') as f:
        for i in res:
            f.write(','.join(i) + '\n')


delete_rows_with_missing_values(sys.argv[1], float(sys.argv[2]), sys.argv[3])

print("Successfull!!")