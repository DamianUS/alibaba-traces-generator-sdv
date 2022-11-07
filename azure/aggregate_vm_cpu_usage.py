import pandas as pd

for hour in range(1,169):
    print("Procesando hora "+str(hour))
    #print("Leyendo csv:",'/home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-'+str(hour)+'_processed_cpu_mem.csv')
    hour_df = pd.read_csv('/home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-' + str(hour) + '_processed_cpu_mem.csv', header=None)
    #print("Leido csv")
    hour_df = hour_df.drop(hour_df.columns[[1, 2]], axis=1)  # drop vm_id and partial cpu usage (not multiplied by core count
    #print("Agregando")
    hour_df = hour_df.groupby(hour_df.columns[0]).sum()
    #print("Termina agregación")
    #print (hour_df.head())
    hour_df.to_csv('/home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-' + str(hour) + '_aggregated_cpu_mem.csv', header=False, index=True)