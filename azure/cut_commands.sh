awk -F, '$1>=0 && $1<3600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-1.csv
awk -F, '$1>=3600 && $1<7200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-2.csv
awk -F, '$1>=7200 && $1<10800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-3.csv
awk -F, '$1>=10800 && $1<14400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-4.csv
awk -F, '$1>=14400 && $1<18000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-5.csv
awk -F, '$1>=18000 && $1<21600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-6.csv
awk -F, '$1>=21600 && $1<25200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-7.csv
awk -F, '$1>=25200 && $1<28800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-8.csv
awk -F, '$1>=28800 && $1<32400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-9.csv
awk -F, '$1>=32400 && $1<36000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-10.csv
awk -F, '$1>=36000 && $1<39600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-11.csv
awk -F, '$1>=39600 && $1<43200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-12.csv
awk -F, '$1>=43200 && $1<46800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-13.csv
awk -F, '$1>=46800 && $1<50400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-14.csv
awk -F, '$1>=50400 && $1<54000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-15.csv
awk -F, '$1>=54000 && $1<57600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-16.csv
awk -F, '$1>=57600 && $1<61200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-17.csv
awk -F, '$1>=61200 && $1<64800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-18.csv
awk -F, '$1>=64800 && $1<68400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-19.csv
awk -F, '$1>=68400 && $1<72000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-20.csv
awk -F, '$1>=72000 && $1<75600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-21.csv
awk -F, '$1>=75600 && $1<79200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-22.csv
awk -F, '$1>=79200 && $1<82800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-23.csv
awk -F, '$1>=82800 && $1<86400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-24.csv
awk -F, '$1>=86400 && $1<90000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-25.csv
awk -F, '$1>=90000 && $1<93600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-26.csv
awk -F, '$1>=93600 && $1<97200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-27.csv
awk -F, '$1>=97200 && $1<100800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-28.csv
awk -F, '$1>=100800 && $1<104400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-29.csv
awk -F, '$1>=104400 && $1<108000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-30.csv
awk -F, '$1>=108000 && $1<111600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-31.csv
awk -F, '$1>=111600 && $1<115200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-32.csv
awk -F, '$1>=115200 && $1<118800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-33.csv
awk -F, '$1>=118800 && $1<122400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-34.csv
awk -F, '$1>=122400 && $1<126000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-35.csv
awk -F, '$1>=126000 && $1<129600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-36.csv
awk -F, '$1>=129600 && $1<133200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-37.csv
awk -F, '$1>=133200 && $1<136800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-38.csv
awk -F, '$1>=136800 && $1<140400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-39.csv
awk -F, '$1>=140400 && $1<144000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-40.csv
awk -F, '$1>=144000 && $1<147600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-41.csv
awk -F, '$1>=147600 && $1<151200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-42.csv
awk -F, '$1>=151200 && $1<154800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-43.csv
awk -F, '$1>=154800 && $1<158400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-44.csv
awk -F, '$1>=158400 && $1<162000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-45.csv
awk -F, '$1>=162000 && $1<165600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-46.csv
awk -F, '$1>=165600 && $1<169200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-47.csv
awk -F, '$1>=169200 && $1<172800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-48.csv
awk -F, '$1>=172800 && $1<176400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-49.csv
awk -F, '$1>=176400 && $1<180000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-50.csv
awk -F, '$1>=180000 && $1<183600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-51.csv
awk -F, '$1>=183600 && $1<187200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-52.csv
awk -F, '$1>=187200 && $1<190800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-53.csv
awk -F, '$1>=190800 && $1<194400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-54.csv
awk -F, '$1>=194400 && $1<198000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-55.csv
awk -F, '$1>=198000 && $1<201600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-56.csv
awk -F, '$1>=201600 && $1<205200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-57.csv
awk -F, '$1>=205200 && $1<208800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-58.csv
awk -F, '$1>=208800 && $1<212400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-59.csv
awk -F, '$1>=212400 && $1<216000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-60.csv
awk -F, '$1>=216000 && $1<219600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-61.csv
awk -F, '$1>=219600 && $1<223200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-62.csv
awk -F, '$1>=223200 && $1<226800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-63.csv
awk -F, '$1>=226800 && $1<230400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-64.csv
awk -F, '$1>=230400 && $1<234000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-65.csv
awk -F, '$1>=234000 && $1<237600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-66.csv
awk -F, '$1>=237600 && $1<241200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-67.csv
awk -F, '$1>=241200 && $1<244800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-68.csv
awk -F, '$1>=244800 && $1<248400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-69.csv
awk -F, '$1>=248400 && $1<252000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-70.csv
awk -F, '$1>=252000 && $1<255600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-71.csv
awk -F, '$1>=255600 && $1<259200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-72.csv
awk -F, '$1>=259200 && $1<262800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-73.csv
awk -F, '$1>=262800 && $1<266400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-74.csv
awk -F, '$1>=266400 && $1<270000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-75.csv
awk -F, '$1>=270000 && $1<273600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-76.csv
awk -F, '$1>=273600 && $1<277200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-77.csv
awk -F, '$1>=277200 && $1<280800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-78.csv
awk -F, '$1>=280800 && $1<284400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-79.csv
awk -F, '$1>=284400 && $1<288000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-80.csv
awk -F, '$1>=288000 && $1<291600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-81.csv
awk -F, '$1>=291600 && $1<295200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-82.csv
awk -F, '$1>=295200 && $1<298800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-83.csv
awk -F, '$1>=298800 && $1<302400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-84.csv
awk -F, '$1>=302400 && $1<306000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-85.csv
awk -F, '$1>=306000 && $1<309600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-86.csv
awk -F, '$1>=309600 && $1<313200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-87.csv
awk -F, '$1>=313200 && $1<316800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-88.csv
awk -F, '$1>=316800 && $1<320400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-89.csv
awk -F, '$1>=320400 && $1<324000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-90.csv
awk -F, '$1>=324000 && $1<327600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-91.csv
awk -F, '$1>=327600 && $1<331200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-92.csv
awk -F, '$1>=331200 && $1<334800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-93.csv
awk -F, '$1>=334800 && $1<338400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-94.csv
awk -F, '$1>=338400 && $1<342000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-95.csv
awk -F, '$1>=342000 && $1<345600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-96.csv
awk -F, '$1>=345600 && $1<349200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-97.csv
awk -F, '$1>=349200 && $1<352800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-98.csv
awk -F, '$1>=352800 && $1<356400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-99.csv
awk -F, '$1>=356400 && $1<360000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-100.csv
awk -F, '$1>=360000 && $1<363600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-101.csv
awk -F, '$1>=363600 && $1<367200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-102.csv
awk -F, '$1>=367200 && $1<370800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-103.csv
awk -F, '$1>=370800 && $1<374400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-104.csv
awk -F, '$1>=374400 && $1<378000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-105.csv
awk -F, '$1>=378000 && $1<381600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-106.csv
awk -F, '$1>=381600 && $1<385200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-107.csv
awk -F, '$1>=385200 && $1<388800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-108.csv
awk -F, '$1>=388800 && $1<392400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-109.csv
awk -F, '$1>=392400 && $1<396000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-110.csv
awk -F, '$1>=396000 && $1<399600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-111.csv
awk -F, '$1>=399600 && $1<403200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-112.csv
awk -F, '$1>=403200 && $1<406800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-113.csv
awk -F, '$1>=406800 && $1<410400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-114.csv
awk -F, '$1>=410400 && $1<414000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-115.csv
awk -F, '$1>=414000 && $1<417600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-116.csv
awk -F, '$1>=417600 && $1<421200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-117.csv
awk -F, '$1>=421200 && $1<424800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-118.csv
awk -F, '$1>=424800 && $1<428400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-119.csv
awk -F, '$1>=428400 && $1<432000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-120.csv
awk -F, '$1>=432000 && $1<435600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-121.csv
awk -F, '$1>=435600 && $1<439200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-122.csv
awk -F, '$1>=439200 && $1<442800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-123.csv
awk -F, '$1>=442800 && $1<446400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-124.csv
awk -F, '$1>=446400 && $1<450000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-125.csv
awk -F, '$1>=450000 && $1<453600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-126.csv
awk -F, '$1>=453600 && $1<457200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-127.csv
awk -F, '$1>=457200 && $1<460800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-128.csv
awk -F, '$1>=460800 && $1<464400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-129.csv
awk -F, '$1>=464400 && $1<468000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-130.csv
awk -F, '$1>=468000 && $1<471600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-131.csv
awk -F, '$1>=471600 && $1<475200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-132.csv
awk -F, '$1>=475200 && $1<478800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-133.csv
awk -F, '$1>=478800 && $1<482400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-134.csv
awk -F, '$1>=482400 && $1<486000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-135.csv
awk -F, '$1>=486000 && $1<489600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-136.csv
awk -F, '$1>=489600 && $1<493200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-137.csv
awk -F, '$1>=493200 && $1<496800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-138.csv
awk -F, '$1>=496800 && $1<500400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-139.csv
awk -F, '$1>=500400 && $1<504000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-140.csv
awk -F, '$1>=504000 && $1<507600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-141.csv
awk -F, '$1>=507600 && $1<511200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-142.csv
awk -F, '$1>=511200 && $1<514800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-143.csv
awk -F, '$1>=514800 && $1<518400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-144.csv
awk -F, '$1>=518400 && $1<522000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-145.csv
awk -F, '$1>=522000 && $1<525600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-146.csv
awk -F, '$1>=525600 && $1<529200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-147.csv
awk -F, '$1>=529200 && $1<532800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-148.csv
awk -F, '$1>=532800 && $1<536400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-149.csv
awk -F, '$1>=536400 && $1<540000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-150.csv
awk -F, '$1>=540000 && $1<543600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-151.csv
awk -F, '$1>=543600 && $1<547200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-152.csv
awk -F, '$1>=547200 && $1<550800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-153.csv
awk -F, '$1>=550800 && $1<554400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-154.csv
awk -F, '$1>=554400 && $1<558000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-155.csv
awk -F, '$1>=558000 && $1<561600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-156.csv
awk -F, '$1>=561600 && $1<565200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-157.csv
awk -F, '$1>=565200 && $1<568800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-158.csv
awk -F, '$1>=568800 && $1<572400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-159.csv
awk -F, '$1>=572400 && $1<576000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-160.csv
awk -F, '$1>=576000 && $1<579600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-161.csv
awk -F, '$1>=579600 && $1<583200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-162.csv
awk -F, '$1>=583200 && $1<586800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-163.csv
awk -F, '$1>=586800 && $1<590400' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-164.csv
awk -F, '$1>=590400 && $1<594000' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-165.csv
awk -F, '$1>=594000 && $1<597600' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-166.csv
awk -F, '$1>=597600 && $1<601200' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-167.csv
awk -F, '$1>=601200 && $1<604800' /home/afdez/trazas_azure/csvs/vm_cpu_readings-files-1-46_cut.csv > /home/afdez/trazas_azure/csvs/vm_cpu_readings_hour-168.csv