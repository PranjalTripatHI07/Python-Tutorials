#DATE - 18/1/2025
iron_man = {
    'name':'tony stark',
    'city':'new york'
}

bruce_van = {
    'name':'bat-man',
    'city':'new york'
}

peoples = [iron_man, bruce_van]

for people in peoples:
    print(f"\n People info :- {people}")


Dog = {
    'owner':'iron-man',
    'pet_type':'dog'
}

cat = {
    'owner':'bruce van',
    'pet_type':'cat'
}

pets = [Dog, cat]

for pet in pets:
    print(f"\n Pets info:- {pet}")


fav_places = {
    'iron-man':'new york',
    'bruce van':'japan',
    'steve roger':'uk',
    'hulk':'russia'

}

for name,place in fav_places.items():
    print(f"\n {name} your fav place is:- {place}")


fav_num = {
    'iron-man':[4,5,2,1],
    'bruce van':[2],
    'steve roger':[45,42],
    'hulk':[55,65,5,2,1]
}

for name,fav_number in fav_num.items():
    if len(fav_number) > 1:
        print(f"\n {name} your fav num are:- ")
    elif len(fav_number) <= 1:
        print(f"\n your fav num is:- ")
    for num in fav_number:
        print(f"\n {num}")




cities = {
    'new york':{
        'country':'usa',
        'population':'1200 Billion',
        'fact':'new your is IT hub of usa'
    },
    'seoul':{
        'country':'south-koria',
        'population':'100 Billion',
        'fact':'seoul is most beautiful city of south koria'
    },
    'tokyo':{
        'country':'japan',
        'population':'200 Billion',
        'fact':'tokyo is japan most populated city'
    }
}

for city,city_info in cities.items():
    print(f"\n city name :- {city}")
    info = f"Country:- {city_info['country']}, population:- {city_info['population']}, fact:- {city_info['fact']}"

    print(f"\n {info}")