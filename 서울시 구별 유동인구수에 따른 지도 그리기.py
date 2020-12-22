#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


population = pd.read_csv('./population07.csv')
population


# In[5]:


# 칼럼 목록
list(population)


# In[6]:


# 칼럼 값의 종류추출
set(population['연령대(10세단위)'])


# In[7]:


set(population['시'])


# In[9]:


set(population['군구']), len(set(population['군구']))


# In[16]:


# 군구별로 데이터 묶고 유동인구수 합 구하기
sum_populationo_by_gu = population.groupby('군구')['유동인구수'].sum()
sorted_sum_populationo_by_gu = sum_populationo_by_gu.sort_values(ascending=False)


# In[14]:


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'


# In[17]:


# 그래프 그리기
plt.figure(figsize=(10,5))
plt.bar(sorted_sum_populationo_by_gu.index, sorted_sum_populationo_by_gu)
plt.title('2020년 7월 서울 군구별 유동인구 수')
plt.xlabel('군구')
plt.ylabel('유동인구 수(명)')
plt.xticks(rotation=-45)
plt.show()


# In[21]:


# 군구가 강남인 데이터만 추출
population_gangnam = population[ population['군구'] == '강남구']
population_gangnam


# In[23]:


# 강남의 일자별 유동인구 수 구하기
population_gangnam_daily = population_gangnam.groupby('일자')['유동인구수'].sum()
population_gangnam_daily


# In[25]:


# 선 그래프 그리기
plt.figure(figsize=(10,5))

date = []
for day in population_gangnam_daily.index:
    date.append(str(day))

plt.plot(date, population_gangnam_daily)
plt.title('2020년 7월 강남구 날짜별 유동인구 수')
plt.xlabel('날짜')
plt.ylabel('유동인구 수(천만명)')
plt.xticks(rotation = - 90)
plt.show()


# In[26]:


import folium
import json


# In[33]:


# 단순화된 지도 가져오기
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='stamentoner')
map

# 서울시 지리정보 가져오기
seoul_state_geo = './seoul_geo.json'
geo_data = json.load(open(seoul_state_geo, encoding='utf-8'))

# 지도(map)에 가져온 지리정보 넣고 표현하기
folium.Choropleth(geo_data=geo_data,
                data=sum_populationo_by_gu,
                colums=[sum_populationo_by_gu.index, sum_populationo_by_gu],
                fill_color='PuRd',
                key_on='properties.name').add_to(map)
map


# In[ ]:




