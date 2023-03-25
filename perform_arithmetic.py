import sys

def convert_to_number(value):
    if value is None or value == '':
        return 0.0
    else:
        return float(value)
    
def perform_arithmetic(filename, attr1_index, attr2_index, operation, newFile):
    # Read the CSV file and extract the attribute values
    rows = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            row = line.strip().split(',')
            rows.append(row)

    # Perform the arithmetic operation on the attributes
    results = []
    for i in range(1, len(rows)):
        attr1 = convert_to_number(rows[i][attr1_index])
        attr2 = convert_to_number(rows[i][attr2_index])

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

    with open(newFile, 'w') as f:
        # Write the result rows
        for i, row in enumerate(rows[1:]):
            f.write(str(results[i]) + '\n')

perform_arithmetic(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5])