while True:
    print('----------------')
    print('1. 加法')
    print('2. 減法')
    print('3. 乘法')
    print('4. 除法')
    print('5. 離開')
    sel=int(input('使用選項 :'))
    if sel==1:
        A=int(input('輸入 :'))
        B=int(input('輸入 :'))
        print(A+B)
    if sel==2:
        A=int(input('輸入 :'))
        B=int(input('輸入 :'))
        print(A-B)
    if sel==3:
        A=int(input('輸入 :'))
        B=int(input('輸入 :'))
        print(A*B)
    if sel==4:
        A=int(input('輸入 :'))
        B=int(input('輸入 :'))
        print(A/B)
    if sel==5:
        print('離開')
        break