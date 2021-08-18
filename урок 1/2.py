time = int(input("Введите ваше время в секундах:"))
time_1 = time//3600
time_2 = (time - time_1*3600)//60
time_3 = time - (time_1*3600 + time_2*60)
print(f'Время в формате чч:мм:сс {time_1:02} : {time_2:02} : {time_3:03}')
