import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
import seaborn as sns
from scipy import stats
import io
import os
import zipfile
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from scipy import stats


def main():

    path="~/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv"
    if not os.path.exists(path):
        path1 = kagglehub.dataset_download("yasserh/housing-prices-dataset", force_download=True)
    fig, ax = plt.subplots()
    df = pd.read_csv(path)

    # fig, ax = plt.subplots()
    #df = pd.read_csv(path)
    # df.hist(figsize=(20,10), ax=ax)
    # st.pyplot(fig)


    st.title("Factors Effecting House Prices")
    le = LabelEncoder()

    df_encoded=df.copy()
    df_encoded['furnishingstatus']=le.fit_transform(df_encoded['furnishingstatus'])
    categorical_columns= df_encoded.select_dtypes(include=['object']).columns.tolist()

    encoder= OneHotEncoder()

    one_hot_encoded=encoder.fit_transform(df_encoded[categorical_columns])

    dummies_df= pd.DataFrame(one_hot_encoded.toarray(), columns=encoder.get_feature_names_out(categorical_columns))

    df_encoded= pd.concat([df_encoded,dummies_df],axis=1)

    df_encoded=df_encoded.drop(categorical_columns,axis=1)



    #row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns((0.1, 1, 0.1, 1, 0.1))


    z_scores = stats.zscore(df_encoded[['price', 'area']], axis=0)

    condition = (z_scores > -3) & (z_scores < 3)

    row_condition = condition.all(axis=1)
    data_filtered = df_encoded[row_condition]


    plot=sns.relplot(x='area', y='price', hue='furnishingstatus', data=data_filtered, palette='muted', style='furnishingstatus')
    st.pyplot(plot.figure)



    

