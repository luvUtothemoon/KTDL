import sys

def normalize(_file, attribute, method, new_file):
    # Read CSV file
    values = []
    with open(_file, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            value = line.strip().split(',')[attribute]
            if value == '':
                value = '0'
            values.append(float(value))

    # Normalize the attribute
    if method == 'min-max':
        # Min-max normalization
        minVal = min(values)
        maxVal = max(values)
        normalizedVal = [(x - minVal) / (maxVal - minVal) for x in values]
    elif method == 'z-score':
        # Z-score normalization
        mean = sum(values) / len(values)
        std_dev = (sum([(x - mean) ** 2 for x in values]) / len(values)) ** 0.5
        normalizedVal = [(x - mean) / std_dev for x in values]
    else:
        raise ValueError('Unknown normalization method')

    # Save the result to the result file
    with open(new_file, 'w') as f:
        f.write(','.join(header) + '\n')  # Unchange the header
        for i, line in enumerate(lines[1:]):
            fields = line.strip().split(',')
            fields[attribute] = str(normalizedVal[i])
            f.write(','.join(fields) + '\n')
            
normalize(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])

print("Successfull!!")
