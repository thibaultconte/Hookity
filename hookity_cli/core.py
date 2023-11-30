import json
import os
import argparse
import shutil
import subprocess
from colorama import Fore, Style
import pyfiglet

def get_user_input(prompt):
    dedent_prompt = prompt.strip().replace('\n', ' ').replace('  ', ' ')
    joined_prompt = ' '.join(dedent_prompt.strip().split())
    input_str = input(joined_prompt).strip()
    reformatted_str = input_str.replace(',', ' ')
    return reformatted_str

def init_command():
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Lancement de l'initialisation de Hookity...{Style.RESET_ALL}")
    current_directory = os.getcwd()
    
    git_directory = os.path.join(current_directory, '.git')
    if not os.path.isdir(git_directory):
        print(f"{Fore.LIGHTRED_EX}Il semble que vous ne soyez pas dans un répertoire Git.{Style.RESET_ALL}")
        return

    if not os.listdir(git_directory):
        print(f"{Fore.LIGHTRED_EX}Le répertoire .git est vide. Assurez-vous d'être dans un dépôt Git valide.{Style.RESET_ALL}")
        return
    
    existing_hookity_config = os.path.join(current_directory, '.hookity')
    if os.path.isdir(existing_hookity_config):
        print(f"{Fore.LIGHTYELLOW_EX}Il semblerai qu'une configuration hookity soit déjà mise en place ...{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}Lancer la commande {Fore.LIGHTGREEN_EX}'hookity install'{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}, pour installer les configurations Hookity{Style.RESET_ALL}")
        return
    
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Nous devons savoir qui vous êtes :{Style.RESET_ALL}")

    organization_name = get_user_input(f"{Style.BRIGHT}Nom de votre projet ou de votre société : {Style.RESET_ALL}")
    
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Configuration des normes conventionnelles pour vos branches Git :{Style.RESET_ALL}")

    branch_type_autorized = get_user_input(f"{Style.BRIGHT}Type de branches autorisés (Ex. Feat,Hotfix,Release,Docs,... ) (Séparé par des ,) : {Style.RESET_ALL}")
    
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Configuration des normes conventionnelles pour vos messages de commit Git : {Style.RESET_ALL}")

    commit_type_autorized = get_user_input(f'''{Style.BRIGHT}Type de commit autorisés 
                                           (Ex. build,docs,bug,feat,fix,experiment,refactor,test... ) | 
                                           (Séparé par des , ) : {Style.RESET_ALL}''')
    
    commit_scope_authorized = get_user_input(f'''{Style.BRIGHT}Scope de commit autorisés
                                             (Ex. controllers,route,middleware,view,config,service,api... ) | 
                                             (Séparé par des , ) {Fore.LIGHTRED_EX}(Laisse vide pour rien) : {Style.RESET_ALL}''')
    

    config_data = {
        'organization_name': organization_name,
        'branch_type_autorized': branch_type_autorized.split(),
        'commit_type_autorized': commit_type_autorized.split(),
        'commit_scope_authorized': commit_scope_authorized.split(),
    }

    hookity_resources = os.path.join(os.path.dirname(__file__), 'resources', '.hookity')
    shutil.copytree(hookity_resources, os.path.join(current_directory, '.hookity'), dirs_exist_ok=True)

    config_path = os.path.join(current_directory, '.hookity', 'hookity_config.json')
    with open(config_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=2)

    print(f"{Fore.GREEN}{Style.BRIGHT}Hookity initialisé avec succés dans votre dépôt Git, un nouveau dossier .hookity à été créer a la racine de votre projet git !{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Vous pouvez à présent push le dossier .hookity sur votre dépôt Git afin que vos collaborateurs puisse installer les configurations{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Exécuter la commande {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'hookity activate'{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} afin d'activer vos configurations et les rendre actives.'{Style.RESET_ALL}")


def activate_hookity_command():
    hookity_script_directory = os.path.join(os.getcwd(), '.hookity', 'scripts')
    activate_hooks_script = os.path.join(hookity_script_directory, 'activate_hookity.sh')

    if os.path.exists(activate_hooks_script):
        subprocess.run(['bash', activate_hooks_script])
    else:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Erreur : Le script activate_hookity.sh n'a pas été trouvé dans le dossier hookity.{Style.RESET_ALL}")


def deactivate_hookity_command():
    hookity_script_directory = os.path.join(os.getcwd(), '.hookity', 'scripts')
    deactivate_hooks_script = os.path.join(hookity_script_directory, 'deactivate_hookity.sh')

    if os.path.exists(deactivate_hooks_script):
        subprocess.run(['bash', deactivate_hooks_script])
    else:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Erreur : Le script deactivate_hookity.sh n'a pas été trouvé dans le dossier hookity.{Style.RESET_ALL}")


def uninstall_hookity_command():
    while True:
        user_choice = get_user_input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Attention, vous allez désinstaller complètement Hookity de votre dépôt git. Êtes-vous sûr ? {Fore.LIGHTBLUE_EX}(O ou N) : {Style.RESET_ALL}")

        if user_choice.upper() == "O":
            hookity_script_directory = os.path.join(os.getcwd(), '.hookity', 'scripts')
            uninstall_hooks_script = os.path.join(hookity_script_directory, 'uninstall_hookity.sh')

            if os.path.exists(uninstall_hooks_script):
                subprocess.run(['bash', uninstall_hooks_script])
                break
            else:
                print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Erreur : Le script uninstall_hookity.sh n'a pas été trouvé dans le dossier hookity.{Style.RESET_ALL}")
                break
        elif user_choice.upper() == "N":
            print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Désinstallation annulée.{Style.RESET_ALL}")
            break 
        else:
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Erreur : Choix invalide. Veuillez entrer 'O' pour oui ou 'N' pour non.{Style.RESET_ALL}")

def version_command():
    try:
        version = "v0.0.1"
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Hookity CLI {version}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Erreur lors de la lecture de la version : {e}{Style.RESET_ALL}")

def print_ascii_art():
    f = pyfiglet.figlet_format("HOOKITY", font="isometric3", width=150)
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{f}{Style.RESET_ALL}")

def main():
    print_ascii_art()
    parser = argparse.ArgumentParser(description=version_command())
    # Commande version
    parser.add_argument('--version', action='store_true', help="Affiche la version de Hookity")

    subparsers = parser.add_subparsers(title="Liste des commandes autorisées",help='Commandes disponibles', dest='command')

    # Init command
    subparsers.add_parser('init', help='Initialisation et configuration de Hookity dans votre projet git.')

    # Activate command
    subparsers.add_parser('activate', help='Activer les configurations Hookity Git dans votre repository (Local).')

    # Deactivate command
    subparsers.add_parser('deactivate', help='Désactiver les configurations Hookity Git dans votre repository (Local).')

    # Uninstall command
    subparsers.add_parser('uninstall', help='Désinstaller et désinitialiser toutes les configurations Hookity Git dans votre repository (HARD).')


    args = parser.parse_args()
    if args.command is None :
        print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Module développé par {Fore.LIGHTGREEN_EX}'Thibault Conte'{Style.RESET_ALL}")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}GITHUB : {Fore.LIGHTWHITE_EX}'https://github.com/thibaultconte/Hookity'{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Entrer {Fore.LIGHTGREEN_EX}'hookity --help'{Fore.LIGHTWHITE_EX} pour afficher les aides{Style.RESET_ALL}")

    if args.command == 'init':
        init_command()
    elif args.command == 'activate':
        activate_hookity_command()
    elif args.command == 'deactivate':
        deactivate_hookity_command()
    elif args.command == 'uninstall':
        uninstall_hookity_command()
    elif args.version:
        version_command()

if __name__ == "__main__":
    main()