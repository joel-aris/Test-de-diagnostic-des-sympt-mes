class Regle:
    def __init__(self, conditions, diagnostic, urgence=0, specificite=0):
        self.conditions = conditions  # Liste de conditions (symptômes)
        self.diagnostic = diagnostic  # Diagnostic associé
        self.urgence = urgence  # Urgence de la règle (0-5)
        self.specificite = specificite  # Spécificité de la règle (0-5)
        self.score = urgence + specificite  # Calcul du score total pour prioriser

    def conditions_satisfaites(self, faits):
        """Vérifie si les conditions de la règle sont satisfaites avec les faits donnés."""
        return all(faits.get(condition, False) for condition in self.conditions)

def demander_symptomes():
    """Demande à l'utilisateur de saisir ses symptômes."""
    print("Veuillez répondre aux questions suivantes avec 1 (oui) ou 0 (non) :")
    faits = {}
    faits["F1"] = bool(int(input("Avez-vous de la fièvre ? (1/0) : ")))
    faits["F2"] = bool(int(input("Avez-vous une toux ? (1/0) : ")))
    faits["F3"] = bool(int(input("Ressentez-vous une fatigue extrême ? (1/0) : ")))
    faits["F4"] = bool(int(input("Avez-vous des douleurs musculaires ? (1/0) : ")))
    faits["F5"] = bool(int(input("Vos résultats de laboratoire sont-ils positifs ? (1/0) : ")))
    faits["F6"] = bool(int(input("Avez-vous voyagé récemment dans une zone tropicale ? (1/0) : ")))
    faits["F7"] = bool(int(input("Avez-vous des maux de tête persistants ? (1/0) : ")))
    return faits

def calculer_niveau_symptomes(faits):
    """Calcule un niveau de gravité basé sur le nombre de symptômes présents."""
    nb_symptomes = sum(faits.values())
    if nb_symptomes == 0:
        return "Aucun symptôme détecté. Vous semblez en bonne santé."
    elif 1 <= nb_symptomes <= 2:
        return "Symptômes légers. Pas de gravité apparente."
    elif 3 <= nb_symptomes <= 4:
        return "Symptômes modérés. Une consultation médicale est recommandée."
    else:
        return "Symptômes graves. Consultez un médecin immédiatement."

def diagnostiquer(faits, regles):
    # Étape 1 : Identifier les règles applicables
    regles_applicables = [regle for regle in regles if regle.conditions_satisfaites(faits)]

    if not regles_applicables:
        niveau_symptomes = calculer_niveau_symptomes(faits)
        print(f"Aucune règle applicable. {niveau_symptomes}")
        return None

    # Étape 2 : Prioriser les règles applicables en fonction du score
    regle_prioritaire = max(regles_applicables, key=lambda regle: regle.score)
    
    # Étape 3 : Retourner le diagnostic de la règle prioritaire
    print(f"Diagnostic : {regle_prioritaire.diagnostic}")
    return regle_prioritaire.diagnostic

# Définition des règles
regles = [
    Regle(["F1", "F2"], "Grippe", urgence=3, specificite=2),
    Regle(["F1", "F3", "F4"], "Dengue", urgence=4, specificite=3),
    Regle(["F2", "F5"], "Infection virale grave", urgence=5, specificite=4),
    Regle(["F1", "F2", "F3", "F4"], "Absence de maladie", urgence=0, specificite=5),
    Regle(["F1", "F6"], "Maladie tropicale", urgence=3, specificite=4),
    Regle(["F3", "F7"], "Stress sévère", urgence=2, specificite=3),
    Regle(["F1", "F4", "F5"], "Infection virale spécifique", urgence=4, specificite=4),
]

# Exécution du programme
print("=== Bienvenue dans le système de diagnostic médical ===")
faits_utilisateur = demander_symptomes()
diagnostic = diagnostiquer(faits_utilisateur, regles)
