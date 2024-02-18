import sys
from bertalign import Bertalign

src_path = sys.argv[1]
tgt_path = sys.argv[2]
output_path = src_path.replace(".txt", ".tsv")

src_string =  open(src_path, "r").read()
tgt_string = open(tgt_path, "r").read()

aligner = Bertalign(src_string, tgt_string, "sa", "en")
aligner.align_sents()
result = aligner.return_tsv()
with open(output_path, "w") as f:
    f.write(result)