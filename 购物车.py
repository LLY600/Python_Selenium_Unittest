#_*_coding:utf-8_*_
#@Author:LLY

product_list=[
    ('mac', 9999),
    ('kindle', 999),
    ('TSL', 999999),
    ('Book', 10),
    ('bike', 1500),
]

saving = input('input saving:')
shopping_car = []
if saving.isdigit():
    saving = int(saving)
    while True:
        for i, j in enumerate(product_list, 1):
            print(i, ',', j)
        choice = input('购买商品编号[退出:q]：')
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(product_list):
                p_item = product_list[choice-1]
                print(p_item)
                if p_item[1] < saving:
                    saving -= p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，剩余 %s' % saving)
            else:
                print('商品编码不存在')
        elif choice == 'q':
            print('你已购买如下商品')
            for i in shopping_car:
                print(i)
            print('剩余%s RMB' % saving)
            break
        else:
            print('非法输入')

