class India():
    def capital(self):
        print("new delhi is the capital of India")
    def language(self):
        print("hindi is the most widest language spoken in India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("british english is the most widely language spoken in USA")
    def type(self):
        print("USA is a developed country")
I = India()
u = USA()
for country in (I,u):
    country.capital()
    country.language()
    country.type()



