# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# Przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
#     1-n = [1,2,3,4,5,...,10]
#     np. n=10
#     wejście: [2,3,7,4,9], 10
#     wyjście: [1,5,6,8,10]
# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
import numpy


def postal_codes_generate(from_range: str, to_range: str):
    postal_codes = []
    first_range = int(from_range.replace('-', '')) + 1
    last_range = int(to_range.replace('-', '')) - 1
    while first_range <= last_range:
        first_range = str(first_range)
        temp_string = first_range[:2] + '-' + first_range[2:]
        postal_codes.append(temp_string)
        first_range = int(first_range)
        first_range += 1

    return postal_codes


def check_missing_numbers(data: list, data_len: int):
    return [number for number in range(1, data_len + 1) if number not in data]


def iterate_by_float_step(from_step, to_step, by_step):
    return [number for number in numpy.arange(from_step, to_step, by_step)]


if __name__ == '__main__':
    data = [2, 3, 7, 4, 9]
    data_len = 10
    str1 = '79-900'
    str2 = '80-155'
    from_step = 2
    to_step = 6
    by_step = .5
    print(postal_codes_generate(str1, str2))
    print(check_missing_numbers(data, data_len))
    print(iterate_by_float_step(from_step, to_step, by_step))
