class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Pass in_start to keep track of our absolute position in the original inorder list
        def dfs(pre, inor, in_start) -> Optional[TreeNode]:
            if not pre or not inor:
                return None

            root = TreeNode(pre[0])
            
            # 1. Calculate the local index using the absolute index and in_start
            local_mid = indices[pre[0]] - in_start

            # 2. Slice and recurse
            # Hint for root.left: The left subarray still starts at the exact same in_start!
            root.left = dfs(pre[1 : local_mid + 1], inor[: local_mid], in_start)
            
            # Hint for root.right: Where does the right subarray start in the original master list?
            # It starts just after the root node's absolute position.
            new_in_start_for_right = indices[pre[0]] + 1
            root.right = dfs(pre[local_mid + 1 :], inor[local_mid + 1 :], new_in_start_for_right)
            
            return root
        
        # The very first call starts at index 0 of the original master inorder list
        return dfs(preorder, inorder, 0)