#https://pandas.pydata.org/pandas-docs/stable/timedeltas.html#frequency-conversion
#Converting difference in dates to mins
df['age'] = (df['read_time'] - min(df['read_time']))/np.timedelta64(1, 'm')
