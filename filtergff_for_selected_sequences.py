import csv
import argparse

# define and parse the command line arguments
parser = argparse.ArgumentParser(description="Filter a GFF file to keep only selected chromosomes.")
parser.add_argument("chromosomes_file", help="The path to a file containing the list of chromosomes to keep.")
parser.add_argument("input_gff", help="The path to the GFF file to filter.")
parser.add_argument("output_gff", help="The path to the output GFF file.")
args = parser.parse_args()

# read the list of chromosomes to keep
with open(args.chromosomes_file, "r") as f:
    chromosomes_to_keep = [line.strip() for line in f]

# open the GFF file and a new file to write the filtered data to
with open(args.input_gff, "r") as gff_file, open(args.output_gff, "w", newline='') as output_file:
    reader = csv.reader(gff_file, delimiter="\t")
    writer = csv.writer(output_file, delimiter="\t")

    for row in reader:
        if row[0] in chromosomes_to_keep:  # the chromosome is the first column in a GFF file
            writer.writerow(row)
