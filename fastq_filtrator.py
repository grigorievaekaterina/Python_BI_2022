def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0,
         save_filtered=False):
    with open(input_fastq) as input_file:
        filtered_output = open(output_file_prefix + "_passed.fastq", 'w')
        bad_output_list = []
        count = 0
        four_lines = []
        check = []
        read = 'read'
        while len(read) != 0:
            read = input_file.readline()
            count += 1
            if count % 4 == 1:
                four_lines.append(read)
            elif count % 4 == 2:
                four_lines.append(read)
                check.append(gc(read.strip(), gc_bounds))
                check.append(length(read.strip(), length_bounds))
            elif count % 4 == 3:
                four_lines.append(read)
            elif count % 4 == 0:
                four_lines.append(read)
                check.append(quality(read[:-1], quality_threshold))
                if check[0] and check[1] and check[2]:
                    filtered_output.write(''.join(four_lines))
                else:
                    bad_output_list.append(four_lines[0])
                    bad_output_list.append(four_lines[1])
                    bad_output_list.append(four_lines[2])
                    bad_output_list.append(four_lines[3])
                count = 0
                four_lines = []
                check = []
        if save_filtered is True:
            with open(output_file_prefix + "_failed.fastq") as bad_output_file:
                bad_output_file.write(''.join(bad_output_list))
                bad_output_file.close()


def gc(line, gc_bounds):
    if gc_bounds != (0, 100):
        gc_read = gc_content(line)
        if type(gc_bounds) is int:
            if gc_read <= gc_bounds:
                return True
            else:
                return False
        else:
            if gc_bounds[0] <= gc_read <= gc_bounds[1]:
                return True
            else:
                return False
    else:
        return True


# calculating gc_content
def gc_content(line):
    gc_in_seq = 0
    for nucl in line:
        if nucl == "G" or nucl == "C":
            gc_in_seq += 1
    return (gc_in_seq / len(line)) * 100


def length(line, length_bounds):
    if length_bounds != (0, 2 ** 32):
        length_read = len(line)
        if type(length_bounds) is int:
            if length_read <= length_bounds:
                return True
            else:
                return False
        else:
            if length_bounds[0] <= length_read <= length_bounds[1]:
                return True
            else:
                return False
    else:
        return True


def quality(line, quality_threshold):
    score = 0
    for nucl in line:
        score += ord(nucl)-33
    mean = score / len(line)
    if mean >= quality_threshold:
        return True
    else:
        return False

