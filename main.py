def calc_standard_deviation():
    pass


def app():
    gene_lengths = []
    gff_file = 'data/genomic.gff'
    target_feature_type = 'gene'

    with open(gff_file, "r") as file:
        for line in file:
            if line[0] == '#':
                continue

            line_data = line.strip().split("\t")
            feature_type = line_data[2]
            start = line_data[3]
            end = line_data[4]
            print(feature_type, start, end)

            if target_feature_type == feature_type:
                gene_lengths.append(gene_length(start, end))

    print(len(gene_lengths))

    mean = calc_standard_deviation(gene_lengths)
    standard_deviation = calc_standard_deviation(gene_lengths)

if __name__ == '__main__':
    app()