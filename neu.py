import numpy as np
from neuralprophet import NeuralProphet
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# df = pd.read_csv("yosemite_temps.csv")
# df['ds'] = pd.to_datetime(df['ds'])
# plt.figure(figsize=(20,16))
# sns.lineplot(data = df.set_index('ds'))
# plt.savefig('raw_y.png',format= 'png')
# plt.show()


# m_baseline = NeuralProphet()
# df_train, df_test = m_baseline.split_df(df, freq='5min', valid_p=0.20)
# plt.figure(figsize=(20,16))
# metrics = m_baseline.fit(df_train, freq='5min',validation_df=df_test)


# m_add_lag = NeuralProphet(n_lags=12*24)
# df_train, df_test = m_add_lag.split_df(df, freq='5min', valid_p=0.20)
# m_add_lag.fit(df_train, freq='5min',validation_df=df_test)
# m_add_lag.plot_parameters()
# plt.savefig('ar_pramas.png',format= 'png')
# plt.show()


df_ercot = pd.read_csv("load_ercot_regions.csv")
df_list = list()
df_dict = {}
regions = ['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
for cols in regions:
    aux = df_ercot[['ds', cols]].copy()  # select column associated with region
    aux = aux.iloc[:26301, :].copy()  # selects data up to 26301 row (2004 to 2007 time stamps)
    aux = aux.rename(columns={cols: 'y'})  # rename column of data to 'y' which is compatible with Neural Prophet
    df_list.append(aux)
    df_dict[cols] = aux

m_case1 = NeuralProphet(n_lags=24, normalize='minmax')
df_train_dict, df_test_dict = m_case1.split_df(df_dict, valid_p=0.33, local_split=True)
two_df = dict((k, df_train_dict[k]) for k in ['COAST', 'EAST'])
metrics_case1 = m_case1.fit(two_df, freq='H')

two_df_test = dict((k, df_test_dict[k]) for k in ['COAST', 'EAST'])
future = m_case1.make_future_dataframe(two_df_test, n_historic_predictions=True)
forecast_two_df_case1 = m_case1.predict(future)
print(forecast_two_df_case1.head())

# def plot_forecast_dict(forecast_dict):
#     fig = go.Figure()
#     for col in forecast_dict:
#         fig.add_trace(go.Scatter(mode='markers',x = forecast_dict[col]['ds'],y=forecast_dict[col]['y'],name=f'{col}_y',opacity=0.5,marker=dict(size=2)))
#         fig.add_trace(go.Scatter(mode='lines',x = forecast_dict[col]['ds'],y=forecast_dict[col]['yhat1'],name=f'{col}_y_hat'))
#     return fig

# fig = plot_forecast_dict(forecast_two_df_case1)
# fig.show()
