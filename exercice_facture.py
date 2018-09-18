import random
from dataclasses import dataclass
import unittest
from typing import Optional

from faker.providers import BaseProvider


@dataclass
class Produit:
    nom : str
    prix : float = 0.0
    reference : Optional[str] = None

import factory

list_of_products = [
    'iPhone', 'Android', 'Acer', 'Apple'
]

class Provider(BaseProvider):
    def product_name(self):
        return random.choice(list_of_products)

factory.Faker.add_provider(Provider)

class ProductFactory(factory.Factory):
    class Meta:
        model=Produit
    reference = factory.Sequence(lambda identifier: f'PRO-{identifier}')
    nom = factory.Faker('product_name')
    prix = factory.Faker('random_int', min=0, max=9999)


def create_product(nom, prix):
    assert isinstance (nom, str) and len (nom.strip()) > 0
    assert isinstance (prix, float) and prix > 0.0
    print (f"Produit : {nom}")
    return Produit(nom,prix)


def create_fake_product():
    return ProductFactory()

@dataclass
class Lignes_facture:
    produit : str
    quantite : float = 0.0

    @property
    def montant(self):
        return self.produit.prix * self.quantite

    def afficher_lignes_facture(self):
        #print("Produit:%s Quantite %s Prix %s Montant %s" % (self.produit.nom, self.quantite, self.produit.prix, self.montant,))
        print (f"Produit : {self.produit.nom}, Quantité : {self.quantite}, Prix : {self.produit.prix}, Montant : {self.montant}")

class InvoiceLineFactory(factory.Factory):
    class Meta:
        model = Lignes_facture

    produit = factory.SubFactory(ProductFactory)
    quantite = factory.Faker('random_int', min=0, max=10)

def create_invoice_line(produit, quantite):
    return invoiceLine(produit, quantite)



class Facture:
    def __init__(self, facture_lignes, num_fact = 0, client = None):

        self.num_fact = 'INV_2018/000' + str(num_fact+1)
        self.client = client
        self.facture_lignes = facture_lignes


    def calcul_facture(self, tva = 1.20):
        total = 0.0
        #total = sum(line.montant for line in facture_lignes)

        for line in self.facture_lignes:
            total += line.montant

        print("Total sans tva=%s"%total)
        total *= tva

        print("Total avec tva=%s"%total)


class FactureFactory(factory.Factory):
    class Meta :
        model = Facture
    client = factory.Faker('name')
    facture_lignes =  factory.List(factory.SubFactory(InvoiceLineFactory) for i in range(5))


# def test_facture():
#     telephone1 = Produit('Iphone6', 800.0)
#     coque = Produit('Coque Protection', 20.0)
#     facture_lignes = []
#
#     lignes_facture =  Lignes_facture(telephone1, 1)
#     facture_lignes.append(lignes_facture)
#     lignes_facture.afficher_lignes_facture()
#
#     lignes_facture =  Lignes_facture(coque, 2)
#     facture_lignes.append(lignes_facture)
#
#     lignes_facture.afficher_lignes_facture()
#
#     facture = Facture(facture_lignes)
#     facture.calcul_facture()

class  ProduitTestCase(unittest.TestCase):
    def test_product_creation(self):
        produit = Produit('Iphone6', 800)

        self.assertEqual(produit.nom, 'Iphone6')
        self.assertEqual(produit.prix, 800.0)

    def test_ligne_facture(self):
        facture_lignes = []
        produit = Produit('Iphone6', 800)
        lignes_facture = Lignes_facture(produit, 1)
        self.assertEqual(lignes_facture.montant, 800)


        produit = Produit('Coque', 20)
        lignes_facture = Lignes_facture(produit, 2)

        self.assertEqual(lignes_facture.montant, 40)
        lignes_facture.afficher_lignes_facture()


class FactureTestCase(unittest.TestCase):

    def test_facture(self):
        facture_lignes = []
        produit = Produit('Iphone6', 800)

        lignes_facture = Lignes_facture(produit, 1)
        facture_lignes.append(lignes_facture)
        facture = Facture(facture_lignes)
        facture.calcul_facture()

        self.assertEqual(facture.num_fact, 'INV_2018/0001')

def main():
    invoice = FactureFactory()
    print (invoice)

def generate_invoice_html(invoice):
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
    env = Environment(
        loader = FileSystemLoader('templates'), undefined=StrictUndefined
    )
    template = env.get_template('invoice.html')
    return (template.render(invoice=invoice))

def generate_invoice_pdf(content, filename):
    from weasyprint import HTML
    from weasyprint.fonts import FontConfiguration
    font_config = FontConfiguration()
    html = HTML(string=content)
    html.write_pdf(filename, font_config=font_config)

if __name__ == '__main__':
    #fakeproduct = create_fake_product()
    #print(fakeproduct.nom)
    #produit = ProductFactory()
    #unittest.main()
    #'test_facture()
    import pathlib

    invoice = FactureFactory()
    content = generate_invoice_html(invoice)
    print(content)
    generate_invoice_pdf(content, '/tmp/invoice.pdf')
    pathlib.Path('/tmp/invoice.html').write_text(content)