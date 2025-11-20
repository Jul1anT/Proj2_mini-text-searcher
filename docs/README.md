# Mini Text Searcher

Text search system implementing three fundamental data structures: **Trie (prefix tree)**, **inverted index (dictionary)** and **sparse vectors**.

## Project Description

This project is a simplified search engine that allows:
- Search for exact words in a document collection
- Autocomplete words by prefix
- Visualize term frequency statistics
- Work efficiently with sparse data

### Implemented Structures

1. **Trie (Tree)**: Prefix tree for efficient search and autocompletion
2. **Inverted Index (Dictionary)**: Word → documents mapping for fast search
3. **Sparse Vector**: Efficient frequency representation storing only non-zero values

---

## User Manual

### Requirements
- Python 3.7 or higher
- No external libraries required

### Installation and Execution

1. Navigate to the project directory:
```bash
cd /path/to/Proj2_mini-text-searcher
```

2. Run the program:
```bash
python3 main.py
```

### System Usage

When running the program, 5 sample documents are automatically loaded and basic tests are executed. Then an interactive menu appears:

```
1. Search exact word
2. Autocomplete (prefix)
3. View statistics
4. View word sparse vector
5. List documents
6. Exit
```

#### Usage Examples

**Search exact word:**
```
Select an option: 1
Enter word to search: python
```
Result: Shows all documents where "python" appears and its frequency.

**Autocomplete:**
```
Select an option: 2
Enter prefix: prog
```
Result: Shows words like "programming", "programs", "provides".

**View statistics:**
```
Select an option: 3
```
Result: Shows total documents, unique words and vector density.

**View sparse vector:**
```
Select an option: 4
Enter word: data
```
Result: Shows sparse representation of frequencies per document.

---

## Use of Artificial Intelligence

### Usage percentage: ~75%

### Description of AI usage:

AI (GitHub Copilot with Claude Sonnet 4.5) was used extensively in this project for:

1. **Architecture design (60%)**:
   - Structuring the three main classes
   - Decisions about which structure to use for each functionality
   - Modular code organization

2. **Code implementation (80%)**:
   - Generation of `Trie`, `TrieNode`, `SparseVector` and `DocumentIndexer` classes
   - Search algorithms, insertion and DFS traversal in the Trie
   - Indexing and sparse vectorization logic
   - Interactive menu and visualization functions

3. **Documentation (90%)**:
   - Technical comments in code
   - README and structures.md documentation
   - Usage examples

4. **Testing (70%)**:
   - Creation of thematic sample documents
   - Automated test function
   - Basic test cases

**Manual work by developer:**
- Initial requirements specification
- Review and validation of functionality
- Decisions on edge cases and error handling
- Final adjustments and formatting

AI significantly accelerated development allowing generation of a complete, well-structured and documented project in a short time. The generated code is clean, follows best practices and is ready to run.

---

## 📁 Project Structure

```
Proj2_mini-text-searcher/
├── trie.py              # Trie implementation (tree)
├── indexer.py           # Indexer with dictionary and sparse vectors
├── main.py              # Main program with interactive menu
├── tests.py             # Test suite for all components
└── docs/
    ├── README.md        # This file
    └── structures.md    # Technical explanation of structures
```

---

## Technical Features

- **Trie Complexity**: O(m) for insertion and search (m = word length)
- **Inverted Index**: O(1) average search using Python dictionary
- **Sparse Vector**: O(k) space where k = non-zero elements << n
- **No external dependencies**: Only Python standard library

---

[Explication Video](https://www.youtube.com/watch?v=OJ1kQ0Mo_5Y)
