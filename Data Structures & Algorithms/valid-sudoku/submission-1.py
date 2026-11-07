class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        sub_boxes = defaultdict(list)

        valid_nums = set("123456789")

        # Iterate over rows
        for x, row in enumerate(board):

            # Iterate through row digits:
            for y, digit in enumerate(row):
                print(f"digit: {digit}, rows: {rows[x]}, columns: {cols[y]}")
                
                # Ensure valid digit
                if digit in valid_nums:
                    # Add numbers to dictionaries for rows and columns, unless the numbers already exist 
                    if digit in rows[x]:
                        print(f"duplicate: {digit} in row: {x+1}")
                        return False
                    rows[x].append(digit)

                    if digit in cols[y]:
                        print(f"duplicate: {digit} in column: {y+1}")
                        return False
                    cols[y].append(digit)

                    sub_box_idx_x = (x // 3)
                    sub_box_idx_y = (y // 3)

                    if digit in sub_boxes[sub_box_idx_x, sub_box_idx_y]:
                        print(f"duplicate: {digit} in sub_box: {sub_box_idx_x + 1, sub_box_idx_y + 1}")
                        return False
                    sub_boxes[sub_box_idx_x, sub_box_idx_y].append(digit)

        print(f"rows: {rows} columns: {cols}")


        return True
