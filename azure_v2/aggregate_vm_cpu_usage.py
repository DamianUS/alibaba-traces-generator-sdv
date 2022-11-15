import pandas as pd

for halfday in range(57, 61):
    print("Procesando medío día "+str(halfday))
    #print("Leyendo csv:",'/home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-'+str(hour)+'_processed_cpu_mem.csv')
    '/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week4/vm_cpu_readings_halfday-28.csv'
    hour_df = pd.read_csv('/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-' + str(halfday) + '_processed_cpu_mem.csv', header=None)
    print("Leido csv")
    hour_df = hour_df.drop(hour_df.columns[[1, 2]], axis=1)  # drop vm_id and partial cpu usage (not multiplied by core count
    print("Agregando")
    hour_df = hour_df.groupby(hour_df.columns[0]).sum()
    print("Termina agregación")
    #print (hour_df.head())
    hour_df.to_csv('/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-' + str(halfday) + '_aggregated_cpu_mem.csv', header=False, index=True)