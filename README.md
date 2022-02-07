This is the repository for Financial Data Analytics:

FIM TS - Is a time series ARIMA model which forecasts stock price

FIN! - Consists of data table manipulation, kurtosis, skew and distribution of stocks

FM-QUA - Consists of basic Quandl code and corresponding financial metrics

TS Simulation - 

Stock Picker - Runs a simulation in which it scans all stocks within the NASDAQ. 
3 main paramters:
return_period_weeks = which measures the length of time the returns are calculated for or the holdign period.
min_avg_return = which defines the minimum return that may be accepted.
max_dev_return = the maximum volatility within the return.


Lets assume:
Time period = 2021-01-01 - 2022-01-01
return_period_weeks = 4
min_avg_return = 0.1
max_dev_return = 0.07

The model works by buying a share of a stock each day and holding for 4 weeks. The share is then sold after 4 weeks. It does this for each day from 2021-2022. Shares that are not sold at the end of the time frame are simply held (ie buying 2021-12-31). The model does this for every stock within NASDAQ only returning those which fit our parameters of a minimum 10% avg return and 7% avg maximum std dev. 
