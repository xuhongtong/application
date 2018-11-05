mobiles = [{'brand': 'Apple', 'model': 'IPHone4s', 'price': 4999.0, 'count': 3, 'version': '国行'},
           {'brand': 'Apple', 'model': 'IPHone4s', 'price': 4999.0, 'count': 3, 'version': '国行'}]


class Phone:
    def __init__(self, brand, model, price, count, version):
        self.brand = brand
        self.model = model
        self.price = price
        self.count = count
        self.version = version

    def show(self):
        print('''
--------------------------------------
手机信息管理系统
1.手机录入
2.根据手机品牌查询手机信息
3.查询全部手机信息
4.根据手机编号修改手机价格
5.根据手机编号删除手机记录
6.退出
--------------------------------------
                ''')

    def add(self):
        while True:
            self.brand = input('请输入手机品牌：')
            self.mobile = input('请输入手机型号：')
            self.price = input('请输入手机价格：')
            self.count = input('请输入手机数量：')
            self.version = input('请输入手机版本：')
            mobile = {'brand': self.brand, 'model': self.model, 'price': self.price, 'count': self.count,
                      'version': self.version}
            mobiles.append(mobile)
            P.show_all()
            a = input('是否继续添加？Y/N')
            if a == 'Y':
                continue
            else:
                break

    def show_brand(self):
        self.brand = input('请输入手机品牌：')
        for mobile in mobiles:
            if self.brand in mobile['brand']:
                print(mobile)
        P.show_all()

    def show_all(self):
        for num, mobile in enumerate(mobiles):
            print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(num + 1, mobile['brand'], mobile['model'], mobile['price'],
                                                        mobile['count'], mobile['version']))

    def modify(self):
        while True:
            num = int(input('请输入手机序号：'))
            self.price = int(input('请输入手机价格：'))
            if num <= len(mobiles):
                mobiles[num - 1]['price'] = self.price
            else:
                print('没有这个序号')
            P.show_all()
            a = input('是否继续修改？Y/N')
            if a == 'Y':
                continue
            else:
                break

    def remove(self):
        while True:
            num = int(input('请输入删除的手机序号：'))
            if num <= len(mobiles) - 1:
                mobiles.pop(num - 1)
            else:
                print('没有这个序号')
            P.show_all()
            a = input('是否继续修改？Y/N')
            if a == 'Y':
                continue
            else:
                break


P = Phone('sony', 'z3l55', 4999.0, 10, '智享版')

while True:
    P.show()
    bh = int(input('请输入编号:',))
    if bh == 1:
        P.add()
    elif bh == 2:
        P.show_brand()
    elif bh == 3:
        P.show_all()
    elif bh == 4:
        P.modify()
    elif bh == 5:
        P.remove()
    elif bh == 6:
        break
