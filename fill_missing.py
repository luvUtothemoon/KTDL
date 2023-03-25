import sys


def fill_missing_values(_file, method, new_file):
    # read CSV file
    with open(_file, 'r') as f:
        data = [line.strip().split(',') for line in f.readlines()]

    # Find the column are numeric
    attributes = []
    cols = len(data[0])
    for i in range(cols):
        if all([row[i].isdigit() or (row[i][1:].isdigit() and row[i].startswith('-')) for row in data[1:]]):
            attributes.append(i)

    # Calculate mean or median for numeric attribute columns
    val_cols = {}
    for i in attributes:
        val = [float(row[i]) for row in data[1:] if row[i].strip() != '']
        if method == 'median':
            val.sort()
            n = len(val)
            if n % 2 == 0:
                val_cols[i] = (val[n // 2 - 1] + val[n // 2]) / 2
            else:
                val_cols[i] = val[n // 2]
        elif method == 'mean':
            val_cols[i] = sum(val) / len(val)

    # Fill in the mean or median in the blanks
    for i in data[1:]:
        for j in attributes:
            if i[j].strip() == '':
                i[j] = str(val_cols[j])

    with open(_file, 'r') as f:
        a = []
        for line in f:
            a.append(line.strip().split(','))

    # Calculate the mode of the categorical attributes
    mode_cate = {}
    for i in range(len(a[0])):
        val = [row[i] for row in a[1:] if row[i]]
        if val:
            mode = max(set(val), key=val.count)
            mode_cate[i] = mode

    # Fill in the missing values with the corresponding mode value
    for i in a[1:]:
        for j in range(len(i)):
            if not i[j] and j in mode_cate:
                i[j] = mode_cate[j]

    # Write data to CSV file
    with open(new_file, 'w') as f:
        for row in data:
            f.write(','.join(row) + '\n')

    with open(new_file, 'w') as f:
        for row in a:
            f.write(','.join(row) + '\n')


fill_missing_values(sys.argv[1], sys.argv[2], sys.argv[3])
print("Successfull!!")
