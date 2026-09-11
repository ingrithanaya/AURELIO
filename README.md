# AURELIO
## Descripciòn 
Un asistente inteligente diseñado para apoyar a personas con discapacidad auditiva mediante 
el uso de tecnologias de Inteligencia Artificial y vision por computadora.
## Objetivo
Buscamos hacer que AURELIO facilite la comunicaciòn entre personas con discapacidad auditiva y personas oyentes utilizando reconocimiento 
de lenguaje de señas, reconocimiento de voz y respuestas inteligentes.
## Caracteristicas
-reconocimiento de lenguaje de señas con media pipe. 
-conversion de texto a voz y de voz a texto.
-reconocimiento facial por medio de la interfaz de yolo.
-inteligencia artificial para responder preguntas de una manera eficiente y fluida.
-base de datos con MYSQL para almacenar usuarios y registros.
## Tecnologias 
Python: Lenguaje de programación principal utilizado para desarrollar la lógica, módulos y funcionamiento general de AURELIO.
MediaPipe: Biblioteca utilizada para la detección y seguimiento de las manos mediante puntos de referencia (landmarks). Actualmente permite obtener 21 puntos por cada mano para generar las características utilizadas en el reconocimiento de señas.
MediaPipe Tasks: Conjunto de herramientas de MediaPipe utilizado específicamente para ejecutar el modelo Hand Landmarker empleado por AURELIO para la detección de las manos.
OpenCV: Biblioteca de visión artificial utilizada para acceder a la cámara, capturar imágenes, procesar los fotogramas y mostrar información del reconocimiento en tiempo real.
YOLO: Tecnología de visión artificial considerada para la detección de objetos y elementos dentro de AURELIO. Se cuenta con un modelo YOLOv8n dentro del proyecto para futuras funciones de detección.
Pandas: Biblioteca de Python utilizada para leer, organizar, analizar y procesar los conjuntos de datos almacenados en archivos CSV.
NumPy: Biblioteca utilizada para el procesamiento de datos numéricos y estructuras matriciales empleadas en diferentes procesos del sistema.
Scikit-learn: Biblioteca de aprendizaje automático utilizada para implementar y evaluar el modelo de clasificación, incluyendo la división de los datos de entrenamiento y prueba, métricas de evaluación y clasificación mediante Random Forest.
Random Forest: Algoritmo de aprendizaje automático utilizado actualmente para clasificar las señas estáticas de LSM a partir de las características obtenidas de los puntos de referencia de las manos.
Joblib: Biblioteca utilizada para guardar y cargar el modelo de aprendizaje automático entrenado. El modelo actual se almacena como modelo_lsm.pkl.
pyttsx3: Biblioteca de síntesis de voz utilizada para que AURELIO pueda convertir texto en audio y proporcionar respuestas mediante voz.
CSV: Formato utilizado para almacenar los conjuntos de datos de entrenamiento. Actualmente se cuenta con un conjunto de datos para señas estáticas y otro destinado a señas dinámicas.
MySQL: Sistema gestor de bases de datos considerado para el almacenamiento y administración de información relacionada con AURELIO.
Git: Sistema de control de versiones utilizado para registrar los cambios realizados durante el desarrollo, crear versiones del proyecto y mantener puntos de recuperación.
GitHub: Plataforma utilizada para almacenar remotamente el código fuente de AURELIO y mantener un respaldo del proyecto mediante un repositorio.
PowerShell: Herramienta de línea de comandos utilizada durante el desarrollo para ejecutar programas de Python, administrar archivos, instalar dependencias y realizar operaciones relacionadas con Git.
Visual Studio Code / editor de código: Herramienta utilizada para crear y modificar los archivos fuente que conforman los diferentes módulos de AURELIO.
Windows: Sistema operativo utilizado como entorno principal de desarrollo y ejecución del proyecto.
## Estado del proyecto
En desarrollo 
## Integrantes 
Ingrith itxel anaya ble 
## Profesor 
Agustin esquivel pat 
## Evidencias 
## Licencia 
Asistente autonomo que ayude a personas con discapacidad auditiva.
