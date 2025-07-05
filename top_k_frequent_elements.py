def top_k_frequent(nums, k):
    # Step 1: Frequency map using dictionary
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Step 2: Create frequency buckets
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num in freq_map:
        freq = freq_map[num]
        buckets[freq].append(num)

    # Step 3: Gather k most frequent from buckets
    result = []
    for freq in range(n, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result  # In case of edge conditions

# Test Case 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print("Output 1:", top_k_frequent(nums1, k1))
# Expected: [1, 2]

# Test Case 2
nums2 = [1]
k2 = 1
print("Output 2:", top_k_frequent(nums2, k2))
# Expected: [1]

# Test Case 3
nums3 = [4, 4, 4, 6, 6, 6, 5, 5, 5, 7]
k3 = 3
print("Output 3:", top_k_frequent(nums3, k3))
#  Expected: [4, 5, 6] or any permutation of these 3


# Component	Complexity
# Frequency Map	O(n)
# Buckets Build	O(n)
# Result Extraction	O(n) (worst-case)
# Total	O(n)
