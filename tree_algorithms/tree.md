# Binary Tree Algorithms Guide

This guide outlines the steps to implement and test each binary tree algorithm. Each algorithm should be placed in its own `.py` file as described below.

---

## Steps for Setting Up and Testing Each Algorithm

1. **Create Files for Each Algorithm:**
   - Make a separate `.py` file for each algorithm:
     - `tree_traversal.py`
     - `check_balanced.py`
     - `lowest_common_ancestor.py`
     - `check_bst.py`
     - `tree_diameter.py`
     - `invert_tree.py`
     - `serialize_deserialize.py`
     - `build_tree_from_traversals.py`

2. **Add the Code for Each Algorithm:**
   - Copy and paste the respective code into each file (refer to code snippets above).

3. **Define Test Cases:**
   - In each `.py` file, add a simple `if __name__ == "__main__":` block for basic testing.
   - Example:
     ```python
     if __name__ == "__main__":
         # Create a sample tree and test the function
         root = TreeNode(1)
         root.left = TreeNode(2)
         root.right = TreeNode(3)
         # Call the function and print the result
         print(preorder_traversal(root))
     ```

4. **Run Each Script:**
   - Execute each file independently in the terminal or IDE to verify the algorithm’s output.
   - Example:
     ```bash
     python tree_traversal.py
     ```

5. **Optional - Organize Tests:**
   - Create a `tests/` directory to store additional test cases for thorough validation.

6. **Document Results:**
   - Record observations or modify the code based on testing outcomes. 

---

## Summary of Algorithms and Files

- `tree_traversal.py`: In-order, Pre-order, Post-order, Level-order traversals, and Max Depth calculation.
- `check_balanced.py`: Checks if a tree is balanced.
- `lowest_common_ancestor.py`: Finds the LCA of two nodes.
- `check_bst.py`: Verifies if a tree is a valid BST.
- `tree_diameter.py`: Calculates the diameter (longest path) of the tree.
- `invert_tree.py`: Inverts (mirrors) the tree.
- `serialize_deserialize.py`: Serializes and deserializes a tree.
- `build_tree_from_traversals.py`: Builds a tree from given In-order and Pre-order traversals.

---

Use this guide to structure each algorithm file, test functionality, and ensure correctness.
