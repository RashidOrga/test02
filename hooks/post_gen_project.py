# import subprocess

# subprocess.call(['git', 'init'])
# subprocess.call(['git', 'add', '.'])
# subprocess.call(['git', 'commit', '-m', 'Initial commit_'])
# subprocess.call(['git', 'remote', 'add', 'origin', "{{cookiecutter.github_repo_link}}"])
# subprocess.call(['git', 'push', '--set-upstream', 'origin', "master"])

import os
import subprocess

def run_command(command):
    """Exécute une commande dans le shell et gère les erreurs."""
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode('utf-8')}")
    else:
        print(result.stdout.decode('utf-8'))

def main():
    # Accéder aux variables définies dans cookiecutter.json
    project_name = os.getenv('COOKIECUTTER_PROJECT_NAME')
    project_slug = os.getenv('COOKIECUTTER_PROJECT_SLUG')
    author_name = os.getenv('COOKIECUTTER_AUTHOR_NAME')
    description = os.getenv('COOKIECUTTER_DESCRIPTION')

    # Exemple d'utilisation des valeurs
    print(f"Création du projet: {project_name} ({project_slug})")
    print(f"Auteur: {author_name}")
    print(f"Description: {description}")

    # # Initialiser le dépôt Git localement
    # run_command("git init")
    # run_command("git add .")
    # run_command('git commit -m "Initial commit"')

    # # Ajouter le dépôt distant et pousser (n'oublie pas de définir remote_url)
    # remote_url = "https://github.com/username/your_repository.git"
    # run_command(f"git remote add origin {remote_url}")
    # run_command("git branch -M main")  # Renommer la branche principale en 'main'
    # run_command("git push -u origin main")

if __name__ == "__main__":
    main()
