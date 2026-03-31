# Hardest Questions - Cambridge 9618 Paper 4

This document ranks the most challenging questions from 2020-2025 exams.

---

## Top 5 Hardest Questions

### 1. 🏆 2022 Q2 - Binary Search Tree
**File:** `2022/q2_binary_tree.py`

**Why it's hardest:**
- Complex `Delete()` operation with 3 cases (leaf, one child, two children)
- Finding in-order successor for two-child deletion
- Implementing all traversals (in-order, pre-order, post-order)
- Tree statistics: height, leaf count, internal nodes
- Recursive thinking required throughout

**Key challenges:**
```python
def Delete(self, data):
    # Must handle: leaf node, one child, two children
    # For two children: find in-order successor
```

---

### 2. 🥈 2024 Q2 - Hash Table
**File:** `2024/q2_hash_table.py`

**Why it's hard:**
- Understanding hash functions and collision resolution
- Linear probing implementation
- Handling deletions without breaking search chain
- Rehashing when table gets full
- Load factor considerations

**Key challenges:**
```python
def Delete(self, key):
    # After deletion, must rehash subsequent items
    # to maintain search integrity
```

---

### 3. 🥉 2025 Q2 - Recursion
**File:** `2025/q2_recursion.py`

**Why it's hard:**
- Multiple different recursive patterns
- Towers of Hanoi (hardest recursive problem)
- Efficient power calculation O(log n) vs O(n)
- Understanding base case and recursive case
- Tracing recursive calls mentally

**Key challenges:**
```python
def PowerEfficient(base, exponent):
    if exponent % 2 == 0:
        half_power = PowerEfficient(base, exponent // 2)
        return half_power * half_power  # O(log n)
```

---

### 4. 2023 Q2 - Searching & Sorting
**File:** `2023/q2_search_sort.py`

**Why it's hard:**
- Implementing 4+ different sorting algorithms
- Understanding time complexity differences
- QuickSort partition logic
- Comparing algorithm efficiency
- Step-by-step visualization

---

### 5. 2022 Q1 - Routes Database
**File:** `2022/q1_routes.py`

**Why it's hard:**
- Complex filtering (origin AND destination)
- Revenue calculations
- Finding shortest/cheapest routes
- Multiple search criteria
- Update and delete operations

---

## Question Difficulty Breakdown

| Year | Q1 Difficulty | Q2 Difficulty |
|------|----------------|----------------|
| 2020 | ⭐⭐ (Easy) | ⭐⭐⭐⭐ (Hard) |
| 2021 | ⭐⭐ (Easy) | ⭐⭐⭐ (Medium-Hard) |
| 2022 | ⭐⭐⭐⭐ (Hard) | ⭐⭐⭐⭐⭐ (Hardest) |
| 2023 | ⭐⭐⭐ (Medium) | ⭐⭐⭐⭐ (Hard) |
| 2024 | ⭐⭐⭐ (Medium) | ⭐⭐⭐⭐⭐ (Very Hard) |
| 2025 | ⭐⭐⭐ (Medium) | ⭐⭐⭐⭐ (Hard) |

---

## Study Tips

1. **Master one data structure at a time** - Don't rush
2. **Practice drawing structures** - Trees, lists, hash tables
3. **Trace through examples** - Walk through each algorithm step-by-step
4. **Understand WHY, not just HOW** - Know when to use which structure
5. **Time yourself** - Exam has 2.5 hours for 2 questions

---

## Quick Reference - When to Use What

| Scenario | Best Structure |
|----------|----------------|
| LIFO (undo) | Stack |
| FIFO (queue) | Queue / Linked List |
| Sorted data, fast search | Binary Search Tree |
| Fast search, key-value | Hash Table |
| Divide and conquer | Quick Sort / Merge Sort |
| Repeat calculations | Recursion (with memoization) |

---

Good luck with your studies! 📚
