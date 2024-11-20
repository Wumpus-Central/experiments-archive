import csv

def transform_csv_to_json(csv_data, key_mapping):
    csv_reader = csv.DictReader(csv_data.splitlines())
    data = []
    for row in csv_reader:
        if 'hash' in row:
            row['hash'] = int(row['hash'])
        transformed_row = {key: row.get(csv_key, "") for csv_key, key in zip(row.keys(), key_mapping)}
        data.append(transformed_row)
    return data