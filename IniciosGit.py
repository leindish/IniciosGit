
# Comandos para manejar Git

# ls // mirar carpetas que tenga
# git --help // para encontrar comandos de git
# git config --list --show-origin // para ver la configuracion de mi git
# git config --global user.name "Leindish" // para ponerle nombre a mi git
# git config --global user.email "Leindish@gmail.com" // para ponerle email a mi git
# ssh-keygen -t rsa -b 4096 -C "Leindish@gmail.com"// Generar una llave de SSH - Dar enter hasta que el cree el archivo en la direccion que da
    #En Github me voy a settings - Voy a SSH and GPG keys - Creo una nueva llave SSH 
    # Voy a la consola git y escribo // clip < ~/.ssh/id_rsa.pub y luego a Github y pego en key y luego Add SSH key
#Clono el repositorio con SSH
    # Se recomienda crear una carpeta en el cd para enviar el clone de la carpeta y luego hacer el siguiente paso
    # copio lo que me da y copio en git bash // git clone ¨¨git@github.com:leindish/IniciosGit.git¨¨ // para clonar el repositorio

# git status // saber el estado en que esta mi carpeta con el repositorio que clone
# git commit -am "Mensaje" // Guardar localmente los cambios que hice
# git push origin main // empujar el cambio a la linea que necesito (en este caso se envio a la linea *main* porque asi se lo ordene)
# git fetch // Actualizar los cambios en la metadata - Luego de este debo usar el comando de halar
# git pull origin main // halar cambios del repositorio en Github

# git branch Dev1 (Le doy un nombre al branch - en este caso le puse Dev1) // Para crear branches en el repositorio desde el commit en que este posicionado - los branches son como bracitos de una misma linea
# git checkout Dev1 (git checkout main) // para moverme entre el main y los branches
