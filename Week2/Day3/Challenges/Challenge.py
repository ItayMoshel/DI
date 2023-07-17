def can_i_afford_it(dic, fund):
    afford = []
    for key in dic.keys():
        if int(fund) >= int(dic[key]):
            afford.append(key)
    if len(afford) > 1:
        return sorted(afford)
    return "Nothing"


items_purchase = {
    "Water": "1",
    "Bread": "3",
    "TV": "1000",
    "Fertilizer": "20"
}

wallet = "300"
print(can_i_afford_it(items_purchase, wallet))

items_purchase1 = {
    "Apple": "4",
    "Honey": "3",
    "Fan": "14",
    "Bananas": "4",
    "Pan": "100",
    "Spoon": "2"
}

wallet1 = "100"
print(can_i_afford_it(items_purchase1, wallet1))

items_purchase2 = {
    "Phone": "999",
    "Speakers": "300",
    "Laptop": "5000",
    "PC": "1200"
}

wallet2 = "1"
print(can_i_afford_it(items_purchase2, wallet2))
