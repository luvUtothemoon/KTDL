import sys


def delete_duplicates(file_path):
    # Open the Excel file
    with open(file_path, 'r') as file:
        # Read the data from the file
        data = file.read()

    # Split the data into rows
    rows = data.split('\n')

    # Create a set to store the unique rows
    unique_rows = set()

    # Iterate through the rows
    for row in rows:
        # Check if the row is not empty
        if row:
            # Add the row to the set
            unique_rows.add(row)

    # Join the unique rows back together
    unique_data = '\n'.join(unique_rows)

    # Write the unique data back to the file
    with open(file_path, 'w') as file:
        file.write(unique_data)


delete_duplicates(sys.argv[1])
print("Successfull!!")
