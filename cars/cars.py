#!/usr/bin/python3

import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def __str__(self):
        return self.brand

    def __repr__(self):
        return f"{self.car_type} {self.brand}"

    def get_photo_file_ext(self):
        photo_file = os.path.splitext(self.photo_file_name)
        return photo_file[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl
        whl = body_whl.split('x') if body_whl else [0, 0, 0]
        self.body_width = float(whl[0])
        self.body_height = float(whl[1])
        self.body_length = float(whl[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

def create_new_car(row):
    if row[1] == '':
        return None
    brand = row[1]
    if row[2] == '' or not row[2].isdecimal():
        return None
    passenger_seats_count = int(row[2])
    if row[3] == '':
        return None
    photo_file_name = row[3]
    if row[4] != '':
        return None
    if row[5] == '':
        return None
    try:
        carrying = float(row[5])
    except:
        return None
    if row[6] != '':
        return None
    return Car(brand, photo_file_name, carrying, passenger_seats_count)

def create_new_truck(row):
    if row[1] == '':
        return None
    brand = row[1]
    if row[2] != '':
        return None
    if row[3] == '':
        return None
    photo_file_name = row[3]
    if row[4]:
        whl = row[4].split('x')
        if len(whl) != 3:
            return None
        try:
            w = float(whl[0])
            h = float(whl[1])
            l = float(whl[2])
        except:
            return None
    body_whl = row[4]
    if row[5] == '':
        return None
    try:
        carrying = float(row[5])
    except:
        return None
    if row[6] != '':
        return None
    return Truck(brand, photo_file_name, carrying, body_whl)

def create_spec_machine(row):
    if row[1] == '':
        return None
    brand = row[1]
    if row[2] != '':
        return None
    if row[3] == '':
        return None
    photo_file_name = row[3]
    if row[4] != '':
        return None
    if row[5] == '':
        return None
    try:
        carrying = float(row[5])
    except:
        return None
    if row[6] == '':
        return None
    extra = row[6]
    return SpecMachine(brand, photo_file_name, carrying, extra)

def get_car_list(csv_filename):

    car_types = ('car', 'truck', 'spec_machine')
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7 and row[0] in car_types:
                if row[0] == car_types[0]:
                    obj = create_new_car(row)
                    if not obj is None:
                        car_list.append(obj)
                elif row[0] == car_types[1]:
                    obj = create_new_truck(row)
                    if not obj is None:
                        car_list.append(obj)
                elif row[0] == car_types[2]:
                    obj = create_spec_machine(row)
                    if not obj is None:
                        car_list.append(obj)
    return car_list

def _main():
    car_list = get_car_list('cars.csv')
    print(car_list)

if __name__ == '__main__':
    _main()
