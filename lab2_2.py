
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mydb = client["laba2"]
mydb.drop_collection("shop")
mycol = mydb["shop"]

#1
one_doc = { "title": "Шарманка",
        "category" : "Футболка",
        "producer": "Бангладеш инкорпорейшон", 
        "price" : 1000,
        "features" : [
            {
                "color" : "Голубой",
                "size" : "XXL",
                "type" : "Оверсайз"
            }] ,
            "customers":[
                {"name": "Николай Басков", "date":"01.10.22", "rewiev": "Супер пупер!", "delivery": "Почта России"},
                {"name": "Дмитрий Песков", "date":"10.10.22", "rewiev": "Удобненько", "delivery": "Кремлевский экспресс"},
                {"name": "Вера Брежнева", "date":"05.11.22", "rewiev": "Какая отвратительная футболка, возврат!", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#2
one_doc = { "title": "Карамба",
        "category" : "Носки",
        "producer": "Гучи", 
        "price" : 5000,
        "features" : [
            {
                "color" : "Розовый",
                "size" : "XS",
                "type" : "Длинные"
            }] ,
            "customers":[
                {"name": "Николай Валуев", "date":"08.09.22", "rewiev": "Нормально", "delivery": "Кремлевский экспресс"},
                {"name": "Педро Санчес", "date":"13.10.22", "rewiev": "Muy bien", "delivery": "Яндекс деливери"},
                {"name": "Дмитрий Песков", "date":"19.09.22", "rewiev": "Очень нравится", "delivery": "Кремлевский экспресс"},
            ]
}
mycol.insert_one(one_doc)
#3
one_doc = { "title": "Советские зори",
        "category" : "Пижама",
        "producer": "Белорусский трикотаж", 
        "price" : 1500,
        "features" : [
            {
                "color" : "Голубой",
                "size" : "S",
                "type" : "Оверсайз"
            }] ,
            "customers":[
                {"name": "Лолита Милявская", "date":"18.11.22", "rewiev": "Мягкая, хорошая", "delivery": "Почта России"},
                {"name": "Ефимова Дарья", "date":"01.11.22", "rewiev": "Хювя!", "delivery": "Яндекс деливери"},
                {"name": "Альберт Эйнштейн", "date":"11.10.22", "rewiev": "E=mc^2", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#4
one_doc = { "title": "Мечта",
        "category" : "Футболка",
        "producer": "Советские зори", 
        "price" : 600,
        "features" : [
            {
                "color" : "Синий",
                "size" : "M",
                "type" : "Приталенная"
            }] ,
            "customers":[
                {"name": "Криштиану Роналду", "date":"01.11.22", "rewiev": "Good for football", "delivery": "Яндекс деливери"},
                {"name": "Петр Первый", "date":"09.09.22", "rewiev": "Лепота", "delivery": "Кремлевский экспресс"},
                {"name": "Банковская Софья", "date":"20.11.22", "rewiev": "Для танцев просто супер!", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#5
one_doc = { "title": "Жу-жу",
        "category" : "Носки",
        "producer": "Советские зори", 
        "price" : 150,
        "features" : [
            {
                "color" : "Красный",
                "size" : "L",
                "type" : "Средние"
            }] ,
            "customers":[
                {"name": "Валерий Меладзе", "date":"18.09.22", "rewiev": "Красиииво они вошли в мою грешную жизнь", "delivery": "Кремлевский экспресс"},
                {"name": "Тамара Гверцителле", "date":"23.10.22", "rewiev": "Отлично", "delivery": "Почта России"},
                {"name": "Александра Донова", "date":"20.09.22", "rewiev": "Gut", "delivery": "Яндекс деливери"},
                {"name": "Банковская Софья", "date":"22.09.22", "rewiev": "Gracias!!", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#6
one_doc = { "title": "Фешон",
        "category" : "Нижнее белье",
        "producer": "Прада", 
        "price" : 3000,
        "features" : [
            {
                "color" : "Красный",
                "size" : "XS",
                "type" : "Кружевное"
            }] ,
            "customers":[
                {"name": "Иван Иванов", "date":"01.09.22", "rewiev": "Норм", "delivery": "Почта России"},
                {"name": "Тамара Петрова", "date":"23.10.22", "rewiev": "Отлично", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#7
one_doc = { "title": "Лидия",
        "category" : "Нижнее белье",
        "producer": "ООО Лидия", 
        "price" : 1000,
        "features" : [
            {
                "color" : "Синий",
                "size" : "XL",
                "type" : "Обычное"
            }] ,
            "customers":[
                {"name": "Семен Семенов", "date":"02.09.22", "rewiev": "Нормально", "delivery": "Служба доставки Стриж"},
                {"name": "Елена Петрова", "date":"03.11.22", "rewiev": "Хорошо", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#8
one_doc = { "title": "Фантази",
        "category" : "Шорты",
        "producer": "Бангладеш инкорпорейшон", 
        "price" : 1200,
        "features" : [
            {
                "color" : "Синий",
                "size" : "XL",
                "type" : "Джинсовые"
            }] ,
            "customers":[
                {"name": "Дмитрий Медведев", "date":"03.09.22", "rewiev": "Заслуживает доверия", "delivery": "Кремлевский экспресс"},
                {"name": "Виктор Павлов", "date":"04.11.22", "rewiev": "Найс", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#9
one_doc = { "title": "Фантазия",
        "category" : "Майка",
        "producer": "Бангладеш инкорпорейшон", 
        "price" : 900,
        "features" : [
            {
                "color" : "Белый",
                "size" : "XS",
                "type" : "База"
            }] ,
            "customers":[
                {"name": "Николай Валуев", "date":"05.09.22", "rewiev": "Круть", "delivery": "Кремлевский экспресс"},
                {"name": "Людмила Семенова", "date":"07.11.22", "rewiev": "Хорошенькая маечка", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#10
one_doc = { "title": "Бархат",
        "category" : "Кофта",
        "producer": "ООО Лидия", 
        "price" : 1900,
        "features" : [
            {
                "color" : "Черный",
                "size" : "S",
                "type" : "Оверсайз"
            }] ,
            "customers":[
                {"name": "Филипп Киркоров", "date":"06.09.22", "rewiev": "Красота!", "delivery": "Кремлевский экспресс"},
                {"name": "Алла Пугачева", "date":"10.11.22", "rewiev": "Хорошенькая кофточка", "delivery": "Кремлевский экспресс"},
            ]
}
mycol.insert_one(one_doc)
#11
one_doc = { "title": "Радуга",
        "category" : "Штаны",
        "producer": "ООО Лидия", 
        "price" : 2200,
        "features" : [
            {
                "color" : "Черный",
                "size" : "M",
                "type" : "Слоучи"
            }] ,
            "customers":[
                {"name": "Петр Петров", "date":"06.09.22", "rewiev": "Мне не понравились", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#12
one_doc = { "title": "Мир",
        "category" : "Кофта",
        "producer": "ООО Лидия", 
        "price" : 1000,
        "features" : [
            {
                "color" : "Голубой",
                "size" : "M",
                "type" : "Приталенный"
            }] ,
            "customers":[
                {"name": "Петр Петров", "date":"06.10.22", "rewiev": "Мне не зашло", "delivery": "Яндекс деливери"},
                {"name": "Андрей Петров", "date":"07.10.22", "rewiev": "Мне зашло", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#13
one_doc = { "title": "Фамилья",
        "category" : "Носки",
        "producer": "Зара", 
        "price" : 200,
        "features" : [
            {
                "color" : "Красный",
                "size" : "S",
                "type" : "Короткий"
            }] ,
            "customers":[
                {"name": "Нина Круглова", "date":"16.10.22", "rewiev": "Мне не понравилось", "delivery": "Почта России"},
                {"name": "Иван Ургант", "date":"09.10.22", "rewiev": "Красивые", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#14
one_doc = { "title": "Немо",
        "category" : "Носки",
        "producer": "ООО Клоутс", 
        "price" : 250,
        "features" : [
            {
                "color" : "Черный",
                "size" : "S",
                "type" : "Длинный"
            }] ,
            "customers":[
                {"name": "Алексей Сыров", "date":"17.11.22", "rewiev": "Удобные", "delivery": "Служба доставки Стриж"},
                {"name": "Вера Ефимова", "date":"29.10.22", "rewiev": "Буду носить с удовольствием", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)
#15
one_doc = { "title": "Дрим",
        "category" : "Футболка",
        "producer": "ООО Клоутс", 
        "price" : 1100,
        "features" : [
            {
                "color" : "Черный",
                "size" : "S",
                "type" : "Укороченная"
            }] ,
            "customers":[
                {"name": "Николай Дроздов", "date":"27.10.22", "rewiev": "Хорошие", "delivery": "Служба доставки Стриж"},
                {"name": "Вера Вершинина", "date":"30.10.22", "rewiev": "Буду носить с радостью", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#16
one_doc = { "title": "Тим",
        "category" : "Майка",
        "producer": "ООО Клоутс", 
        "price" : 1000,
        "features" : [
            {
                "color" : "Белый",
                "size" : "S",
                "type" : "Укороченная"
            }] ,
            "customers":[
                {"name": "Андрей Аршавин", "date":"10.09.22", "rewiev": "Для футбола супер", "delivery": "Служба доставки Стриж"},
            ]
}
mycol.insert_one(one_doc)
#17
one_doc = { "title": "Мое",
        "category" : "Шорты",
        "producer": "ООО Семерочка", 
        "price" : 2000,
        "features" : [
            {
                "color" : "Зеленый",
                "size" : "XXL",
                "type" : "Зауженные"
            }] ,
            "customers":[
                {"name": "Максим Галкин", "date":"11.09.22", "rewiev": "На работу пойду в них", "delivery": "Яндекс деливери"},
            ]
}
mycol.insert_one(one_doc)
#18
one_doc = { "title": "Твое",
        "category" : "Нижнее белье",
        "producer": "ООО Семерочка", 
        "price" : 2500,
        "features" : [
            {
                "color" : "Зеленый",
                "size" : "XXS",
                "type" : "Спортивный"
            }] ,
            "customers":[
                {"name": "Сергей Светлаков", "date":"01.09.22", "rewiev": "Мягенькое", "delivery": "Служба доставки Стриж"},
            ]
}
mycol.insert_one(one_doc)
#19
one_doc = { "title": "Найс дей",
        "category" : "Нижнее белье",
        "producer": "Виктория Сикрет", 
        "price" : 4500,
        "features" : [
            {
                "color" : "Розовый",
                "size" : "XS",
                "type" : "Элегантный"
            }] ,
            "customers":[
                {"name": "Мария Авдеева", "date":"01.10.22", "rewiev": "Очень элегантное", "delivery": "Служба доставки Стриж"},
            ]
}
mycol.insert_one(one_doc)
#20
one_doc = { "title": "Виктория",
        "category" : "Нижнее белье",
        "producer": "Виктория Сикрет", 
        "price" : 5500,
        "features" : [
            {
                "color" : "Черный",
                "size" : "S",
                "type" : "База"
            }] ,
            "customers":[
                {"name": "Лолита Милявская", "date":"01.11.22", "rewiev": "Куплю здесь еще", "delivery": "Кремлевский экспресс"},
                {"name": "Леонид Агутин", "date":"11.11.22", "rewiev": "Жене понравилось", "delivery": "Кремлевский экспресс"},
                {"name": "Дмитрий Дибров", "date":"26.10.22", "rewiev": "Доставили быстро", "delivery": "Почта России"},
            ]
}
mycol.insert_one(one_doc)


def replaceFeatures(target_str):
    replace_values = {"color": "Цвет", "size": "Размер", "type":"Тип","title":"Название","price":"Цена", "producer":"Производитель"}
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str


def showProductsByCategory(category):
# 1.Получить список названий товаров, относящихся к заданной категории;
    myquery = { "category": { "$eq": f"{category}" } }
    mydoc = mycol.find(myquery)
    print("1.Получить список названий товаров, относящихся к заданной категории;")
    for x in mydoc:
        print(x["title"])

def showProductFeatureByCategory(category):
# 2.Получить список характеристик товаров заданной категории;
    myquery = { "category": { "$eq": f"{category}" } }
    mydoc = mycol.find(myquery)
    print("2.Получить список характеристик товаров заданной категории;")
    for x in mydoc:
        print("Характеристики товара " + x["title"]+":")
        for y in x["features"]:
            for z in y:

                print(replaceFeatures(z)+ " : "+y[z])
        print(" ")


def showNamesAndPricesByCustomer(customer):
# 3.Получить список названий и стоимости товаров, купленных заданным покупателем;
    myquery = mycol.aggregate([
    #{"$unwind" : "$customers"},
    {"$match": {"customers.name" : f"{customer}"}},
    {"$project" : {"_id" : 0, "title" : 1, "price" : 1}}
    ])
    print("3.Название, стоимость товара для заданного покупателя: ")
    for item in myquery:
        for i in item:
            print(replaceFeatures(i)+" : "+str(item[i]))
        print(" ")
    myquery.close()


def showTitlesProducersPricesByColor(color):
# 4.Получить список названий, производителей и цен на товары, имеющие заданный цвет;
    myquery = mycol.aggregate([
    #{"$unwind" : "$customers"},
    {"$match": {"features.color" : f"{color}"}},
    {"$project" : {"_id" : 0, "title" : 1, "producer" : 1, "price" : 1}}
    ])

    print("4.Список названий, производителей и цен на товары, имеющие заданный цвет: ")
    for item in myquery:
        for i in item:
            print(replaceFeatures(i)+" : "+str(item[i]))
        print(" ")
    myquery.close()

def getTotalAmount():

    myquery = mycol.aggregate([
    {"$unwind" : "$customers"},
    {"$group": {"_id": "null", "summa" :
    {"$sum": "$price"}}},
    {"$project" : {"_id" : 0, "summa" : 1}}
    ])

    print("5.Получить общую сумму проданных товаров;")
    for item in myquery:
        print("Общая сумма = ",item["summa"])


def showAmountOfProductsInEachCategory():
# 6.Получить количество товаров в каждой категории;
    myquery = mycol.aggregate([
    {"$group": {"_id": "$category", "count" :
    {"$sum": 1}},}
    ])


    print("6.Получить количество товаров в каждой категории")
    for item in myquery:
        print(item["_id"]+":"+str(item["count"]))

def showListOfCustomersByTitle(title):
# 7. Получить список имен покупателей заданного товара;
    myquery = mycol.aggregate([

    {"$match": {"title" : f"{title}"}},
    {"$project" : {"_id" : 0, "customers.name" : 1}}
    ])
    print("7. Получить список имен покупателей заданного товара;")
    for item in myquery:
        for i in item:
            for y in item[i]:
                for z in y:
                    print("Имя: "+ y[z])

def showCustomersByTitleAndDelivery(title,delivery):
# 8. Получить список имен покупателей заданного товара, с доставкой фирмы с заданным названием.
    myquery = mycol.aggregate([
        {"$match": {"title" : f"{title}"}},
        {"$unwind" : "$customers"},
        {"$match": {"customers.delivery" : f"{delivery}"}},
        {"$replaceRoot": {"newRoot": {"name":"$customers.name"}}},
        # {"$project" : {"_id" : 0, "customers.name" : 1}}
        ])
    print("8. Получить список имен покупателей заданного товара, с доставкой фирмы с заданным названием.")
    for item in myquery:
        for i in item:
            print("Имя: " + item[i])




def main():
    print("Ведите номер запроса")
    a = input()

    if (a==str(1)):
        print("Введите категорию")
        b=input()
        showProductsByCategory(b)

    elif (a==str(2)):
        print("Введите категорию")
        b=input()
        showProductFeatureByCategory(b)

    elif (a==str(3)):
        print("Введите имя покупателя")
        b=input()
        showNamesAndPricesByCustomer(b)

    elif (a==str(4)):
        print("Введите цвет")
        b=input()
        showTitlesProducersPricesByColor(b)

    elif (a==str(5)):
        print("Общая сумма: ")
        getTotalAmount()

    elif (a==str(6)):
        showAmountOfProductsInEachCategory()

    elif (a==str(7)):
        print("Введите название товара: ")
        b=input()
        showListOfCustomersByTitle(b)

    elif (a==str(8)):
        print("Введите название товара и название фирмы доставки: ")
        print("Название товара: ")
        b=input()
        print("Название доставки: ")
        c = input()
        showCustomersByTitleAndDelivery(b,c)



if __name__ == "__main__":
	main()




