### String Methods

city = "aMsTeRDam"
print(city.upper())  # AMSTERDAM
print(city.lower())  # amsterdam
print(city.title())  # Amsterdam

city_2 = "sAn fRanCIsco"
print(city_2.capitalize())  # San francisco
print(city_2.swapcase())  # SaN FrANcISCO
print(city_2.title())  # San Francisco

### Strip Method

city_3 = "   Los Angeles   "
print(city_3.strip())  # Los Angeles
print(city_3.lstrip())
print(city_3.rstrip())

city_4 = "-+-+-London-+-+-"
print(city_4.strip("-"))  # +-+-London-+-+
print(city_4.strip("-+"))  # London => INTERESTING!
print(city_4.strip("+"))  # -+-+-London-+-+-

### Replace Method

races = '3km 5km 10km 21km 42km'
print(races.replace('km', 'CM'))  # 3CM 5CM 10CM 21CM 42CM
print(races.replace('km', 'CM', 1))  # 3CM 5km 10km 21km 42km

### Find Method

address = 'Amsterdam, Netherlands'
print(address.find('s'))  # 2
print(address.find('x'))  # -1
print(address.find('s', 2))  # 2
print(address.find('s', 3))  # 21
print(address.find('s', 3, 19))  # -1

### Count Method

sentence = 'Python is a programming language'
print(sentence.count('a'))  # 4
print(sentence.count('a', 0, 5))  # 0

### Method Chaining

city_5 = "   Los Angeles   "
print(city_5.strip().lower().replace(' ', '-'))  # los-angeles
