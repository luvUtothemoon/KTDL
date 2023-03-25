import sys


def delete_duplicates(file_path, newFile):
    # Open the Excel file
    with open(file_path, 'r') as file:
        # Read the data from the file
        data = file.read()

    # Split the data into rows
    rows = data.split('\n')

    # Save the header row
    header_row = rows[0]

    # Create a set to store the unique rows
    unique_rows = set()

    # Iterate through the rows starting from the second row (to exclude the header)
    for row in rows[1:]:
        # Check if the row is not empty
        if row:
            # Add the row to the set
            unique_rows.add(row)

    # Join the header row and unique rows back together
    unique_data = header_row + '\n' + '\n'.join(unique_rows)

    # Write the unique data back to the file
    with open(newFile, 'w') as file:
        file.write(unique_data)

delete_duplicates(sys.argv[1], sys.argv[2])
print("Successfull!!")
