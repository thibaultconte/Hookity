import json
import os
import argparse
import shutil
import subprocess

def get_user_input(prompt):
    return input(prompt).strip()

def init_command():
    current_directory = os.getcwd()
    
    git_directory = os.path.join(current_directory, '.git')
    if not os.path.isdir(git_directory):
        print("Il semble que vous ne soyez pas dans un répertoire Git.")
        return

    if not os.listdir(git_directory):
        print("Le répertoire .git est vide. Assurez-vous d'être dans un dépôt Git valide.")
        return
    
    existing_hookity_config = os.path.join(current_directory, 'hookity')
    if os.path.isdir(existing_hookity_config):
        print("Il semblerai qu'une configuration hookity soit déjà mise en place ...")
        print("Lancer la commande 'hookity install', pour installer les configurations Hookity")
        return
    
    print("Nous devons savoir qui vous êtes !")
    organization_name = get_user_input("Nom de votre projet ou de votre société : ")
    
    print("Configuration des normes conventionnelles pour vos branches Git")
    branch_type_autorized = get_user_input("Type de branches autorisés (Ex. Feat, Hotfix, Release, Docs, ... ) (Séparé par des espaces, si plusieurs): ")
    
    print("Configuration des normes conventionnelles pour vos messages de commit Git")
    commit_type_autorized = get_user_input("Type de commit autorisés (Ex. build|docs|bug|feat|fix|experiment|refactor|test... ) (Séparé par des espaces, si plusieurs): ")
    commit_scope_authorized = get_user_input("Scope de commit autorisés (Ex. controllers|route|middleware|view|config|service|api... ) (Séparé par des espaces, si plusieurs) (Mettre * pour laisser libre): ")
    

    config_data = {
        'organization_name': organization_name,
        'branch_type_autorized': branch_type_autorized.split(),
        'commit_type_autorized': commit_type_autorized.split(),
        'commit_scope_authorized': commit_scope_authorized.split(),
    }

    hookity_resources = os.path.join(os.path.dirname(__file__), '..', 'resources', 'hookity')
    shutil.copytree(hookity_resources, os.path.join(current_directory, 'hookity'), dirs_exist_ok=True)

    config_path = os.path.join(current_directory, 'hookity', 'hookity_config.json')
    with open(config_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=2)

    print(f"Hookity initialisé avec succés !")


def install_command():
    hookity_directory = os.path.join(os.getcwd(), 'hookity')
    setup_hooks_script = os.path.join(hookity_directory, 'setup_hooks.sh')

    if os.path.exists(setup_hooks_script):
        subprocess.run(['bash', setup_hooks_script])
    else:
        print("Erreur : Le script setup_hooks.sh n'a pas été trouvé dans le dossier hookity.")

# Faire deactivate command

# Faire uninstall command

def main():
    parser = argparse.ArgumentParser(description='Hookity CLI v0.1')

    subparsers = parser.add_subparsers(title="Liste des commandes autorisées",help='Commandes disponibles', dest='command')

    # Init command
    subparsers.add_parser('init', help='Initialisation de Hookity dans votre projet git.')

    # Install command
    subparsers.add_parser('activate', help='Installer et initialiser les configurations Hookity Git dans votre repository.')

    args = parser.parse_args()

    if args.command == 'init':
        init_command()
    elif args.command == "activate":
        install_command()

if __name__ == "__main__":
    main()