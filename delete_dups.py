import sys


def delete_duplicates(_file, new_file):
    # Open CSV file
    with open(_file, 'r') as _file:
        data = _file.read()

    # Split the data
    rows = data.split('\n')
    # Save the header
    header_row = rows[0]
    # store unique rows into set()
    unique_rows = set()

    # Examinate all splited row
    for row in rows[1:]:
        # Check if the row is not empty
        if row:
            # Add the row to the set
            unique_rows.add(row)

    # Join the header
    unique_data = header_row + '\n' + '\n'.join(unique_rows)
    # Save the result into the result file
    with open(new_file, 'w') as file:
        file.write(unique_data)


delete_duplicates(sys.argv[1], sys.argv[2])
print("Successfull!!")
