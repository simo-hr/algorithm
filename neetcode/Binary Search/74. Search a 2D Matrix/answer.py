# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for m in matrix:
#             for n in m:
#                 if n == target:
#                     return True

#         return False

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         col_l = 0
#         col_r = len(matrix) - 1
#         while col_l <= col_r:
#             col_mid = math.floor((col_l + col_r) / 2)
#             row = matrix[col_mid]
#             if(row[-1] < target):
#                 col_l = col_mid + 1
#             elif (row[0] > target):
#                 col_r = col_mid -1
#             else:
#                 row_l = 0
#                 row_r = len(row) - 1
#                 while row_l <= row_r:
#                     row_mid = math.floor((row_l + row_r) / 2)
#                     if row[row_mid]  == target:
#                         return True
#                     elif row[row_mid] < target:
#                         row_l = row_mid + 1
#                     else:
#                         row_r = row_mid - 1
#         return False
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for m in matrix:
#             for n in m:
#                 if n == target:
#                     return True

#         return False

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         col_l = 0
#         col_r = len(matrix) - 1
#         while col_l <= col_r:
#             col_mid = math.floor((col_l + col_r) / 2)
#             row = matrix[col_mid]
#             if(row[-1] < target):
#                 col_l = col_mid + 1
#             elif (row[0] > target):
#                 col_r = col_mid -1
#             else:
#                 break

#         if not col_l <= col_r:
#             return False

#         row_l = 0
#         row_r = len(row) - 1
#         while row_l <= row_r:
#             row_mid = math.floor((row_l + row_r) / 2)
#             if row[row_mid]  == target:
#                 return True
#             elif row[row_mid] < target:
#                 row_l = row_mid + 1
#             else:
#                 row_r = row_mid - 1
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (m*n) - 1

        while l <= r:
            mid = (l + r) // 2
            i, j = divmod(mid, m)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False