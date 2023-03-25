import sys

def find_missing_values_of_columns(_file):
    with open(_file, 'r') as f:
        # read data from file CSV
        lines = f.readlines()
        header = lines[0].strip().split(',')
        numCol = len(header)
        # find column with missing values
        columns = []
        for i in range(numCol):
            colVal = [line.strip().split(',')[i] for line in lines[1:]]
            if '' in colVal:
                columns.append(header[i])

    return columns

print(find_missing_values_of_columns(sys.argv[1]))
