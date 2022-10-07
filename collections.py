print("Hello! This tool can calculate transcribed, reverse, complement and reverse complement sequences. "
      "Moreover, it can calculate gc-content or open reading frame and build protein")

'''
reverse transcribe
'''


def reverse_transcribe(seq):
    rev_transcribe_dict = {"U": "T", "u": "t"}
    rev_trans_seq = ''
    for nucl in seq:
        if nucl in rev_transcribe_dict:
            rev_trans_seq += rev_transcribe_dict[nucl]
        else:
            rev_trans_seq += nucl
    return reverse(rev_trans_seq)


'''
reverse
'''


def reverse(seq):
    return seq[::-1]


'''
complement
'''


def complement(seq):
    if na == "DNA":
        complement_dna_dict = {"A": "T", "a": "t", "T": "A", "t": "a", "G": "C", "g": "c", "C": "G", "c": "g"}
        comp_dna_seq = ''
        for nucl in seq:
            comp_dna_seq += complement_dna_dict[nucl]
        return comp_dna_seq
    else:
        complement_rna_dict = {"A": "U", "a": "u", "U": "A", "u": "a", "G": "C", "g": "c", "C": "G", "c": "g"}
        comp_rna_seq = ''
        for nucl in seq:
            comp_rna_seq += complement_rna_dict[nucl]
        return comp_rna_seq


'''
reverse complement
'''


def reverse_complement(seq):
    return complement(seq)[::-1]


'''
gc-content
'''


def gc_content(seq):
    gc_in_seq = 0
    for nucl in seq.lower():
        if nucl == "g" or nucl == "c":
            gc_in_seq += 1
    return str((gc_in_seq / len(seq)) * 100) + " %"


'''
transcribe
'''


def transcribe(seq):
    transcribe_dict = {"T": "U", "t": "u"}
    trans_seq = ''
    for nucl in seq:
        if nucl in transcribe_dict:
            trans_seq += transcribe_dict[nucl]
        else:
            trans_seq += nucl
    return reverse(trans_seq)


'''
open reading frame
'''


def orf(seq):
    triplets_1 = [seq[i:i + 3] for i in range(0, len(seq), 3)]
    triplets_2 = [seq[i:i + 3] for i in range(1, len(seq), 3)]
    triplets_3 = [seq[i:i + 3] for i in range(2, len(seq), 3)]
    triplets_4 = [reverse_complement(seq)[i:i + 3] for i in range(0, len(seq), 3)]
    triplets_5 = [reverse_complement(seq)[i:i + 3] for i in range(1, len(seq), 3)]
    triplets_6 = [reverse_complement(seq)[i:i + 3] for i in range(2, len(seq), 3)]
    triplets = [triplets_1, triplets_2, triplets_3, triplets_4, triplets_5, triplets_6]
    start_indexes = [[], [], [], [], [], []]
    stop_indexes = [[], [], [], [], [], []]
    starts = ["aug", "atg"]
    stops = ["uaa", "uga", "uag", "taa", "tga", "tag"]
    for var in range(len(triplets)):
        for triple in range(len(triplets[var])):
            if triplets[var][triple].lower() in starts:
                start_indexes[var].append(triple)
            elif triplets[var][triple].lower() in stops:
                stop_indexes[var].append(triple)
    orfs = [[], [], [], [], [], []]
    for pos in range(len(start_indexes)):
        for ind in range(len(start_indexes[pos])):
            for stop in stops:
                if stop in triplets[pos]:
                    orf_list = triplets[pos][start_indexes[pos][ind]:(triplets[pos].index(stop)+1)]
                    count = 0
                    for another_stop in stops:
                        if another_stop in orf_list:
                            count += 1
                    if count == 1:
                        orfs[pos].append(''.join(orf_list))
    return orfs

'''
protein in development
'''

'''
def protein(seq):
    aminoacids = {
        'aua': 'I', 'auc': 'I', 'auu': 'I', 'aug': 'M',
        'aca': 'T', 'acc': 'T', 'acg': 'T', 'acu': 'T',
        'aac': 'N', 'aau': 'N', 'aaa': 'K', 'aag': 'K',
        'agc': 'S', 'agu': 'S', 'aga': 'R', 'agg': 'R',
        'cua': 'L', 'cuc': 'L', 'cug': 'L', 'cuu': 'L',
        'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'ccu': 'P',
        'cac': 'H', 'cau': 'H', 'caa': 'Q', 'cag': 'Q',
        'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgu': 'R',
        'gua': 'V', 'guc': 'V', 'gug': 'V', 'guu': 'V',
        'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gcu': 'A',
        'gac': 'D', 'gau': 'D', 'gaa': 'E', 'gag': 'E',
        'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggu': 'G',
        'uca': 'S', 'ucc': 'S', 'ucg': 'S', 'ucu': 'S',
        'uuc': 'F', 'uuu': 'F', 'uua': 'L', 'uug': 'L',
        'uac': 'Y', 'uau': 'Y', 'uaa': '_', 'uag': '_',
        'ugc': 'C', 'ugu': 'C', 'uga': '_', 'ugg': 'W',
    }
    triplets = [orf(seq)[i:i + 3] for i in range(0, len(seq), 3)]
    if len(triplets[len(triplets) - 1]) < 3:
        triplets.pop(len(triplets) - 1)
    prot = ''
    for i in triplets:
        prot += aminoacids[i]
    return prot
'''

'''
exit
'''


def escape():
    return "Good luck!"


'''
help
'''


def available():
    return list(available_cmds_dict.keys())


'''
check for correct alphabet
'''


def check(seq):
    nucleotides = ["A", "T", "G", "C", "U", "a", "t", "g", "c", "u"]
    nucl_acid = ""
    for nucl in seq:
        if nucl not in nucleotides:
            print("Invalid alphabet. Try again!")
            nucl_acid += "warning"
            return nucl_acid
    u_in_seq = seq.lower().find("u")
    t_in_seq = seq.lower().find("t")
    if u_in_seq != -1 and t_in_seq != -1:
        print("Invalid alphabet. Try again!")
        nucl_acid += "warning"
    elif u_in_seq == -1 and t_in_seq != -1:
        nucl_acid += "DNA"
    elif u_in_seq != -1 and t_in_seq == -1:
        nucl_acid += "RNA"
    return nucl_acid


'''
available commands, which this tool runs
'''

available_cmds_dict = {"transcribe": transcribe,
                       "reverse transcribe": reverse_transcribe,
                       "reverse": reverse,
                       "complement": complement,
                       "reverse complement": reverse_complement,
                       "gc-content": gc_content,
                       "open reading frame": orf,
                       "exit": escape,
                       "help": available
                       }

'''
input sequence and command in infinite loop
'''

while True:
    command = input("Enter command:")

    if command not in available_cmds_dict.keys():
        print("Invalid command. Try again!")
        continue
    elif command == "exit":
        print(escape())
        break
    elif command == "help":
        print(available())
        continue

    na = ''

    while True:
        sequence = input("Enter sequence:")
        nucl_acid = check(sequence)
        if nucl_acid == '' and command not in ["reverse", "gc-content"]:
            nucl_acid += input("What type of nucleic acid is the sequence? (DNA/RNA)")
            if nucl_acid != "DNA" and nucl_acid != "RNA":
                print("Invalid nucleic acid! Try again!")
                continue
            else:
                na += nucl_acid
                break
        elif nucl_acid == "warning":
            continue
        else:
            na += nucl_acid
            break

    if na == "RNA" and command == "transcribe":
        print("Invalid command or nucleic acid type. Try again!")
        continue
    elif na == "DNA" and command == "reverse transcribe":
        print("Invalid command or nucleic acid type. Try again!")
        continue
    for cmd in range(len(list(available_cmds_dict.keys()))):
        if list(available_cmds_dict.keys())[cmd] == command:
            print(available_cmds_dict.values()[cmd](sequence))
