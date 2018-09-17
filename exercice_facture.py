from dataclasses import dataclass

@dataclass
class Produit:
    nom : str
    prix : float = 0.0

@dataclass
class Lignes_facture:
    produit : str
    quantite : float = 0.0

    @property
    def montant(self):
        return self.produit.prix * self.quantite
        #self.montant = produit.prix * quantite

    def afficher_lignes_facture(self):
        #print("Produit:%s Quantite %s Prix %s Montant %s" % (self.produit.nom, self.quantite, self.produit.prix, self.montant,))
        print (f"Produit : {self.produit.nom}, Quantité : {self.quantite}, Prix : {self.produit.prix}, Montant : {self.montant}")


class Facture:
    def __init__(self, facture_lignes, num_fact = 0, client = None):
        assert isinstance(num_fact, int), " Numero non-entier, instance de " + str(type(num_fact))

        self.num_fact = num_fact + 1
        self.num_fact = 'INV_2018/000' + str(self.num_fact)
        self.client = client
        self.facture_lignes = facture_lignes

    def calcul_facture(self, tva = 1.20):
        total = 0.0
        for line in self.facture_lignes:
            total += line.montant

        print("Total sans tva=%s"%total)
        total *= tva
        print("Total avec tva=%s"%total)


def test_facture():
    telephone1 = Produit('Iphone6', 800.0)
    coque = Produit('Coque Protection', 20.0)
    facture_lignes = []

    lignes_facture =  Lignes_facture(telephone1, 1)
    facture_lignes.append(lignes_facture)
    lignes_facture.afficher_lignes_facture()

    lignes_facture =  Lignes_facture(coque, 2)
    facture_lignes.append(lignes_facture)

    lignes_facture.afficher_lignes_facture()

    facture = Facture(facture_lignes)
    facture.calcul_facture()

test_facture()

