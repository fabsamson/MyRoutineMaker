import random
class Agenda:
    def __init__(self, Jours, Activites, NombreActivites):
        self.Jours = Jours
        self.Activites = Activites
        self.NombreActivites = NombreActivites

    def activites_obligatoire(self):
        self.obligatoire = []
        self.facultatif = []
        for activite in self.Activites:
            if(activite.Obligatoire):
                self.obligatoire.append(activite)
            else:
                self.facultatif.append(activite)
    

    def select_jour(self):
        jours_pris = self.agenda.keys()
        jours_pris = [jour[0] for jour in jours_pris]
        test = len(jours_pris) < len(self.Jours)
        if(test):
            jours_dispo = [jour for jour in self.Jours if jour not in jours_pris]
            return random.choice(jours_dispo)
        else:
            return random.choice(self.Jours)

    def run_schedule(self):
        self.agenda = {}
        i = 0
        nb_iter = 0
        self.activites_obligatoire() 
        while i < self.NombreActivites and nb_iter < 100:
            nb_iter += 1
            jour = self.select_jour()
            activite_obligatoire = len(self.obligatoire) > 0
            if(activite_obligatoire):
                random_index = random.randrange(len(self.obligatoire))
                activite = self.obligatoire.pop(random_index)
            else:
                random_index = random.randrange(len(self.facultatif))
                activite = self.facultatif.pop(random_index)
            moment = random.choice(activite.Moments)
            if((jour,moment) in self.agenda.keys()):
                if(activite_obligatoire):
                    self.obligatoire.append(activite)
                else:
                    self.facultatif.append(activite)
                continue
            if(moment in jour.Moments):
                self.agenda.update({(jour,moment):activite})
                i += 1
        self.print_agenda()

    def print_agenda(self):
        agenda = self.agenda
        for k,v in agenda.items():
            print("%s -> %s : %s" % (k[0].Nom, k[1].name, v.Nom))