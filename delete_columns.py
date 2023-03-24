import sys

def delete_cols_with_missing_values(filename, threshold_pct):
    # Read the file contents into a list of lists
    with open(filename) as f:
        lines = f.readlines()

    contents = []
    for line in lines:
        contents.append(line.strip().split(','))

    # Determine the number of rows and columns in the sheet
    num_rows = len(contents)
    num_cols = len(contents[0])

    # Calculate the threshold number of missing values
    threshold = int(num_rows * threshold_pct)

    # Delete any columns that contain more than the threshold number of missing values
    filtered_contents = []
    for i in range(num_cols):
        col_data = [row[i] for row in contents]
        num_missing = col_data.count('')
        if num_missing <= threshold:
            filtered_contents.append(col_data)

    # Transpose the filtered contents to get the columns back into rows
    filtered_contents = [list(x) for x in zip(*filtered_contents)]

    # Write the filtered contents back to the file
    with open(filename, 'w') as f:
        for row in filtered_contents:
            f.write(','.join(row) + '\n')

delete_cols_with_missing_values(sys.argv[1], sys.argv[2])