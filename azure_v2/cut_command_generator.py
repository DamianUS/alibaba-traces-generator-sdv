# def generate_cut_command (day):
#     start_timestamp = 86400*day
#     end_timestamp = 86400*(day+1)
#     return f'awk -F, \'$1>={start_timestamp} && $1<{end_timestamp}\' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_day-{day+1}.csv'
#
# commands = [generate_cut_command(day) for day in range(7)]
# print (commands)

#
# def generate_cut_command (hour):
#     start_timestamp = 60*60*hour
#     end_timestamp = 60*60*(hour+1)
#     return f'awk -F, \'$1>={start_timestamp} && $1<{end_timestamp}\' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-{hour+1}.csv'


# def generate_cut_command (week):
#     start_timestamp = 60*60*24*7*week
#     end_timestamp = 60*60*24*7*(week+1)
#     return f'awk -F, \'$1>={start_timestamp} && $1<{end_timestamp}\' /home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/vm_cpu_readings-files-46-195_sorted_cut.csv > /home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/vm_cpu_readings_week-{week+1}.csv'
def generate_cut_command (halfday):
    start_timestamp = 60*60*12*halfday
    end_timestamp = 60*60*12*(halfday+1)
    return f'awk -F, \'$1>={start_timestamp} && $1<{end_timestamp}\' /home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_week-5.csv > /home/afdez/trazas_azure/segunda_tanda/uncompressed_47-195/week5/vm_cpu_readings_halfday-{halfday+1}.csv'


commands = [generate_cut_command(week) for week in range(57,67)]
print (commands)