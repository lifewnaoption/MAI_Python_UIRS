import re

num_to_let, let_to_num = {},{}
for num in range(1,27):
    num_to_let[num] = chr(ord("A")+num-1)
    let_to_num[chr(ord("A")+num-1)] = num

def spreadsheet(s):
    print("S",s)
    if len(re.findall("\d+",s)) == 2:
        row, col_num = re.findall("\d+",s)
        col_num, col = int(col_num,), ""
        while col_num:
            col_num, mod = divmod(col_num,26)          
            if mod == 0:
                col_num = col_num - 1
                mod = 26                
            col =  num_to_let[mod] + col
        print (row,col)
        
        return col + row
    else:
        col_let, row = re.findall("[A-Z]+|\d+",s)
        col = 0
        while col_let:
            col = col*26 + let_to_num[col_let[0]]
            col_let = col_let[1:]
        return "R" + row + "C" + str(col)