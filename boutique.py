class Boutique:
    """Mini-boutique : gestion d'un stock et d'un panier."""

    def __init__(self):
        self.produits = {}

    def ajouter_produit(self, nom, prix, quantite):
        if prix < 0 or quantite < 0:
            raise ValueError("Prix et quantité doivent être positifs")
        if nom in self.produits:
            self.produits[nom]["quantite"] += quantite
        else:
            self.produits[nom] = {"prix": prix, "quantite": quantite}

    def retirer_stock(self, nom, quantite):
        if nom not in self.produits:
            raise KeyError("Produit inconnu : " + nom)
        if quantite > self.produits[nom]["quantite"]:
            raise ValueError("Stock insuffisant")
        self.produits[nom]["quantite"] -= quantite

    def total_panier(self, panier):
        total = 0
        for nom, quantite in panier.items():
            if nom not in self.produits:
                raise KeyError("Produit inconnu : " + nom)
            total += self.produits[nom]["prix"] * quantite
        return total
