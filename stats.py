def get_num_words(fp):
    with open(fp) as f:
        text = f.read()
    tw = 0
    wl = text.split()
    for word in wl:
        tw +=1
    return tw
def get_total_l(fp):
    ld = {}
    with open(fp) as f:
        text = f.read().lower()
    for char in text:
        ld[char] = ld.setdefault(char, 0) + 1
    return ld
def sortd(dit):
    lod = []
    for key in dit:
        if key.isalpha():
            newdict = {}
            newdict["char"] = key
            newdict["num"] = dit[key]
            lod.append(newdict)
        else:
            continue
    return lod
def h(item):
    return item["num"]
    