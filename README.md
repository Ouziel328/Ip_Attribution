# Ip_Attribution
# Gestion d'Adresse IP - Projet Python avec Interface Graphique

Ce projet est une application permettant de gérer l'attribution d'adresses IP. L'utilisateur saisit les quatre octets d'une adresse IP, et l'application valide chaque entrée tout en vérifiant que l'adresse IP est valide et non réservée.

## Fonctionnalités

- Validation des adresses IP (les nombres doivent être compris entre 0 et 255).
- Vérification que les adresses IP ne sont pas dans les plages réservées.
- Affichage du type de classe d'adresse IP (A, B, C, D, E).
- Interface graphique simple avec Tkinter.
- Prise en compte des événements de l'utilisateur (FocusOut sur les champs).

## Installation

1. **Clonez ce dépôt sur votre machine locale :**

    ```bash
    git clone https://github.com/ton-utilisateur/GestionAdresseIP.git
    ```

2. **Accédez au dossier du projet :**

    ```bash
    cd GestionAdresseIP
    ```

3. **Installez les dépendances nécessaires :**
    
    Ce projet utilise la bibliothèque `tkinter`, qui est généralement incluse avec Python. Si vous ne l'avez pas, vous pouvez l'installer via la commande suivante (pour Linux) :

    ```bash
    sudo apt-get install python3-tk
    ```

    Pour Windows et macOS, `tkinter` est normalement préinstallé.

## Utilisation

1. **Lancez le programme :**

    Une fois que vous avez installé les dépendances, lancez simplement le script `main.py` :

    ```bash
    python main.py
    ```

2. **Interface Utilisateur :**

    L'interface consiste en quatre champs de saisie pour entrer les octets de l'adresse IP. Lorsque l'utilisateur sort du champ (FocusOut), l'adresse est validée et le résultat est affiché.

3. **Exemple d'utilisation :**

    - Entrez une adresse IP telle que `192.168.1.1` et appuyez sur "Entrée".
    - Si l'adresse est valide, l'application vous indiquera la classe de l'adresse IP (par exemple, "Classe C").
    - Si l'adresse IP est invalide ou réservée, l'application affichera un message d'erreur et vous demandera de saisir à nouveau l'adresse.

## Conception

Ce projet a été conçu dans le but d'explorer l'utilisation de **Tkinter** pour la création d'une interface graphique simple, tout en intégrant des concepts de validation de données et de gestion d'erreurs.

- **Tkinter** est utilisé pour l'interface graphique.
- Le programme permet de valider les adresses IP en temps réel et de fournir un retour d'information à l'utilisateur.

### Détails de l'implémentation :

- La validation de l'adresse IP assure que chaque octet est compris entre 0 et 255, et que les plages réservées comme 0.x.x.x et 127.x.x.x ne sont pas utilisées.
- Lorsqu'une adresse IP complète est entrée, l'application affiche la classe de l'adresse (A, B, C, D ou E).

## Améliorations possibles

Voici quelques améliorations que vous pourriez envisager pour ce projet :

- Ajouter la possibilité d'exporter les adresses IP attribuées dans un fichier (par exemple, CSV ou JSON).
- Permettre la gestion de plusieurs plages d'adresses IP et l'attribution dynamique en fonction de la demande.
- Ajouter une fonctionnalité de génération automatique d'adresses IP dans des plages spécifiques.
- Support multilingue pour l'interface.

## Contributeurs

- **Ouziel Olou** - Développeur et créateur du projet.

## Licence

Ce projet est sous la licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Pour toute question ou suggestion, n'hésitez pas à me contacter via LinkedIn : [Mon profil LinkedIn](https://www.linkedin.com/in/ton-profile).
