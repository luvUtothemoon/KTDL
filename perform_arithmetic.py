import sys


def convertNum(value):
    if value is None or value == '':
        return 0.0
    else:
        return float(value)


def perform_operation(_file, attribute1, attribute2, operation, new_file):
    # Read CSV file
    rows = []
    with open(_file, 'r') as f:
        for i, line in enumerate(f):
            row = line.strip().split(',')
            rows.append(row)

    # Perform operation
    results = []
    for i in range(1, len(rows)):
        attr1 = convertNum(rows[i][attribute1])
        attr2 = convertNum(rows[i][attribute2])

        if operation == '+':
            result = attr1 + attr2
        elif operation == '-':
            result = attr1 - attr2
        elif operation == '*':
            result = attr1 * attr2
        elif operation == '/':
            result = attr1 / attr2 if attr2 != 0 else 0.0
        else:
            raise ValueError('Unknown arithmetic operation')

        results.append((result))

    with open(new_file, 'w') as f:
        # Save the result in result file
        for i, row in enumerate(rows[1:]):
            f.write(str(results[i]) + '\n')


perform_operation(sys.argv[1], int(sys.argv[2]), int(
    sys.argv[3]), sys.argv[4], sys.argv[5])
print("Successfull!!")
