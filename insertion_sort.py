#  Insertion Sort algorithm that sorts an array in monotonically decreasing order (largest to smallest, instead of the standard smallest to largest)
def insertion_sort_desc(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are smaller than key,
        # to one position ahead of their current position
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def run_tests():
    """Run comprehensive tests for insertion_sort_desc"""
    
    # Test 1: Basic unsorted array
    test1 = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    result1 = insertion_sort_desc(test1.copy())
    assert result1 == [9, 8, 7, 6, 5, 4, 3, 2, 1], f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: Basic unsorted array")
    
    # Test 2: Empty array
    test2 = []
    result2 = insertion_sort_desc(test2.copy())
    assert result2 == [], f"Test 2 failed: {result2}"
    print("✓ Test 2 passed: Empty array")
    
    # Test 3: Single element
    test3 = [42]
    result3 = insertion_sort_desc(test3.copy())
    assert result3 == [42], f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: Single element")
    
    # Test 4: Two elements (unsorted)
    test4 = [1, 5]
    result4 = insertion_sort_desc(test4.copy())
    assert result4 == [5, 1], f"Test 4 failed: {result4}"
    print("✓ Test 4 passed: Two elements (unsorted)")
    
    # Test 5: Already sorted in descending order
    test5 = [10, 8, 6, 4, 2]
    result5 = insertion_sort_desc(test5.copy())
    assert result5 == [10, 8, 6, 4, 2], f"Test 5 failed: {result5}"
    print("✓ Test 5 passed: Already sorted in descending order")
    
    # Test 6: Sorted in ascending order (worst case)
    test6 = [1, 2, 3, 4, 5]
    result6 = insertion_sort_desc(test6.copy())
    assert result6 == [5, 4, 3, 2, 1], f"Test 6 failed: {result6}"
    print("✓ Test 6 passed: Sorted in ascending order (worst case)")
    
    # Test 7: Array with duplicates
    test7 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result7 = insertion_sort_desc(test7.copy())
    assert result7 == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], f"Test 7 failed: {result7}"
    print("✓ Test 7 passed: Array with duplicates")
    
    # Test 8: All same elements
    test8 = [7, 7, 7, 7, 7]
    result8 = insertion_sort_desc(test8.copy())
    assert result8 == [7, 7, 7, 7, 7], f"Test 8 failed: {result8}"
    print("✓ Test 8 passed: All same elements")
    
    # Test 9: Negative numbers
    test9 = [-3, -1, -4, -1, -5, -9, -2, -6]
    result9 = insertion_sort_desc(test9.copy())
    assert result9 == [-1, -1, -2, -3, -4, -5, -6, -9], f"Test 9 failed: {result9}"
    print("✓ Test 9 passed: Negative numbers")
    
    # Test 10: Mixed positive and negative numbers
    test10 = [3, -1, 0, -5, 2, -2, 4]
    result10 = insertion_sort_desc(test10.copy())
    assert result10 == [4, 3, 2, 0, -1, -2, -5], f"Test 10 failed: {result10}"
    print("✓ Test 10 passed: Mixed positive and negative numbers")
    
    # Test 11: Floating point numbers
    test11 = [3.14, 2.71, 1.41, 1.73, 2.23]
    result11 = insertion_sort_desc(test11.copy())
    assert result11 == [3.14, 2.71, 2.23, 1.73, 1.41], f"Test 11 failed: {result11}"
    print("✓ Test 11 passed: Floating point numbers")
    
    # Test 12: Large array
    import random
    random.seed(42)
    test12 = [random.randint(1, 1000) for _ in range(100)]
    result12 = insertion_sort_desc(test12.copy())
    assert result12 == sorted(test12, reverse=True), f"Test 12 failed"
    print("✓ Test 12 passed: Large random array (100 elements)")
    
    # Test 13: Array with zeros
    test13 = [0, 5, 0, 3, 0, 1]
    result13 = insertion_sort_desc(test13.copy())
    assert result13 == [5, 3, 1, 0, 0, 0], f"Test 13 failed: {result13}"
    print("✓ Test 13 passed: Array with zeros")
    
    # Test 14: Very large and very small numbers
    test14 = [1000000, 1, -1000000, 0, 999999]
    result14 = insertion_sort_desc(test14.copy())
    assert result14 == [1000000, 999999, 1, 0, -1000000], f"Test 14 failed: {result14}"
    print("✓ Test 14 passed: Very large and very small numbers")
    
    print("\n" + "="*50)
    print("All 14 tests passed successfully! ✓")
    print("="*50)


if __name__ == "__main__":
    run_tests()
