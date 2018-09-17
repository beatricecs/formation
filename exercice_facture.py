class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Ligne_facture:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.nom = produit.nom
        self.prix = produit.prix
        self.quantite = quantite
        self.montant = produit.prix * quantite

    def afficher_ligne_facture(self):
        print("Produit:%s Quantite %s Prix %s Montant %s" % (self.nom, self.quantite, self.prix, self.montant,))

class Facture:
    def __init__(self, ligne_facture):
        self.name = 'INV_2018/0001'
        self.client = 'toto'
        self.ligne_facture = ligne_facture

    def calcul_facture(self):
        total = 0.0
        tva = 1.20
        for line in facture_ligne:
            total += line.montant

        print("Total sans tva=%s"%total)
        total *= tva
        print("Total avec tva=%s"%total)



telephone1 = Produit('iphone6', 800.0)
coque = Produit('coque', 20.0)
facture_ligne = []

ligne_facture =  Ligne_facture(telephone1, 1)
facture_ligne.append(ligne_facture)
ligne_facture.afficher_ligne_facture()

ligne_facture =  Ligne_facture(coque, 2)
facture_ligne.append(ligne_facture)

ligne_facture.afficher_ligne_facture()

facture = Facture(ligne_facture)
facture.calcul_facture()

