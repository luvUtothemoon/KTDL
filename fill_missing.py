import sys

def fill_missing_values(csv_file, method, new_file):
    # read CSV file
    with open(csv_file, 'r') as f:
        data = [line.strip().split(',') for line in f.readlines()]

    # Tìm các cột là thuộc tính số
    num_cols = len(data[0])
    num_attributes = []
    for col in range(num_cols):
        if all([row[col].isdigit() or (row[col].startswith('-') and row[col][1:].isdigit()) for row in data[1:]]):
            num_attributes.append(col)

    # Tính giá trị trung bình hoặc trung vị cho các cột thuộc tính số
    col_values = {}
    for col in num_attributes:
        values = [float(row[col])
                  for row in data[1:] if row[col].strip() != '']
        if method == 'mean':
            col_values[col] = sum(values) / len(values)
        elif method == 'median':
            values.sort()
            n = len(values)
            if n % 2 == 0:
                col_values[col] = (values[n // 2 - 1] + values[n // 2]) / 2
            else:
                col_values[col] = values[n // 2]

    # Điền giá trị trung bình hoặc trung vị vào các giá trị trống
    for row in data[1:]:
        for col in num_attributes:
            if row[col].strip() == '':
                row[col] = str(col_values[col])

    with open(csv_file, 'r') as f:
        rows = []
        for line in f:
            rows.append(line.strip().split(','))

    # Tính mode của các thuộc tính phân loại
    mode_dict = {}
    for col in range(len(rows[0])):
        values = [row[col] for row in rows[1:] if row[col]]
        if values:
            mode = max(set(values), key=values.count)
            mode_dict[col] = mode

    # Điền các giá trị thiếu bằng giá trị mode tương ứng
    for row in rows[1:]:
        for col in range(len(row)):
            if not row[col] and col in mode_dict:
                row[col] = mode_dict[col]

    # Ghi lại dữ liệu vào file CSV
    with open(new_file, 'w') as f:
        for row in data:
            f.write(','.join(row) + '\n')

    with open(new_file, 'w') as f:
        for row in rows:
            f.write(','.join(row) + '\n')


fill_missing_values(sys.argv[1], sys.argv[2], sys.argv[3])
print("Successfull!!")
