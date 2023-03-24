import sys


def delete_rows_with_missing_values1(filename, threshold_pct):
    # Read the file contents into a list of lists
    with open(filename) as f:
        lines = f.readlines()

    contents = []
    for line in lines:
        contents.append(line.strip().split(','))

    # Determine the number of columns in the sheet
    num_columns = len(contents[0])

    # Calculate the threshold number of missing values
    threshold = int(num_columns * threshold_pct)

    # Delete any rows that contain more than the threshold number of missing values
    filtered_contents = []
    for row in contents:
        num_missing = row.count('')
        if num_missing <= threshold:
            filtered_contents.append(row)

    # Write the filtered contents back to the file
    with open(filename, 'w') as f:
        for row in filtered_contents:
            f.write(','.join(row) + '\n')


delete_rows_with_missing_values1(sys.argv[1], sys.argv[2])
