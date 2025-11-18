"""
Document indexer using inverted index and sparse vectors.
- Inverted index: dictionary {word -> list of documents}
- Sparse vector: dictionary {position -> frequency} for infrequent terms
"""

import re
from collections import defaultdict
from trie import Trie


class SparseVector:
    """
    Sparse vector that stores only non-zero positions.
    Useful for representing term frequencies in large documents.
    """
    
    def __init__(self):
        self.data = {}  # {índice: valor} solo para valores != 0
    
    def set(self, index, value):
        """Sets value at given index. Removes if 0."""
        if value == 0:
            self.data.pop(index, None)
        else:
            self.data[index] = value
    
    def get(self, index):
        """Gets value at index (0 if not exists)."""
        return self.data.get(index, 0)
    
    def increment(self, index):
        """Increments counter at given index."""
        self.data[index] = self.data.get(index, 0) + 1
    
    def items(self):
        """Returns sorted (index, value) pairs."""
        return sorted(self.data.items())
    
    def __len__(self):
        """Number of non-zero elements."""
        return len(self.data)
    
    def __repr__(self):
        return f"SparseVector({dict(self.items())})"


class DocumentIndexer:
    """
    Indexer that combines:
    - Trie for autocompletion
    - Inverted index (dictionary) for document search
    - Sparse vectors for term frequencies
    """
    
    def __init__(self):
        self.trie = Trie()
        self.inverted_index = defaultdict(list)  # {word: [(doc_id, frequency), ...]}
        self.documents = {}  # {doc_id: original content}
        self.word_vectors = {}  # {word: SparseVector} maps word to vector of doc_ids
        self.doc_counter = 0
    
    def add_document(self, content, doc_name=None):
        """
        Adds document to the index.
        Extracts words, updates Trie, inverted index and sparse vectors.
        """
        doc_id = doc_name if doc_name else f"doc_{self.doc_counter}"
        self.doc_counter += 1
        
        self.documents[doc_id] = content
        
        # Extract words (only alphanumeric)
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Count local frequencies
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1
        
        # Update structures
        for word, freq in word_freq.items():
            # Insert into Trie
            self.trie.insert(word)
            
            # Update inverted index
            self.inverted_index[word].append((doc_id, freq))
            
            # Update sparse vector (uses hash of doc_id as index)
            if word not in self.word_vectors:
                self.word_vectors[word] = SparseVector()
            doc_index = hash(doc_id) % 10000  # Convert doc_id to numeric index
            self.word_vectors[word].set(doc_index, freq)
        
        return doc_id
    
    def search_exact(self, word):
        """
        Searches for exact word in inverted index.
        Returns list of (doc_id, frequency) where it appears.
        """
        word = word.lower()
        if not self.trie.search(word):
            return []
        return self.inverted_index[word]
    
    def autocomplete(self, prefix, max_results=10):
        """Returns words starting with prefix using Trie."""
        return self.trie.autocomplete(prefix, max_results)
    
    def get_word_vector(self, word):
        """Gets sparse frequency vector for a word."""
        word = word.lower()
        return self.word_vectors.get(word, SparseVector())
    
    def get_document(self, doc_id):
        """Gets document content."""
        return self.documents.get(doc_id, "")
    
    def get_all_documents(self):
        """Returns list of document IDs."""
        return list(self.documents.keys())
    
    def get_statistics(self):
        """Returns index statistics."""
        total_words = len(self.inverted_index)
        total_docs = len(self.documents)
        sparse_vectors_count = len(self.word_vectors)
        
        # Calculate average density of sparse vectors
        avg_density = 0
        if sparse_vectors_count > 0:
            total_nonzero = sum(len(v) for v in self.word_vectors.values())
            avg_density = total_nonzero / sparse_vectors_count
        
        return {
            'total_documents': total_docs,
            'unique_words': total_words,
            'sparse_vectors': sparse_vectors_count,
            'avg_vector_density': avg_density
        }
