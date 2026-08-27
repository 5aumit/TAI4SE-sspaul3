#!/usr/bin/env python
# coding: utf-8

# # Energy Generation 

# Imporing libraries

# In[1]:


from entsoe import EntsoePandasClient
import pandas as pd

from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()

import plotly.graph_objs as go
import plotly.figure_factory as ff


# Belgum solar data

# In[29]:


client = EntsoePandasClient(api_key='#######################')

start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180701', tz='Europe/Brussels')

country_code = 'BE'  # Belgium
# total energy generation

belgium=client.query_generation(country_code, start=start,end=end, psr_type=None)


# In[30]:


belgium.tail(10)


# In[31]:


trace0=go.Scatter(x=belgium.index,y=belgium['Wind Onshore'],name='Onshore Wind')

trace1=go.Scatter(x=belgium.index,y=belgium['Solar'],name='Solar')

data=[trace0,trace1]

layout={'title':'Belgum Wind energy VS Solar Energy, 2017-2018',
       'xaxis':{'title':'Date'},
       'yaxis':{'title':'Energy Generation'}}

iplot({'data':data,'layout':layout})


# 

# ## Energy Generation Forcast

# In[4]:


client = EntsoePandasClient(api_key='205f80f0-55c9-48aa-bd82-d603c4900119')

start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180201', tz='Europe/Brussels')

country_code = 'NO'  # Norway
# total energy generation

norway=client.query_generation_forecast(country_code, start=start,end=end)


# In[10]:


norway.head()


# In[11]:


trace1=go.Scatter(x=norway.index,y=norway,name='Solar')

data=[trace1]

layout={'title':'Norway Energy Forcast',
       'xaxis':{'title':'Date'},
       'yaxis':{'title':'Energy Generation'}}

iplot({'data':data,'layout':layout})


# In[ ]:




