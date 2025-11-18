"""
Mini Text Searcher - Main Program
Demonstrates the use of Trie, inverted index and sparse vectors.
"""

from indexer import DocumentIndexer


# Sample documents for testing
SAMPLE_DOCS = {
    "python_intro.txt": """
        Python is a high-level interpreted programming language.
        Python is known for its clear and readable syntax. Many developers
        prefer Python for data science, web development and automation.
        Python's philosophy emphasizes code readability.
    """,
    
    "data_structures.txt": """
        Data structures are fundamental in programming. Trees
        are hierarchical structures. Dictionaries allow fast search.
        Sparse matrices save memory by storing only non-zero values.
        Python provides efficient implementations of these structures.
    """,
    
    "algorithms.txt": """
        Search algorithms are essential for retrieving information.
        Binary search works on sorted data. Hash algorithms
        allow constant-time search. Python includes optimized algorithms
        in its standard libraries for sorting and searching.
    """,
    
    "web_development.txt": """
        Python is popular for web development. Frameworks like Django and Flask
        facilitate the creation of web applications. Python allows connecting
        databases, creating REST APIs and generating dynamic content.
        Web development with Python is fast and efficient.
    """,
    
    "machine_learning.txt": """
        Python dominates the field of machine learning and artificial intelligence.
        Libraries like TensorFlow, PyTorch and scikit-learn facilitate the development
        of models. Python is the preferred language for data processing
        and building neural networks. Data analysis with Python is powerful.
    """
}


def load_sample_documents(indexer):
    """Loads sample documents into the indexer."""
    print("Loading sample documents...\n")
    for doc_name, content in SAMPLE_DOCS.items():
        indexer.add_document(content, doc_name)
        print(f"| {doc_name}")
    print()


def display_search_results(word, results, indexer):
    """Displays search results in formatted way."""
    if not results:
        print(f"Word '{word}' not found.\n")
        return
    
    print(f"'{word}' found in {len(results)} document(s):\n")
    for doc_id, freq in results:
        print(f" [ ] {doc_id}")
        print(f"     Occurrences: {freq}")
        # Show document snippet
        content = indexer.get_document(doc_id)
        lines = content.strip().split('\n')
        snippet = lines[0][:80] + "..." if len(lines[0]) > 80 else lines[0]
        print(f"     Preview: {snippet.strip()}")
        print()


def display_autocomplete(prefix, suggestions):
    """Displays autocomplete suggestions."""
    if not suggestions:
        print(f"No words starting with '{prefix}'.\n")
        return
    
    print(f"Suggestions for '{prefix}':\n")
    for i, word in enumerate(suggestions, 1):
        print(f"  {i}. {word}")
    print()


def display_statistics(stats):
    """Displays index statistics."""
    print("Index Statistics:\n")
    print(f"  Indexed documents: {stats['total_documents']}")
    print(f"  Unique words: {stats['unique_words']}")
    print(f"  Sparse vectors: {stats['sparse_vectors']}")
    print(f"  Average density: {stats['avg_vector_density']:.2f} docs/word")
    print()


def display_vector_info(word, vector):
    """Displays sparse vector information for a word."""
    print(f"Sparse vector for '{word}':\n")
    if len(vector) == 0:
        print("  Empty vector (word not found)")
    else:
        print(f"  Non-zero elements: {len(vector)}")
        print(f"  Data: {vector}")
    print()


def run_menu(indexer):
    """Runs the interactive search menu."""
    while True:
        print("=" * 50)
        print("MINI TEXT SEARCHER")
        print("1. Search exact word")
        print("2. Autocomplete (prefix)")
        print("3. View statistics")
        print("4. View word sparse vector")
        print("5. List documents")
        print("6. Exit")
        print("=" * 50)
        
        choice = input("Select an option: ").strip()
        print()
        
        if choice == '1':
            word = input("Enter word to search: ").strip()
            results = indexer.search_exact(word)
            display_search_results(word, results, indexer)
            
        elif choice == '2':
            prefix = input("Enter prefix: ").strip()
            suggestions = indexer.autocomplete(prefix, max_results=10)
            display_autocomplete(prefix, suggestions)
            
        elif choice == '3':
            stats = indexer.get_statistics()
            display_statistics(stats)
            
        elif choice == '4':
            word = input("Enter word: ").strip()
            vector = indexer.get_word_vector(word)
            display_vector_info(word, vector)
            
        elif choice == '5':
            docs = indexer.get_all_documents()
            print("Documents in index:\n")
            for i, doc_id in enumerate(docs, 1):
                print(f"  {i}. {doc_id}")
            print()
            
        elif choice == '6':
            break
            
        else:
            print("Invalid option. Try again.\n")


def main():
    """Main function."""
    indexer = DocumentIndexer()
    
    # Load sample documents
    load_sample_documents(indexer)
    
    # Start interactive menu
    run_menu(indexer)


if __name__ == "__main__":
    main()
