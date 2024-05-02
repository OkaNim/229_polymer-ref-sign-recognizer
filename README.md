# Polymer referring sign recognizer
'the film' や 'the membrane' などのポリマーの指示表現を自動認識します。<br>
<br>
<br>
## How to use
Please run 229_test.py in /src without moving out of the folder.<br>
<br>
----- 229_test.py -----<br>
import src_039_recognize_polymer_name_240426 as src_039<br>
import src_229_recognize_polymer_refsign_240426 as src_229<br>
<br>
<br>
toks = ["in", "polystyrene-block-poly", '(', "ethylene", "oxide", ')', '(', "PS-b-PEO", ')', "bottlebrush", "block", "copolymers", '(', "BBCP", ')', "upon", "The", "BBCPs", "are", "soluble", "in", "organic", "solvents", "."]<br>
<br>
pos_tags = ["IN", "NN", "-LRB-", "NN", "NN", "-RRB-", "-LRB-", "NN", "-RRB-", "NN", "NN", "NNS", "-LRB-", "NN", "-RRB-", "IN", "DT", "NNS", "VBP", "JJ", "IN", "JJ", "NNS", "."]<br>
# It is necessary to recognize pos_tags in advance using Stanford Core NLP.<br>
<br>
<br>
refsign_tags, refsign_abbs = src_229.main(toks, pos_tags)<br>
<br>
polymer_tags = src_039.main(toks)<br>
<br>
<br>
print("\ntoks\n", toks)<br>
print("\nrefsign_tags\n", refsign_tags)<br>
print("\npolymer_tags\n", polymer_tags)<br>
print("")<br>
print("\nrefsign_abbs\n", refsign_abbs)<br>
print("\n\n")<br>
-------------------<br>
<br>
After running, the results will be printed on screen as follow:<br>
<br>
toks<br>
 ['in', 'polystyrene-block-poly', '(', 'ethylene', 'oxide', ')', '(', 'PS-b-PEO', ')', 'bottlebrush', 'block', 'copolymers', '(', 'BBCP', ')', 'upon', 'The', 'BBCPs', 'are', 'soluble', 'in', 'organic', 'solvents', '.']<br>
<br>
refsign_tags<br>
 ['O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'E', 'O', 'S', 'O', 'O', 'B', 'E', 'O', 'O', 'O', 'O', 'O', 'O']<br>
<br>
polymer_tags<br>
 ['O', 'B', 'I', 'I', 'I', 'E', 'O', 'S', 'O', 'O', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'O', 'O', 'O']<br>
<br>
<br>
refsign_abbs<br>
 {'BBCP': 'bottlebrush block copolymers'}<br>

