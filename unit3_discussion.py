"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Performance variation explanation:
    # Python lists are implemented as dynamic arrays. Inserting elements requires
    # shifting subsequent elements in memory to free up a slot at the target index.
    #
    # - Inserting at the beginning (index 0) requires shifting ALL elements, making it O(n) (worst-case).
    # - Inserting in the middle requires shifting roughly half the elements, which is still O(n) (average-case).
    # - Inserting at the end (index len(lst)) requires no shifting, running in O(1) amortized time (best-case).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Importance of index validation and safe deletion:
    # Because Python lists are dynamic arrays, attempting to remove an element
    # from an out-of-bounds index throws an IndexError, which crashes the application.
    # Safe validation protects runtime stability. Deletion also triggers memory shifting
    # for all elements to the right of the deleted index to fill the empty slot.

    # Check if the index falls within the valid bounds of the list
    if 0 <= index < len(lst):
        return lst.pop(index)

    # Return None gracefully if the index is out of bounds
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear Search Explanation:
    # Python lists store elements sequentially in contiguous memory blocks. Without sorting,
    # the computer cannot predict where a specific value resides. The algorithm must inspect
    # each element step-by-step from index 0 to len(lst)-1 until a match is found.
    # This sequential scanning gives it a worst-case time complexity of O(n).
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    # Return -1 if the value is not present in the list
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # 1. Create a base list tracking e-commerce inventory items
    inventory = ["Laptop", "Mouse", "Keyboard"]
    print(f"Original Inventory List: {inventory}")

    # 3a. Test insertion at the beginning (index 0)
    # Requires shifting "Laptop", "Mouse", and "Keyboard" to the right in memory.
    insert_at(inventory, 0, "Monitor")
    print(f"After Insertion at Beginning (index 0): {inventory}")

    # 3b. Test insertion in the middle (index 2)
    # Requires shifting "Mouse" and "Keyboard" to the right.
    insert_at(inventory, 2, "Headset")
    print(f"After Insertion in Middle (index 2): {inventory}")

    # 3c. Test insertion at the end (index equals length of list)
    # Fast O(1) operation because no elements need to be shifted.
    insert_at(inventory, len(inventory), "Speakers")
    print(f"After Insertion at End (index {len(inventory)-1}): {inventory}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # 1a. Delete from the beginning (index 0)
    # The value "Monitor" is removed; remaining items shift left to fill the gap.
    removed_beg = delete_at(inventory, 0)
    print(f"Removed Value (Beginning): {removed_beg}")
    print(f"Updated List: {inventory}")

    # 1b. Delete from the middle (index 1)
    # The value "Headset" is removed; items after it shift left.
    removed_mid = delete_at(inventory, 1)
    print(f"Removed Value (Middle): {removed_mid}")
    print(f"Updated List: {inventory}")

    # 1c. Delete from the end (index equals last valid index)
    # Efficient O(1) removal since zero elements require shifting.
    removed_end = delete_at(inventory, len(inventory) - 1)
    print(f"Removed Value (End): {removed_end}")
    print(f"Updated List: {inventory}")


    # ===============================
    # TODOION (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # 1. Search for an item known to be in the list
    search_target_1 = "Mouse"
    result_1 = search_value(inventory, search_target_1)
    # Displays the matching index where the item was found sequentially
    print(f"Searching for '{search_target_1}': Found at index {result_1}")

    # 2. Search for an item absent from the list
    search_target_2 = "Webcam"
    result_2 = search_value(inventory, search_target_2)
    # Displays -1 because the linear search scanned the entire list without a match
    print(f"Searching for '{search_target_2}': Result code {result_2} (Not Found)")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using a highly out-of-bounds invalid index
    # Demonstrates that the program safely catches the invalid index and returns None without crashing.
    invalid_index = 99
    edge_delete_result = delete_at(inventory, invalid_index)
    print(f"Edge Case 1 - Deleting at invalid index {invalid_index}: Safe Return = {edge_delete_result}")

    # Edge Case 2: Perform operations on an empty list
    # Verifies that structural utilities handle an empty array smoothly.
    empty_list = []
    print(f"Created empty list: {empty_list}")

    # Try safe deletion from an empty list
    empty_delete_result = delete_at(empty_list, 0)
    print(f"Edge Case 2a - Deleting from empty list: Safe Return = {empty_delete_result}")

    # Try insertion into an empty list
    insert_at(empty_list, 0, "First Item")
    print(f"Edge Case 2b - Inserting into empty list at index 0: {empty_list}")


if __name__ == "__main__":
    main()