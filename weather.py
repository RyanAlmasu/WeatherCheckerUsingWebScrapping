#Program Maker = Ryan Almasu 
from requests_html import HTMLSession
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class App:
    
    def get_weather(self):
        
        try:
            
            self.user = input(str('Please select the list (1)(2) : '))
            self.query = input("Input the location / Press ctrl+c for Quit: ")
            y = HTMLSession()
            url = f'https://www.google.com/search?q=weather+{self.query}'
            z = y.get(url , headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
            self.temp = z.html.find("span#wob_tm" , first=True).text
            self.tempinc = z.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
            self.desc = z.html.find("div.wob_dcp" , first=True).find("span#wob_dc" , first=True).text
            self.city_time = z.html.find("div.wob_dts" , first=True).text
            self.time = datetime.now()
            self.current_time = self.time.strftime("%H:%M:%S, %b %d %Y")
            print(f'The weather from {self.query} is {self.temp}{self.tempinc} {self.desc} in {self.city_time} recorded on {self.current_time}')
            
        except KeyboardInterrupt:
            
            pass
            
    def export_excel(self):
        
        try:
            
            df = [[self.query , self.city_time , self.temp, self.tempinc , self.desc , self.current_time]]
            dff =  pd.DataFrame(df , columns=["Location" , "City Time" , "Temp" , "Temp Type" , "Condition" , "Recorded On"])
            for i in self.user:
                i = dff
                i.to_csv("User Log.csv" , mode='a' , index=False  , header=False)
                
        except:
            
            pass

    def visualize(self):
        
        try:
            
            data = pd.read_csv("User Log.csv")
            result = data["Location"].sort_values()
            temp = data["Temp"]
            plt.bar(result , temp)
            plt.xticks(rotation=45)
            plt.xlabel("Location")
            plt.ylabel("In Celcius")
            plt.show()
            
        except:
            
            pass
a = App()
print("Welcome to my App")
print("1. Check Weather")
print('2. Quit')
a.get_weather()
a.export_excel()
a.visualize()

    