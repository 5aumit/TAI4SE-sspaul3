import itertools

import urllib

import word2vec

# MSD: http://corpus.leeds.ac.uk/mocky/ru-table.tab
# Universal: http://universaldependencies.org/ru/pos/index.html
def convert_pos_MSD_to_Universal(pos):
    if pos.startswith('A'):
        return 'ADJ'
    elif pos.startswith('C'):
        return 'CCONJ'
    elif pos.startswith('I'):
        return 'INTJ'
    elif pos.startswith('M'):
        return 'NUM'
    elif pos.startswith('Nc'):
        return 'NOUN'
    elif pos.startswith('Np'):
        return 'PROPN'
    elif pos.startswith('N'):
        return 'NOUN'
    elif pos.startswith('P'):
        return 'PRON' # TODO: or DET 
    elif pos.startswith('Q'):
        return 'PART'
    elif pos.startswith('R'):
        return 'ADV'
    elif pos.startswith('S'):
        return 'ADP'
    elif pos.startswith('V'):
        return 'VERB' # TODO: or AUX
    elif pos.startswith('SENT') or pos.startswith('PUNC'):
        return 'PUNCT'
    else:
        return 'X'

# ------------------
# get_dep_tree(sentence)
# ---
# Creates a word dependency tree from a sentence.
# Returns: deptree=(node, [deptree])

# Creates a deptree from the webservice response dictionary
def make_dep_tree(respDict, idx):
  if idx == 0:
    el = None
  else:
    el = respDict[idx]
  children = [(k, respDict[k]) for k in respDict if int(respDict[k][6]) == idx]
  childTrees = [ make_dep_tree(respDict, k) for (k, c) in children ]

  return (el, childTrees)

def get_dep_tree(sentence):
  url = 'http://deptree.jental.name/parse?' + urllib.parse.urlencode({'text': sentence})
  respRaw = urllib.request.urlopen(url)
  resp = respRaw.read()
  respStr = resp.decode('utf-8')
  respList = [ r[1:-1].split('\\t') for r in respStr[1:-1].split(',') ]
  respDict = dict([(int(r[0]), r + [convert_pos_MSD_to_Universal(r[5])]) for r in respList])

  (root, trees) = make_dep_tree(respDict, 0)

  if len(trees) == 0:
    print('No tree', sentence, trees)
    return None
  else:
    return trees[0]

# ------------------
# filter_dep_tree(tree)
# ---
# Filters out invaluable parts of speech.
# Returns: deptree=(node, [deptree])

def filter_dep_tree(tree):
  root, children = tree
  posp = convert_pos_MSD_to_Universal(root[3])
  if (posp == 'ADJ' or posp == 'NUM' or posp == 'NOUN' or posp == 'PROPN' or posp == 'ADV' or posp == 'VERB'):
    res = [ (root, list(itertools.chain.from_iterable([ filter_dep_tree(c) for c in children ]))) ]
  else:
    cd = [ filter_dep_tree(c) for c in children ]
    if len(cd) > 0:
      res = list(itertools.chain.from_iterable(cd))
    else:
      res = []
  return res

# ------------------
# filter_dep_tree(tree)
# ---
# Prints a word dependency tree

def print_dep_tree(tree):
  def pdt(t, offset):
    root, children = t
    print(''.join([ ' ' for i in range(0, offset) ]), root[1], root[3])
    for c in children:
      pdt(c, offset + 1)
  pdt(tree, 0)
