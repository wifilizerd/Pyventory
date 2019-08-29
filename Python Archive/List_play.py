add_col = 4
test_list = [['1','a','b','c',''],
             ['2','a','b','c',''],
             ['3','a','b','c',''],
             ['4','a','b','c',''],
             ['5','a','b','c','']
            ]


for row in test_list:
    if row[0] == '2':
        print(row)
        row[add_col] = 'working'
        print(row)