import src_039_recognize_polymer_name_240426 as src_039
import src_229_recognize_polymer_refsign_240426 as src_229


toks = ["in", "polystyrene-block-poly", '(', "ethylene", "oxide", ')', '(', "PS-b-PEO", ')', "bottlebrush", "block", "copolymers", '(', "BBCP", ')', "upon", "The", "BBCPs", "are", "soluble", "in", "organic", "solvents", "."]

pos_tags = ["IN", "NN", "-LRB-", "NN", "NN", "-RRB-", "-LRB-", "NN", "-RRB-", "NN", "NN", "NNS", "-LRB-", "NN", "-RRB-", "IN", "DT", "NNS", "VBP", "JJ", "IN", "JJ", "NNS", "."]
"""It is necessary to obtain pos_tags in advance using Stanford Core NLP."""


refsign_tags, refsign_abbs = src_229.main(toks, pos_tags)

polymer_tags = src_039.main(toks)


print("\nrefsign_tags\n", refsign_tags)
print("\nrefsign_abbs\n", refsign_abbs)
print("\npolymer_tags\n", polymer_tags)
print("\n\n")
