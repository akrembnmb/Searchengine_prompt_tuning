import matplotlib.pyplot as plt

# Données
etapes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
perte_entrainement = [4.034800, 2.778900, 1.478700, 0.536900, 0.071200, 0.005400, 0.002000, 0.000800, 0.000500, 0.000300, 0.000200, 0.000200, 0.000100, 0.000100, 0.000100, 0.000100, 0.000100, 0.000100, 0.000100, 0.000100]
perte_validation = [3.209239, 2.034879, 0.811721, 0.182733, 0.008686, 0.002787, 0.000904, 0.000681, 0.000339, 0.000226, 0.000192, 0.000146, 0.000110, 0.000130, 0.000099, 0.000110, 0.000098, 0.000096, 0.000099, 0.000096]
exactitude_entrainement = [0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.92, 0.93, 0.94, 0.95, 0.96, 0.96, 0.97, 0.97, 0.97, 0.98, 0.98, 0.98, 0.98, 0.98]
exactitude_validation = [0.58, 0.68, 0.73, 0.78, 0.83, 0.88, 0.91, 0.92, 0.93, 0.94, 0.95, 0.95, 0.96, 0.96, 0.96, 0.97, 0.97, 0.97, 0.97, 0.97]

# Tracé des Pertes
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(etapes, perte_entrainement, label='Perte d\'Entraînement')
plt.plot(etapes, perte_validation, label='Perte de Validation')
plt.xlabel('Étapes')
plt.ylabel('Perte')
plt.title('Perte d\'Entraînement et de Validation')
plt.legend()

# Tracé des Exactitudes
plt.subplot(1, 2, 2)
plt.plot(etapes, exactitude_entrainement, label='Exactitude d\'Entraînement')
plt.plot(etapes, exactitude_validation, label='Exactitude de Validation')
plt.xlabel('Étapes')
plt.ylabel('Exactitude')
plt.title('Exactitude d\'Entraînement et de Validation')
plt.legend()

# Afficher les tracés
plt.tight_layout()
plt.show()
