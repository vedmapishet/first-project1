import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):

        self.__name_items = []

        self.__number_items = 0

        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}

        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property  # 1 геттер значения name_items
    def name_items(self):

        return self.__name_items

    @name_items.setter  # 1 сеттер для свойства grade
    def name_items(self, value):

        if value != None:

            self.__name_items = value

        else:
            self.__name_items = []

    @property  # 1 геттер значения number_items
    def number_items(self):

        return self.__number_items

    @number_items.setter  # 1 сеттер для свойства number_items
    def number_items(self, value):

        if value != 0:

            self.__number_items = value

        else:

            self.__number_items = 0

    @property
    def item_price(self):

        self.__item_price = item_price

    @property
    def tax_rate(self):

        self.__tax_rate = tax_rate

    def add_item_to_cheque(self, name):  # 2 добавляет товары в чек

        try:

            if (len(name) == 0) or (len(name) > 40):

                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

            elif (name not in self.__item_price):

                raise NameError('Позиция отсутствует в товарном справочнике')

            else:

                self.__name_items.append(name)

                self.__number_items += 1

        except Exception as e:

            print(e)

    def delete_item_from_check(self, name):  # 3 убирает товары из чека

        try:

            if name not in self.__name_items:

                raise NameError('Позиция отсутствует в чеке')

            else:

                self.__name_items.remove(name)

                self.__number_items -= 1



        except Exception as e:

            print(e)

    def check_amount(self):  # 4 считает общую сумму покупок

        total = []

        for item in self.__name_items:

            total.append(self.__item_price[item])

            if self.__number_items > 10:

                a = map(lambda x: x * 0.9, total)

            else:
                a = total

        return sum(a)

    def twenty_percent_tax_calculation(self):  # 5 рассчитывает НДС товаров, у которых налоговая ставка 20%

        twenty_percent_tax = []

        total = []

        for item in self.__name_items:

            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)

                total.append(self.__item_price[item])

            if self.__number_items > 10:

                a = map(lambda x: x * 0.9, total)

            else:

                a = total

        return sum(map(lambda x: x * 0.2, a))

    def ten_percent_tax_calculation(self):  # 6 рассчитывает НДС товаров, у которых ставка 10%

        ten_percent_tax = []

        total = []

        for item in self.__name_items:

            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

                total.append(self.__item_price[item])

            if self.__number_items > 10:

                a = map(lambda x: x * 0.9, total)

            else:

                a = total

        return sum(map(lambda x: x * 0.1, a))

    def total_tax(self):  # 7 возвращает общую сумму НДС по чеку

        total_tax = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

        return total_tax

    @staticmethod
    def get_telephone_number(telephone_number):  # 8 возвращает номер телефона покупателя

        try:

            if isinstance(telephone_number, int):

                if len(str(telephone_number)) == 10:

                    print(f'+7{telephone_number}')

                else:

                    raise ValueError



            else:

                raise TypeError

        except TypeError:

            print('Необходимо ввести цифры')

        except ValueError:

            print('Необходимо ввести 10 цифр после "+7"')

    @staticmethod
    def get_date_and_time():  # 9 возвращает дату и время покупки

        date_and_time = []

        now = str(datetime.datetime.now())

        year = lambda x: (x[:4])

        month = lambda x: (x[5:7])

        day = lambda x: (x[9:10])

        hours = lambda x: (x[11:13])

        minutes = lambda x: (x[14:16])

        date = [['часы', hours(now)], ['минуты', minutes(now)], ['день', day(now)], ['месяц', month(now)],
                ['год', year(now)]]

        for i in range(0, 5):
            a = date[i][0] + ': ' + date[i][1]

            date_and_time.append(a)

        return date_and_time


collector = OnlineSalesRegisterCollector()

collector.name_items = ['молоко', 'молоко', 'молоко', 'молоко', 'молоко', 'молоко', 'молоко', 'молоко', 'молоко',
                        'молоко', 'печенье']

collector.number_items = len(collector.name_items)

collector.add_item_to_cheque('чипсы')

print(collector.name_items, collector.number_items)

collector.delete_item_from_check('чипсы')

print(collector.name_items, collector.number_items)

print(collector.check_amount())

print(collector.twenty_percent_tax_calculation())

print(collector.ten_percent_tax_calculation())

print(collector.total_tax())

collector.get_telephone_number(9999999)

print(collector.get_date_and_time())




