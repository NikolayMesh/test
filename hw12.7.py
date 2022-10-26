money =int(input('Введите сумму '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

max_value = max(per_cent.values())

max_value_key = max(per_cent, key=per_cent.get)

print ('Самый выгодный банк по вкладу', max_value_key, '=', max_value, 'годовых')

deposit=int(max_value*money/100)

print('Максимальная сумма, которую вы можете заработать ', deposit)

deposit = [int(per_cent.get("ТКБ")*money/100),
           int(per_cent.get("СКБ")*money/100),
           int(per_cent.get("ВТБ")*money/100),
           int(per_cent.get("СБЕР")*money/100)]

deposit.sort(reverse = True)

print(deposit)
