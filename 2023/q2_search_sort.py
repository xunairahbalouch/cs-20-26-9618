def LinearSearch(data_list, target):
    """Task 2.1: Linear search - returns index and comparison count"""
    comparisons = 0
    
    for i in range(len(data_list)):
        comparisons += 1
        if data_list[i] == target:
            return i, comparisons
    
    return -1, comparisons


def BinarySearchIterative(data_list, target):
    """Task 2.2: Binary search (iterative)"""
    left = 0
    right = len(data_list) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if data_list[mid] == target:
            return mid, comparisons
        elif data_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons


def BinarySearchRecursive(data_list, target, left=None, right=None, comparisons=0):
    """Task 2.2: Binary search (recursive)"""
    if left is None:
        left = 0
    if right is None:
        right = len(data_list) - 1
    
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    
    if data_list[mid] == target:
        return mid, comparisons
    elif data_list[mid] < target:
        return BinarySearchRecursive(data_list, target, mid + 1, right, comparisons)
    else:
        return BinarySearchRecursive(data_list, target, left, mid - 1, comparisons)


def InsertionSort(data_list):
    """Task 2.3: Insertion sort with step-by-step visualization"""
    arr = data_list.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    print("Insertion Sort steps:")
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        print(f"\nStep {i}: Inserting {key}")
        print(f"  Before: {arr}")
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        
        comparisons += 1 if j >= 0 else 0
        arr[j + 1] = key
        print(f"  After:  {arr}")
    
    return arr, comparisons, swaps


def QuickSort(data_list):
    """Task 2.4: Quick sort with step-by-step visualization"""
    arr = data_list.copy()
    comparisons = 0
    swaps = 0
    
    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        
        print(f"  Partition: pivot={pivot}, arr[{low}:{high+1}] = {arr[low:high+1]}")
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        
        print(f"    Result: {arr[low:high+1]}")
        return i + 1
    
    def quick_sort(low, high):
        nonlocal comparisons
        if low < high:
            pi = partition(low, high)
            print(f"  Pivot at index {pi}, value {arr[pi]}")
            quick_sort(low, pi - 1)
            quick_sort(pi + 1, high)
    
    print("Quick Sort steps:")
    quick_sort(0, len(arr) - 1)
    
    return arr, comparisons, swaps


def BubbleSort(data_list):
    """Task 2.5: Bubble sort for comparison"""
    arr = data_list.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    
    return arr, comparisons, swaps


def MergeSort(data_list):
    """Task 2.5: Merge sort for comparison"""
    arr = data_list.copy()
    comparisons = 0
    
    def merge(left, mid, right):
        nonlocal comparisons
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            comparisons += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def merge_sort(left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)
    
    merge_sort(0, len(arr) - 1)
    
    return arr, comparisons, 0


def CompareSortingAlgorithms(data_list):
    """Task 2.5: Compare different sorting algorithms"""
    results = {}
    
    print("=" * 80)
    print("Comparing Sorting Algorithms")
    print("=" * 80)
    print(f"Original list: {data_list}")
    print()
    
    print("Running Bubble Sort...")
    bubble_result, bubble_comp, bubble_swaps = BubbleSort(data_list)
    results['Bubble Sort'] = {'comparisons': bubble_comp, 'swaps': bubble_swaps}
    print(f"Result: {bubble_result}")
    print(f"Comparisons: {bubble_comp}, Swaps: {bubble_swaps}")
    print()
    
    print("Running Insertion Sort...")
    insertion_result, insertion_comp, insertion_swaps = InsertionSort(data_list)
    results['Insertion Sort'] = {'comparisons': insertion_comp, 'swaps': insertion_swaps}
    print(f"Result: {insertion_result}")
    print(f"Comparisons: {insertion_comp}, Swaps: {insertion_swaps}")
    print()
    
    print("Running Quick Sort...")
    quick_result, quick_comp, quick_swaps = QuickSort(data_list)
    results['Quick Sort'] = {'comparisons': quick_comp, 'swaps': quick_swaps}
    print(f"Result: {quick_result}")
    print(f"Comparisons: {quick_comp}, Swaps: {quick_swaps}")
    print()
    
    print("Running Merge Sort...")
    merge_result, merge_comp, merge_swaps = MergeSort(data_list)
    results['Merge Sort'] = {'comparisons': merge_comp, 'swaps': merge_swaps}
    print(f"Result: {merge_result}")
    print(f"Comparisons: {merge_comp}, Swaps: {merge_swaps}")
    print()
    
    print("=" * 80)
    print("Summary:")
    print("=" * 80)
    print(f"{'Algorithm':<20} {'Comparisons':>15} {'Swaps':>15}")
    print("-" * 50)
    for algo, stats in results.items():
        print(f"{algo:<20} {stats['comparisons']:>15} {stats['swaps']:>15}")


if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    
    print("=" * 80)
    print("Task 2.1: Linear Search")
    print("=" * 80)
    target = 25
    idx, comps = LinearSearch(sorted_list, target)
    print(f"Search for {target} in {sorted_list}")
    print(f"Found at index: {idx}, Comparisons: {comps}")
    
    print("\n" + "=" * 80)
    print("Task 2.2: Binary Search")
    print("=" * 80)
    target = 25
    idx, comps = BinarySearchIterative(sorted_list, target)
    print(f"Iterative: Search for {target} - Found at index: {idx}, Comparisons: {comps}")
    
    idx, comps = BinarySearchRecursive(sorted_list, target)
    print(f"Recursive: Search for {target} - Found at index: {idx}, Comparisons: {comps}")
    
    print("\n" + "=" * 80)
    print("Task 2.5: Algorithm Comparison")
    print("=" * 80)
    CompareSortingAlgorithms(test_list)
