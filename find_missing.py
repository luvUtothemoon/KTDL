import sys

def find_missing_values_of_columns(file):
    with open(file, 'r') as f:
        # đọc dữ liệu từ tệp CSV
        lines = f.readlines()
        header = lines[0].strip().split(',')
        numCol = len(header)

        # tìm cột có giá trị missing values
        missing_value_columns = []
        for i in range(numCol):
            colVal = [line.strip().split(',')[i] for line in lines[1:]]
            if '' in colVal:
                missing_value_columns.append(header[i])

    return missing_value_columns
find_missing_values_of_columns(sys.argv[1])