import pandas as pd

from itertools import islice
import csv

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

#vmtable_df = pd.read_csv('/home/afdez/trazas_azure/vmtable.csv', header=None)
#print("Número de distincts vmids",len(vmtable_df.groupby(vmtable_df.columns[0])))

reader = csv.reader(open('/home/afdez/trazas_azure/vmtable.csv'))

vm_ids_dict = {}
for row in reader:
    vm_id = row[0]
    if vm_id in vm_ids_dict:
        print('Clave', vm_id, 'duplicada')
        pass
    try:
        core_count = float(row[9])
    except:
        core_count = float(row[9][1:])
    try:
        mem = float(row[10])
    except:
        mem = float(row[10][1:])

    vm_ids_dict[vm_id] = [core_count, mem]

print('Diccionario de vms cargado con un total de ' + str(len(vm_ids_dict)) + ' máquinas virtuales')
#print('Diccionario: ', take(10, vm_ids_dict.items()))



for halfday in range(57, 61):
    print("Procesando hora " + str(halfday))
    print("Leyendo csv:",'/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-' + str(halfday) + '.csv')
    day_df = pd.read_csv('/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-' + str(halfday) + '.csv', header=None)
    print("Leido csv")

    # print(day_df.head())
    # for index, row in day_df.iterrows():
    #     print("for")
    #     print(row[2], vm_ids_dict[row[1]][0])
    #print("Número de distincts vmids",len(day_df.groupby(day_df.columns[1]).mean()))

    # print("Borrando claves no existentes")
    # print("N filas antes de drop", day_df.shape[0])
    # print("indices: ",day_df[~day_df[1].isin(list(vm_ids_dict.keys()))].index)
    # day_df.drop(day_df[~day_df[1].isin(list(vm_ids_dict.keys()))].index, inplace=True)
    # print("N filas después de drop", day_df.shape[0])
    # print("Eliminadas claves no existentes")


    print("Empieza computación avg_cpu")
    day_df['average_cpu'] = day_df.apply(lambda row: row[2] * (vm_ids_dict[row[1]][0]), axis=1)
    print("Termina computación avg_cpu")
    print("Empieza computación mem")
    day_df['mem'] = day_df.apply(lambda row: vm_ids_dict[row[1]][1], axis=1)
    print("Termina computando mem")
    #print (day_df.head())
    day_df.to_csv('/home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-' + str(halfday) + '_processed_cpu_mem.csv', header=False, index=False)