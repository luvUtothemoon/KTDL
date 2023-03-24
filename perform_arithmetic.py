import sys


def perform_arithmetic(filename, attr1_index, attr2_index, operation):
    # Read the CSV file and extract the attribute values
    rows = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            row = line.strip().split(',')
            rows.append(row)

    # Perform the arithmetic operation on the attributes
    results = []
    for i in range(1, len(rows)):
        attr1 = float(rows[i][attr1_index])
        attr2 = float(rows[i][attr2_index])

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

    for result in results:
        print(result)


perform_arithmetic(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
