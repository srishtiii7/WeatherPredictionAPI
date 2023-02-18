
# In[2]:


from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Daily,Point
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


start = datetime(2013, 1, 1)
end = datetime.now()
#coordinates,elevation of Pune
pune= Point(18.5204,73.8567,560)

data = Daily(pune, start, end)
data = data.fetch()

df = pd.DataFrame(data)
df.to_csv("2022data.csv")


# In[3]:


weather=df[["tmax","tmin","tavg","prcp","wdir","wspd","pres"]]



# In[4]:




# In[6]:


#Renamed the columns
weather.columns=["Max_Temp","Min_Temp","Avg_Temp","Prcp","Wnd_Dir","Wind_Speed","Pressure"]



# In[7]:


#Calculated the null values
weather.apply(pd.isnull).sum()/weather.shape[0]


# In[8]:


weather=weather.fillna(weather.mean())



# In[9]:


weather.apply(pd.isnull).sum()/weather.shape[0]


# In[10]:


weather = weather.rename_axis('date').reset_index()



# In[11]:


weather[["Max_Temp","Min_Temp"]].plot(figsize=(15,10))


# In[12]:


#Set the target temperature to the max temprature of next day
weather["target"]=weather.shift(-1)["Max_Temp"]


# In[13]:




# In[14]:


weather=weather.iloc[:-1,:].copy()


# In[15]:





# In[16]:


weather['date']=pd.to_datetime(weather['date'],format='%y-%m-%d')
weather['year']=weather['date'].dt.year
weather['month']=weather['date'].dt.month



# In[17]:


plt.style.use('fivethirtyeight')
plt.figure(figsize=(15,10))
plt.title("Temperature change in Pune over the years")
sns.lineplot(data=weather,x='month',y='Max_Temp',hue='year')



# In[18]:


forecast_data = weather.rename(columns = {"date": "ds", 
                                       "Max_Temp": "y"})



# In[ ]:





# In[19]:



from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)




# In[20]:



# In[21]:





# In[22]:


df1 = pd.DataFrame(predictions)
df2 = df1[['ds','yhat']]
df2['ds'] = df2['ds'].astype(str)


# In[23]:


def predict_tmax(d):
  #date = input("The data you want to forecast for : ")
  for i in range(len(df2)):
    if(d == df2['ds'][i]):
         a = str(df2['yhat'][i])
         return a

# In[24]:
       # print("Max Temperature : " + 
              #str(df2['yhat'][i]))




# In[25]:


# In[26]:


#def mse(predictions, actual_label="actual_val", pred_label="yhat"):
#   se = ((predictions[actual_label] - predictions[pred_label]) ** 2)
#  print(se.mean())
    
#mse(predictions)
#print(mse)   


# In[ ]:





# In[ ]:




