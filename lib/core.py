import json
import os
import argparse
import shutil

def get_user_input(prompt):
    return input(prompt).strip()

def init_command(args):
    current_directory = os.getcwd()
    
    # # Vérifier si le répertoire courant est un dépôt Git
    # git_directory = os.path.join(current_directory, '.git')
    # if not os.path.isdir(git_directory):
    #     print("Il semble que vous ne soyez pas dans un répertoire Git.")
    #     return

    # # Vérifier si le répertoire .git n'est pas vide
    # if not os.listdir(git_directory):
    #     print("Le répertoire .git est vide. Assurez-vous d'être dans un dépôt Git valide.")
    #     return

    author_name = get_user_input("Auteur de la configuration : ")
    branch_type_autorized = get_user_input("Type de branches autorisés (Ex. Feat, Hotfix, Release, Docs, ... ) (Séparé par des espaces, si plusieurs): ")
    branch_join_authorized = get_user_input("Séparateurs de branches autorisé (Ex. /, \, |, ... ) : ")

    # Créer le dictionnaire de configuration
    config_data = {
        'author_name': author_name,
        'branch_type_autorized': branch_type_autorized.split(),
        'branch_join_authorized': branch_join_authorized,
    }

    # Copier le dossier hookity depuis resources vers le répertoire .git
    hookity_resources = os.path.join(os.path.dirname(__file__), '..', 'resources', 'hookity')
    shutil.copytree(hookity_resources, os.path.join(current_directory, 'hookity'), dirs_exist_ok=True)

    # Créer le fichier de configuration JSON
    config_path = os.path.join(current_directory, 'hookity', 'hookity_config.json')
    with open(config_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=2)

    print(f"Hookity initialisé avec succés !")

def main():
    parser = argparse.ArgumentParser(description='Hookity CLI v0.1')

    subparsers = parser.add_subparsers(help='Subcommands', dest='command')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialisation de kookity dans votre projet git.')
    init_parser.add_argument('directory', metavar='DIRECTORY', help='Répertoire du projet git où initialiser hookity.')

    args = parser.parse_args()

    if args.command == 'init':
        init_command(args)

if __name__ == "__main__":
    main()