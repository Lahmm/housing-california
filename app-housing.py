import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-bright')

st.title('California Housing Data(1990) by Haobo Yang')

# read the file
df_housing = pd.read_csv('housing.csv')

# create a slider 
median_house_value_filter = st.slider('Median House Value', 0, 500001, 200000)

# create a multi select
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the loation type',
     df_housing.ocean_proximity.unique(),  
     df_housing.ocean_proximity.unique())

# create a radio select
median_income_filter = st.sidebar.radio(
     label='Choose income level',
     options=('Low', 'Medium', 'High', 'All'),
     horizontal=True,
)


# filter 1: select by price (slider)
df_housing_high = df_housing[df_housing.median_house_value >= median_house_value_filter]

# filter 2: select by pricr (hist)
df_housing_low = df_housing[df_housing.median_house_value <= median_house_value_filter]

# filter 3: choose by the ocean proximity
df_housing_high = df_housing_high[df_housing_high.ocean_proximity.isin(ocean_proximity_filter)]
df_housing_low = df_housing_low[df_housing_low.ocean_proximity.isin(ocean_proximity_filter)]

# filter 4: choose by the income level
if median_income_filter == 'Low':
     df_housing_high = df_housing_high[df_housing_high.median_income <= 2.5]
     df_housing_low = df_housing_low[df_housing_low.median_income <= 2.5]
elif median_income_filter == 'Medium':
     df_housing_high = df_housing_high[df_housing_high.median_income <= 4.5]
     df_housing_low = df_housing_low[df_housing_low.median_income <= 4.5]
elif median_income_filter == 'High':
     df_housing_high = df_housing_high[df_housing_high.median_income > 4.5]
     df_housing_low = df_housing_low[df_housing_low.median_income > 4.5]
else:
     pass
# map
st.subheader('See more filters in the sidebar:')
st.map(df_housing_high)

# histogram
st.subheader('Histogram of the Median House value')
fig, ax = plt.subplots(figsize=(15, 10))
df_housing_low.median_house_value.hist(bins=30)
st.pyplot(fig)