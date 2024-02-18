import sys
import os 
from bertalign import Bertalign


def align_text_pair(src_path, tgt_path, output_path):
    print("Now aligning", src_path, tgt_path, output_path)
    output_path = src_path.replace(".txt", ".tsv")

    src_string =  open(src_path, "r").read()
    tgt_string = open(tgt_path, "r").read()
    if len(src_string) >= 100 and len(tgt_string) >= 100:
        aligner = Bertalign(src_string, tgt_string, "sa", "en")    
        aligner.align_sents()
        result = aligner.return_tsv()
        with open(output_path, "w") as f:
            f.write(result)

def process_file(eng_path):
    original_path = eng_path.replace("-eng.txt", ".txt")
    output_path = original_path.replace(".txt", ".tsv")
    print("Processing", original_path, eng_path, output_path)
    if os.path.isfile(original_path) and os.path.isfile(eng_path):
        if not os.path.isfile(output_path):
            align_text_pair(original_path, eng_path, output_path)
        else:
            print("Already processed", original_path, eng_path, output_path)
    else:
        print("Skipping since files are not existing", original_path, eng_path, output_path)
    

def process_folder(folder):
    # get recursively all files ending in -eng.txt in folder
    english_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("-eng.txt"):
                english_files.append(os.path.join(root, file))
    for file in english_files:
        process_file(file)
    

process_folder(sys.argv[1])