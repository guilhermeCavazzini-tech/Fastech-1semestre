#
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')


def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválido, deve ser DD/MM/AAAA")
        return None
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')

        dia = datetime.strftime(data_datetime, '%d')
        mes = datetime.strftime(data_datetime, '%B')
        ano = datetime.strftime(data_datetime, '%Y')
        return dia + " de " + mes[0].upper() + mes[1:] + " de " + ano


data = input("Digite uma data no formato DD/MM/AAAA:")
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)
