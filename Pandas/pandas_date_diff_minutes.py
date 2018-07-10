#https://pandas.pydata.org/pandas-docs/stable/timedeltas.html#frequency-conversion
#Converting difference in dates to mins
basic_ft_base['age'] = (basic_ft_base['read_time'] - min(basic_ft_base['read_time']))/np.timedelta64(1, 'm')
