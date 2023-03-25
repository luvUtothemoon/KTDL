import sys

def normalize_csv3(filename, attribute_index, method, newfile):
    # Read the CSV file and extract the attribute values
    values = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            value = line.strip().split(',')[attribute_index]
            if value == '':
                value = '0'
            values.append(float(value))

    # Normalize the attribute using the chosen method
    if method == 'min-max':
        # Min-max normalization: (x - min) / (max - min)
        min_value = min(values)
        max_value = max(values)
        normalized_values = [(x - min_value) / (max_value - min_value) for x in values]
    elif method == 'z-score':
        # Z-score normalization: (x - mean) / std_dev
        mean = sum(values) / len(values)
        std_dev = (sum([(x - mean) ** 2 for x in values]) / len(values)) ** 0.5
        normalized_values = [(x - mean) / std_dev for x in values]
    else:
        raise ValueError('Unknown normalization method')

    # Write the normalized values back to the CSV file
    with open(newfile, 'w') as f:
        f.write(','.join(header) + '\n')  # write the header row unchanged
        for i, line in enumerate(lines[1:]):
            fields = line.strip().split(',')
            fields[attribute_index] = str(normalized_values[i])
            f.write(','.join(fields) + '\n')
            
normalize_csv3(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])

print("Successfull!!")
