def generer_cles_feistel(cle, permutation, ordre_decalage):
    # Appliquer la fonction de permutation
    cle_permutee = [cle[i] for i in permutation]
    
    # Diviser la clé en deux blocs de 4 bits
    k1 = cle_permutee[:4]
    k2 = cle_permutee[4:]
    
    # Appliquer les opérations XOR et AND
    k1_prime = [k1[i] ^ k2[i] for i in range(4)]
    k2_prime = [k2[i] & k1[i] for i in range(4)]
    
    # Appliquer les décalages
    k1_decale = k1_prime[ordre_decalage:] + k1_prime[:ordre_decalage]
    k2_decale = k2_prime[-ordre_decalage:] + k2_prime[:-ordre_decalage]
    
    return k1_decale, k2_decale

# Exemple d'utilisation
cle = [1, 0, 1, 0, 0, 1, 1, 0]  # Exemple de clé de longueur 8
permutation = [6, 5, 2, 7, 4, 1, 3, 0]  # Exemple de permutation
ordre_decalage = 2  # Exemple d'ordre de décalage

k1, k2 = generer_cles_feistel(cle, permutation, ordre_decalage)
print("Sous-clé k1:", k1)
print("Sous-clé k2:", k2)
