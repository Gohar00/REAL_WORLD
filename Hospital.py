from Building import Building


class Hospital(Building):
    def __init__(self, hospital_name):
        Building.__init__(self, hospital_name)
        self.patients = []

    def admit_patient(self, patient):
        if patient:
            self.patients.append(patient)

    def discharge_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)

    def show_info(self):
        patient_list = "\n".join(self.patients)
        return f"Hospital Name: {self.name}\nNumber of Patients: {len(self.patients)}\nList of Patients:\n{patient_list}"

