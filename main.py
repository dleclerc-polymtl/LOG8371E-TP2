#! python
# -*- coding: utf-8 -*-

import random
from faker import Faker



fake = Faker()



class Patient():

    def __init__(self, id):
        self.id = id
        self.gender = random.choice(['M', 'F'])
        self.date_of_birth = fake.date_of_birth()

        [ first_name, last_name ] = (
            [ fake.first_name_male, fake.last_name_male ]
            if self.gender == 'M' else
            [ fake.first_name_female, fake.last_name_female ]
        )

        self.first_name = first_name()
        self.last_name = last_name()

        self.street_address = fake.street_address()
        self.city = fake.city()
        self.country = fake.country()
        self.postcode = fake.postcode()



    def __str__(self):
        person = '{0} {1} [{2}, {3}]'.format(self.first_name, self.last_name, self.gender, self.date_of_birth)
        address = '{0}, {1}, {2}, {3}'.format(self.street_address, self.city, self.country, self.postcode)
                
        return '{0}: {1}, {2}'.format(self.id, person, address)



    def get_csv(self):
        return ';'.join([
            self.id,
            self.first_name, self.last_name, self.gender, str(self.date_of_birth),
            self.street_address, self.city, self.country, self.postcode
        ])



def generate_patient_details():
    patients = []

    with open('./data/patient_ids.csv', mode = 'r', encoding = 'utf-8') as f:
        ids = f.read().splitlines()
    
    for id in ids:
        patient = Patient(id)
        print(patient)
        patients += [ patient.get_csv() + '\n' ]

    with open('./data/patient_details.csv', mode = 'w', encoding = 'utf-8') as f:
        f.writelines(patients)



def generate_patient_names(n):
    names = [ fake.first_name() + '\n' for i in range(n) ]

    with open('./data/patient_names.csv', mode = 'w', encoding = 'utf-8') as f:
        f.writelines(names)



def main():
    generate_patient_names(1000)



if __name__ == '__main__':
    main()