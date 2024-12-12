def main():
    import pandas as pd
    from scipy import stats
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    from joblib import dump
    
    df = pd.read_csv("pages/housing-prices-dataset.zip")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    le = LabelEncoder()

    df_encoded=df.copy()
    df_encoded['furnishingstatus']=le.fit_transform(df_encoded['furnishingstatus'])

    categorical_columns= df_encoded.select_dtypes(include=['object']).columns.tolist()

    encoder= OneHotEncoder(sparse_output=False) # if running on colab

    one_hot_encoded=encoder.fit_transform(df_encoded[categorical_columns])

    dummies_df= pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

    df_encoded= pd.concat([df_encoded,dummies_df],axis=1)

    df_encoded=df_encoded.drop(categorical_columns,axis=1)


    z_scores = stats.zscore(df_encoded[['price','area']], axis=0)

    condition = (z_scores > -3) & (z_scores < 3)

    row_condition=condition.all(axis=1)
    data_filtered=df_encoded[row_condition]
    
    X=data_filtered[['area', 'bedrooms', 'bathrooms', 'stories', 'parking',
       'furnishingstatus', 'mainroad_no', 'mainroad_yes', 'guestroom_no',
       'guestroom_yes', 'basement_no', 'basement_yes', 'hotwaterheating_no',
       'hotwaterheating_yes', 'airconditioning_no', 'airconditioning_yes',
       'prefarea_no', 'prefarea_yes']]
    y= data_filtered['price']
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=7)

    lm = LinearRegression()
    model=lm.fit(X_train, y_train)
    dump(model, 'LinearModel.joblib')
if __name__ == "__main__":
    main()