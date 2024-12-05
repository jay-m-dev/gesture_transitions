import csv

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'transitions_test.csv'
output_file = 'transitions_test_output.csv'

transition_time = 1000
# Open and read the CSV file
with open(file_path, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    csv_reader = csv.DictReader(infile)  # Reads rows as ordered dictionaries
    fieldnames = csv_reader.fieldnames + ['transition_label', 'transition_time']
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    csv_writer.writeheader()

    for row in csv_reader:
        row_time = int(row['Time Stamp'])
        while row_time >= transition_time:
            # Write duplicate row for 'n' label
            duplicated_row = row.copy()
            duplicated_row['transition_label'] = 'n'
            duplicated_row['transition_time'] = transition_time
            csv_writer.writerow(duplicated_row)
            transition_time += 1000

        # Write the row with the 't' label when row_time < transition_time
        row['transition_label'] = 't'
        row['transition_time'] = transition_time
        csv_writer.writerow(row)
        transition_time += 1000

