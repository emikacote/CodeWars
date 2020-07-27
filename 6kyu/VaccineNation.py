vaccine_dict = {
                'fiveInOne' : ['8 weeks', '12 weeks', '16 weeks'], # Protects against: diphtheria, tetanus, whooping cough, polio and Hib (Haemophilus influenzae type b)
                'pneumococcal' : ['8 weeks', '16 weeks'], # Protects against: some types of pneumococcal infection
                'rotavirus' : ['8 weeks', '12 weeks'], # Protects against: rotavirus infection, a common cause of childhood diarrhoea and sickness
                'meningitisB' : ['8 weeks', '16 weeks', '12 months'], # Protects against: meningitis caused by meningococcal type B bacteria
                'hibMenC' : ['12 months'], # Protects against: Haemophilus influenzae type b (Hib), meningitis caused by meningococcal group C bacteria
                'measlesMumpsRubella' : ['12 months', '40 months'], # Protects against: measles, mumps and rubella
                'fluVaccine' : ['september','october','november'], # Given at: annually in Sept/Oct
                'preSchoolBooster' : ['40 months'] # Protects against: diphtheria, tetanus, whooping cough and polio
                }
class Kid:
    def __init__(self, age, status, month):
        self.age = age
        self.status = status
        self.month = month

    def find_vaccines(self):
        vaccines_needed = []
        if self.month in vaccine_dict['fluVaccine']:
            vaccines_needed.append('offer fluVaccine')
        for key in vaccine_dict:
            if self.status != 'up-to-date':
                if self.status in vaccine_dict[key]:
                    vaccines_needed.append(key)
            if self.age in vaccine_dict[key] and key not in vaccines_needed:
                vaccines_needed.append(key)
        return sorted(vaccines_needed)

vaccine_list = lambda age, status, month: Kid(age, status, month).find_vaccines()
