from difflib import SequenceMatcher
import os
import sys

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

SIMILARITY_THRESHOLD = 0.5

def folder_lookup(folder_name):
    folder_contents = [n for n in os.listdir('.')]
    dir_names = filter(os.path.isdir, folder_contents)
    #Get match ratio for each folder against folder name
    folders_ratios = {n: similar(folder_name.lower(), n.lower()) for n in dir_names}
    max_coeff_dirname = max(folders_ratios, key=folders_ratios.get)
    max_coeff_value = folders_ratios[max_coeff_dirname]
    #highest_ratio_dir = (folders_ratios[max_coeff], max_coeff)
    #print(highest_ratio_dir)
    if float(max_coeff_value) < SIMILARITY_THRESHOLD:
        sys.exit(1)
    return max_coeff_dirname #folders_ratios[max_coeff_dirname])

if __name__ == '__main__':
    n = sys.argv[1]
    result_folder = folder_lookup(n)
    print(result_folder)
    sys.exit(0)
