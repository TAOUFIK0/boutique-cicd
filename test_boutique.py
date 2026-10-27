import pytest
from boutique import Boutique


def test_ajouter_produit():
    b = Boutique()
    b.ajouter_produit("stylo", 2.5, 10)
    assert b.produits["stylo"]["quantite"] == 10


def test_ajouter_meme_produit_cumule_le_stock():
    b = Boutique()
    b.ajouter_produit("stylo", 2.5, 10)
    b.ajouter_produit("stylo", 2.5, 5)
    assert b.produits["stylo"]["quantite"] == 15


def test_retirer_stock():
    b = Boutique()
    b.ajouter_produit("cahier", 4, 8)
    b.retirer_stock("cahier", 3)
    assert b.produits["cahier"]["quantite"] == 5


def test_retirer_stock_insuffisant():
    b = Boutique()
    b.ajouter_produit("cahier", 4, 2)
    with pytest.raises(ValueError):
        b.retirer_stock("cahier", 5)


def test_total_panier():
    b = Boutique()
    b.ajouter_produit("stylo", 2, 10)
    b.ajouter_produit("cahier", 5, 10)
    assert b.total_panier({"stylo": 3, "cahier": 2}) == 16


def test_produit_inconnu():
    b = Boutique()
    with pytest.raises(KeyError):
        b.total_panier({"gomme": 1})
