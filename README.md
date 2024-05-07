'the film' や 'the membrane' などのポリマーの指示表現を自動認識します。<br>
<br>
<br>
## How to use
Please create the script such as 229_test.py in /src and run.<br>
```
python 229_test.py
```
<br>
----- 229_test.py -----<br>
import src_229_recognize_polymer_refsign_240426 as src_229<br>
<br>
<br>
toks = ["in", "polystyrene-block-poly", '(', "ethylene", "oxide", ')', '(', "PS-b-PEO", ')', "bottlebrush", "block", "copolymers", '(', "BBCP", ')', "upon", "The", "BBCPs", "are", "soluble", "in", "organic", "solvents", "."]<br>
<br>
pos_tags = ["IN", "NN", "-LRB-", "NN", "NN", "-RRB-", "-LRB-", "NN", "-RRB-", "NN", "NN", "NNS", "-LRB-", "NN", "-RRB-", "IN", "DT", "NNS", "VBP", "JJ", "IN", "JJ", "NNS", "."]
""" It is necessary to obtain pos_tags in advance using Stanford Core NLP. """<br>
<br>
<br>
refsign_tags, refsign_abbs = src_229.main(toks, pos_tags)<br>
<br>
print("\nrefsign_tags\n", refsign_tags)<br>
print("\nrefsign_abbs\n", refsign_abbs)<br>
print("\n\n")<br>
-------------------<br>
<br>
<br>
The BIOES tags are outputted for every token as follow:<br>
```
refsign_tags
 ['O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'E', 'O', 'S', 'O', 'O', 'B', 'E', 'O', 'O', 'O', 'O', 'O', 'O']
```
<br>
The abbreviations for referring signs are also outputted as follow:<br>
```
refsign_abbs<br>
 {'BBCP': 'bottlebrush block copolymers'}<br>
```
<br>
The tokenized text (toks) and the POS tags (pos_tags) are necessary.<br>
The POS tags should be obtained using Stanford Core NLP (https://stanfordnlp.github.io/CoreNLP/).<br>
<br>
<br>
