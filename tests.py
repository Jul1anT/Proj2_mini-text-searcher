"""
Test Suite for Mini Text Searcher
Basic tests to verify functionality of Trie, inverted index and sparse vectors.
"""

from indexer import DocumentIndexer


def run_all_tests(indexer):
    """Runs all system tests."""
    print("RUNNING TESTS\n")
    
    # Test 1: Exact search
    print("Test 1: Exact search for 'python'")
    results = indexer.search_exact("python")
    print(f"  Found in {len(results)} documents\n")
    
    # Test 2: Autocomplete
    print("Test 2: Autocomplete 'prog'")
    suggestions = indexer.autocomplete("prog")
    print(f"  Suggestions: {suggestions}\n")
    
    # Test 3: Sparse vector
    print("Test 3: Sparse vector for 'python'")
    vector = indexer.get_word_vector("python")
    print(f"  Non-zero elements: {len(vector)}\n")
    
    # Test 4: Non-existent word
    print("Test 4: Search for non-existent word")
    results = indexer.search_exact("javascript")
    print(f"  Results: {len(results)} (expected: 0)\n")
    
    print("All tests completed\n")


def run_individual_test(test_name, indexer):
    """Runs a specific test by name."""
    tests = {
        "search": test_exact_search,
        "autocomplete": test_autocomplete,
        "vector": test_sparse_vector,
        "nonexistent": test_nonexistent_word,
        "trie": test_trie_search,
        "prefix": test_prefix_check,
        "stats": test_statistics
    }
    
    if test_name in tests:
        tests[test_name](indexer)
    else:
        print(f"Unknown test: {test_name}")
        print(f"Available tests: {', '.join(tests.keys())}")


def test_exact_search(indexer):
    """Test exact word search."""
    print("Testing exact search...")
    results = indexer.search_exact("python")
    print(f"Found 'python' in {len(results)} documents")
    for doc_id, freq in results:
        print(f"  - {doc_id}: {freq} occurrences")


def test_autocomplete(indexer):
    """Test autocomplete functionality."""
    print("Testing autocomplete...")
    suggestions = indexer.autocomplete("prog", max_results=5)
    print(f"Suggestions for 'prog': {suggestions}")


def test_sparse_vector(indexer):
    """Test sparse vector representation."""
    print("Testing sparse vector...")
    vector = indexer.get_word_vector("python")
    print(f"Sparse vector has {len(vector)} non-zero elements")
    print(f"Data: {vector}")


def test_nonexistent_word(indexer):
    """Test search for non-existent word."""
    print("Testing non-existent word search...")
    results = indexer.search_exact("javascript")
    print(f"Results for 'javascript': {len(results)}")


def test_trie_search(indexer):
    """Test Trie exact word search."""
    print("Testing Trie search...")
    found = indexer.trie.search("python")
    print(f"'python' in Trie: {found}")


def test_prefix_check(indexer):
    """Test prefix existence in Trie."""
    print("Testing prefix check...")
    exists = indexer.trie.starts_with("pro")
    print(f"Prefix 'pro' exists: {exists}")


def test_statistics(indexer):
    """Test index statistics."""
    print("Testing statistics...")
    stats = indexer.get_statistics()
    print(f"Total documents: {stats['total_documents']}")
    print(f"Unique words: {stats['unique_words']}")
    print(f"Sparse vectors: {stats['sparse_vectors']}")
    print(f"Average density: {stats['avg_vector_density']:.2f}")


if __name__ == "__main__":
    # If run directly, execute tests
    print("Mini Text Searcher - Test Suite\n")
    
    # Import and setup
    from main import SAMPLE_DOCS
    
    indexer = DocumentIndexer()
    
    # Load sample documents
    print("Loading sample documents...\n")
    for doc_name, content in SAMPLE_DOCS.items():
        indexer.add_document(content, doc_name)
        print(f"{doc_name}")
    print()
    
    # Run all tests
    run_all_tests(indexer)
