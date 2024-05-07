# import
import os, re




# main
def main(toks, tags_pos):
    refsign_words = input_polymer_refsign_words()                              # f


    tags = ['O'] * len(toks)
    words = refsign_words
    tags, abbs = search_refsign(toks, tags, tags_pos, words, abb=0)            # f

    words = list(abbs.keys())
    tags = search_refsign(toks, tags, tags_pos, words, abb=1)[0]               # f


    return tags, abbs




# f
def input_polymer_refsign_words():
    indir = "./229_file"
    infname = "polymer-refsign-words.txt"
    refsign_words = []
    with open(indir + '/' + infname, 'r', encoding = "utf-8") as f:
        for x in f:
            x = x[:-1]
            refsign_words.append(x)

    return refsign_words



def search_refsign(TOK, TAG, POS, REFSIGN_TERM, abb):
    ABB = {}
    for i, tok in enumerate(TOK):
        if TAG[i] != "O": continue
        if abb == 0: tok = tok.lower()

        for term in REFSIGN_TERM:
            if term in tok:

                start, end = check_span(i, POS, TOK)                           # f
                end_2 = -1

                if abb == 0:
                    cnt_bracket = check_cnt_bracket(start, end, POS)           # f
                    if cnt_bracket % 2 == 1: continue

                # if TOK[start].lower() in ["a", "an"]: continue
                if POS[end][:2] in ["VB"]: continue
                tok_end = TOK[end]
                if abb == 0: tok_end = TOK[end].lower()
                if not term in tok_end:
                    if POS[end][:2] == "-R" and POS[i + 1][:2] == "-L":
                        if end - (i + 1) == 2:
                            if TOK[end - 1].isnumeric(): end = i
                            else:
                                if abb == 0:
                                    refsign_abb = check_abbreviation(TOK[end - 1])    # f
                                    if refsign_abb != "":
                                        REFSIGN = TOK[start : i + 1]
                                        refsign_long = longform_for_abb(REFSIGN, refsign_abb)    # f
                                        if not refsign_abb in ABB:
                                            ABB[refsign_abb] = refsign_long
                                        end_2 = end - 1
                        end = i
                    else: continue

                TAG = tag_BIES(TAG, start, end, end_2)                         # f


    return TAG, ABB



def check_span(i, POS, TOK):
    OK_POS_1 = ["NN", "JJ", "RB", "CD", "HY", "-L", "-R", "SY", "AD", "PD"]
    OK_POS_2 = OK_POS_1
    # OK_POS_2 = ["NN", "CD", "HY", "SY"]


    start, end = 0, len(POS) - 1
    for j in range(i)[::-1]:
        if not POS[j][:2] in OK_POS_1:
            if POS[j] == "DT":
                start = j
                break
            if POS[j] == "VBN": continue
            if POS[j][:2] == "CC":
                if TOK[j].lower() == "both": continue
                if 0 < j < len(POS) - 1 and POS[j - 1][:2] == POS[j + 1][:2]: continue
            start = j + 1
            break
    for j in range(i + 1, len(POS)):
        if not POS[j][:2] in OK_POS_2:
            if POS[j][:2] == "CC":
                if 0 < j < len(POS) - 1 and POS[j - 1][:2] == POS[j + 1][:2]: continue
            end = j - 1
            break


    return start, end



def check_cnt_bracket(start, end, POS):
    cnt_bracket = 0
    for j in range(start, end + 1):
        if "-L" in POS[j] or "-R" in POS[j]: cnt_bracket += 1

    return cnt_bracket



def check_abbreviation(tok):
    refsign_abb = ""
    M = re.findall(r"[A-Z]", tok)
    if len(M) / len(tok) >= 0.5:
        if not tok.isnumeric(): refsign_abb = tok

    return refsign_abb



def longform_for_abb(REFSIGN, refsign_abb):
    if refsign_abb[-1] == "s": refsign_abb = refsign_abb[:-1]

    long = "_"
    num = len(refsign_abb)
    while num > len(REFSIGN): num -= 1
    if num <= len(REFSIGN):
        cnt_OK = 0
        if refsign_abb[0].upper() == REFSIGN[-num:][0][0].upper(): cnt_OK = 1
        else:
            if num > 1:
                num -= 1
                if refsign_abb[0].upper() == REFSIGN[-num:][0][0].upper(): cnt_OK = 1
        if cnt_OK == 1:
            abb = ""
            i2 = -1
            for i, char_abb in enumerate(refsign_abb):
                i2 += 1
                if i2 < num:
                    word = REFSIGN[-num:][i2]
                    if word[0].upper() == char_abb.upper(): abb += word[0].upper()
                    else:
                        char = check_middle_char(REFSIGN[-num:][i2 - 1], char_abb)    # f
                        if char != "":
                            abb += char
                            i2 -= 1
                elif i2 == num:
                    char = check_middle_char(REFSIGN[-num:][i2 - 1], char_abb)    # f
                    if char != "": abb += char
            if abb == refsign_abb.upper(): long = " ".join(REFSIGN[-num:])


    return long



def check_middle_char(word, abb_char):
    char = ""
    for i, x in enumerate(word):
        if i == 0: continue
        if x.upper() == abb_char.upper():
            char = x.upper()
            break

    return char



def tag_BIES(TAG, start, end, end_2, label=None):
    if start == end: TAG[start] = "S"
    else:
        for j in range(start, end + 1):
            if j == start: TAG[j] = "B"
            elif j == end: TAG[j] = "E"
            else: TAG[j] = "I"
    if end_2 != -1: TAG[end_2] = "S"


    if label is not None:
        for tag in TAG:
            if tag != 'O': tag += '-' + label


    return TAG

