
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
# git checkout -B Dev2 // Este comando crea y me mueve al branch que cree
# para juntar todo lo que hice en los branch creo un *Pull requests* en el Github

# git merge main Dev2 // para empujar lo que tengo en el main a un brach - generalmente se hace cuando hay un conflicto por que github encuentra codigo en las mismas lineas de codigo y no sabe que sobreescribir

# git reset --hard // Resetea el codigo al ultimo commit que tenga guardado
# git checkout HEAD -- IniciosGit // Esto permite resetear uno de los archivos que alla editado pero no todo como el comando anterior. Es importante especificar cual es el archivo que necesitas resetear, en este caso solo estamos trabajando en IniciosGit.

# git log // muestra el historial de los commit que haya hecho dependiendo del archivo en el que este posicionado
# git log --oneline // Es lo mismo que la anterior linea pero esta es de manera mas reducida
# git log --oneline --graph // Lo mismo pero mejor organizado visualmente
    # Puedo usar un git log oneline y copiar el codigo de algun commit anterior que haya hecho para regresarme a el haciendo un git checkout
    # git checkout CODIGO_COMMIT Ej: (97a5d98)

# se hacen RELEASE en github para liberar el codigo, como decir ya termine hago un release

# Se hacen Issue en github para dar a conocer error o problemas existentes en el codigo o en la funcionalidad del software como tal
