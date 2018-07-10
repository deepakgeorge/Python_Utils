
fig, ax = plt.subplots()
#ax.set_title('RMS & Kurtosis visualization')
ax.scatter(lag_base_test_predict['b1_vib_kurt_hzrate'],lag_base_test_predict['life_per'], marker= 'o',alpha=0.5, lw=0.3,label='life_per')
ax.set_ylabel('life_per')
ax.scatter(lag_base_test_predict['b1_vib_kurt_hzrate'],lag_base_test_predict['y_pred'], marker= 'o',alpha=0.5, lw=0.3,label='y_pred')
ax.set_xlabel('b1_vib_kurt_hzrate')
ax.legend(bbox_to_anchor=(0.4,-0.10), loc=3,ncol=10,borderaxespad=0, edgecolor='k').draggable() #ncol makes legend horizontal. give high value like 10 when not sure of number of legends
fig.savefig('../docs/plots/b1_vib_kurt_hzrate_ypred_lm.png', bbox_inches='tight')
