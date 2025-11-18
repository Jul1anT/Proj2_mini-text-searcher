# Data Structures Used

This document explains the three data structures implemented in the mini text searcher.

---

## 1. Trie (Prefix Tree)

### What is it?
A **Trie** is a specialized tree for storing character strings where each node represents a character. Words are formed by following paths from the root to nodes marked as "end of word".

### Structure
```
        root
       /  |  \
      p   d   a
      |   |   |
      y   a   l
      |   |   |
      t   t   g
      |   |    \
      h   a     o
      |    \
      o     s
      |
      n (end)
```

### Usage in the Project
- **Insertion**: Add words to the Trie letter by letter
- **Search**: Verify if a complete word exists
- **Autocompletion**: Find all words with a given prefix using DFS

### Advantages
- Very efficient prefix search: O(m) where m = length
- Ideal for autocompletion and spell checkers
- Shares common prefixes saving space

### Key Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary char -> TrieNode
        self.is_end_of_word = False
```

The `autocomplete()` method uses **DFS (Depth-First Search)** to traverse all branches from the prefix node and collect complete words.

---

## 2. Inverted Index (Dictionary)

### What is it?
An **inverted index** is a dictionary that maps each word to the list of documents where it appears, along with its frequency.

### Structure
```python
{
    "python": [("python_intro.txt", 4), ("data_structures.txt", 1), ...],
    "data": [("data_structures.txt", 2), ("machine_learning.txt", 3)],
    "web": [("web_development.txt", 5)]
}
```

### Usage in the Project
- **Indexing**: When processing a document, extract words and update the dictionary
- **Search**: Given a word, instantly get all relevant documents
- **Frequencies**: Know how many times each term appears in each document

### Advantages
- Extremely fast search: O(1) average
- Scalable to millions of documents
- Base of real search engines (Elasticsearch, Solr)

### Key Implementation
```python
from collections import defaultdict

inverted_index = defaultdict(list)
inverted_index[word].append((doc_id, frequency))
```

Python uses **hash tables** internally for dictionaries, which guarantees average constant-time access.

---

## 3. Sparse Vector

### What is it?
A **sparse vector** is an efficient representation of vectors where most elements are zero. It only stores non-zero positions and values in a dictionary.

### Problem it Solves
If we have 10,000 documents and a word appears only in 3:
- **Dense vector**: [0, 0, 0, ..., 5, 0, ..., 2, 0, ..., 1, 0, ...] → 10,000 entries
- **Sparse vector**: {15: 5, 234: 2, 9876: 1} → 3 entries

### Structure
```python
class SparseVector:
    def __init__(self):
        self.data = {}  # {index: value} only values != 0
```

### Usage in the Project
For each word, we maintain a sparse vector that indicates:
- **Index**: Hash of document ID (position in vector space)
- **Value**: Term frequency in that document

Example:
```python
word_vectors["python"] = SparseVector({142: 4, 567: 1, 1890: 3, 8765: 2})
#                                      doc1: 4  doc2: 1  doc3: 3  doc4: 2
```

### Advantages
- **Memory savings**: Only stores values != 0
- **Efficiency**: Operations only on existing elements
- **Scalability**: Essential for NLP and information retrieval

### Implemented Operations
```python
vector.set(index, value)     # Set value (removes if 0)
vector.get(index)            # Get value (returns 0 if not exists)
vector.increment(index)      # Increment counter
vector.items()               # Iterate over non-zero elements
```

---

## Integration of the Three Structures

### Indexing Flow
1. **Process document** → extract words
2. **Trie** ← insert word for autocompletion
3. **Inverted Index** ← add (doc_id, frequency)
4. **Sparse Vector** ← update position hash(doc_id)

### Search Flow
1. User enters prefix "pro"
2. **Trie** → autocomplete: ["programming", "provides", "processing"]
3. User selects "programming"
4. **Inverted Index** → get documents with "programming"
5. **Sparse Vector** → visualize frequency distribution

---

## Computational Complexity

| Operation | Trie | Inverted Index | Sparse Vector |
|-----------|------|----------------|---------------|
| Insertion | O(m) | O(1) average | O(1) |
| Search | O(m) | O(1) average | O(1) |
| Autocomplete | O(m + n) | N/A | N/A |
| Space | O(ALPHABET * N * M) | O(V * D) | O(k) where k << n |

Where:
- m = word length
- n = number of results
- N = number of words
- M = average length
- V = vocabulary
- D = documents
- k = non-zero elements

---

## Real-World Use Cases

### Trie
- Google Search autocomplete
- Spell checkers
- Suggestion systems
- Dictionary validation

### Inverted Index
- Search engines (Google, Bing)
- Elasticsearch and Solr
- Full-text databases
- Log systems

### Sparse Vector
- TF-IDF models in NLP
- Recommendation systems
- Sparse graphs
- Computational linear algebra (SciPy sparse)

---

## Conclusion

The combination of these three structures allows:
- **Fast searches** (inverted index)
- **Efficient autocompletion** (Trie)
- **Efficient memory usage** (sparse vectors)

This design is the foundation of modern information retrieval systems and demonstrates how choosing the correct data structure directly impacts software performance.
