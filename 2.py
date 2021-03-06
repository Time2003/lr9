#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.
if __name__ == '__main__':
    def rev_key(dct):
        dct_new = dict()
        for i, v in dct.items():
            for w in v:
                dct_new[w] = dct_new.get(w, []) + [i]
        return dct_new


    dct = {1: 'acc', 2: 'cab', 3: 'ccb'}
    print(rev_key(dct))