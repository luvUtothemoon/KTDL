import sys

def count_lines_missing_data(_file):
    # read CSV file
    with open(_file, 'r') as f:
        lines = f.readlines()
        # count missing values
        num = 0
        for line in lines[1:]:
            if ',' not in line:
                continue
            value = line.strip().split(',')
            if '' in value:
                num += 1
    return num

print(count_lines_missing_data(sys.argv[1]))
