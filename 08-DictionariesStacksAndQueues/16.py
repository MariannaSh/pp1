Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    # hotel_name=hotels['name']
    list_names=''
    for hotels in hotels :
        list_names+=hotels['name']+", "
    return list_names[:-2]

def avg_price(hotels):
    summa=0
    count=0
    for hotels in hotels:
        summa+=hotels['price']
        count+=1
    return int(summa/count)

print("Hotels in Krakow: ",hotel_list(Hotels_in_Krakow))
print("Average hotel price in Krakow: ", avg_price(Hotels_in_Krakow))
print()

print("Hotels in Sopot: ",hotel_list(hotels_in_Sopot))
print("Hotels in Sopot: ",avg_price(hotels_in_Sopot))

if avg_price(Hotels_in_Krakow) > avg_price(hotels_in_Sopot):
    print('Hotel in Sopot cheaper')
else:
    print('Hotel in Krakow cheaper')