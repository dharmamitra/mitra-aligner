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


def process_folder(folder):
    skt_folder = ""
    eng_folder = ""
    for subfolder in os.listdir(folder):
        if "sanskrit-prepared" in subfolder and os.path.isdir(os.path.join(folder, subfolder)):
            skt_folder = os.path.join(folder, subfolder)
        if "english-prepared" in subfolder and os.path.isdir(os.path.join(folder, subfolder)):
            eng_folder = os.path.join(folder, subfolder)
    for file in os.listdir(skt_folder):
        src_path = os.path.join(skt_folder, file)
        tgt_path = os.path.join(eng_folder, file)
        if src_path.endswith(".txt"):
            if os.path.isfile(src_path) and os.path.isfile(tgt_path):
                output_path = src_path.replace(".txt", ".tsv")
                align_text_pair(src_path, tgt_path, output_path)
            else:
                print("Skipping", src_path, tgt_path)

process_folder(sys.argv[1])