# S.I.N

#posición del texto


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define audio.menu_music = "audio/menu_music.mp3"

define o = Character("Oliver", image= "oliver", color="#ffcc00")  # Nombre verde
define d = Character("Demyan", image= "demyan", color="#232364")  # Nombre azul
define h = Character ("Aiden", image= "aiden", color= "#feaeae") #Nombre rosa

define oo = Character("???", color="#ffcc00")  # Oliver desconocido
define dd = Character("???", color="#232364")  # Demyan desconocido
define hh = Character ("???", color= "#feaeae") # Aiden desconocido

#Posicion allen

define a = Character("allen", image="allen")

image side allen feliz = Fixed(
    Transform("side Allen feliz.png", pos=(30, 700))
)
image side allen neutral = Fixed(
    Transform("side Allen neutral.png", pos=(30, 700))
)
image side allen asustado = Fixed(
    Transform("side Allen espantao.png", pos=(30, 700))
)

# Disable rollback entirely
define config.rollback_enabled = False

# Declare images used by this game.
image bg demo = "fondo.png"
image bg oficina_demyan = "oficina demyan.jpg"
image bg cafeteria = "cafetería.jpg"
image bg recepcion = "recepcion.jpg"
image bg escaleras = "escaleras.jpg"
image bg lobby = "lobby.jpg"
image bg escritorio_allen ="escritorio allen.jpg"
image bg oficina = "oficina.jpg"

image aiden neutral = "aiden_neutral.png"
image aiden feliz = "aiden_feliz.png"
image aiden enojado = "aiden_nojao.png"

image oliver neutral = "oliver_neutral.png"
image oliver feliz = "oliver_feliz.png"
image oliver enojado = "oliver_nojao.png"

image demyan neutral = "demy_neutral.png"
image demyan feliz = "demy_feliz.png"
image demyan enojado = "demy_nojao.png"

label splashscreen:
    scene black 
    with Pause(1)

    # Primera imagen (logo de kalico)
    play sound "audio/kalico.mp3"
    show kalico_logo:
        size (1920, 1080)
        align (0.5, 0.5)
    with dissolve
    with Pause(1.5)
    hide kalico_logo with dissolve
    with Pause(0.5)

    # Segunda imagen (advertencia)
    show pantalla_advertencia:
        size (1920, 1080)
        align (0.5, 0.5)
    with dissolve  
    with Pause(3)
    hide pantalla_advertencia with dissolve
    with Pause(1)

    return

# Pantalla de advertencia.
label start:
    stop music fadeout 1.0
    scene bg black
    with fade
    
    
    a neutral "Hola, esta es mi side image."
    a asustado "esta es la otra"
    a feliz "y la ultima"
    ""

    "ADVERTENCIA: Esta demo contiene temas sensibles como"
    "suicidio, depresión, mención de violencia"
    "y otros tópicos."
    "Se recomienda discreción."
    
    scene bg black
    with fade
    play sound "aaa.mp3"
    
    # Aqui empieza el juego
    "..."
    "¿Esto es... la muerte?"
    "¿Esto es la paz de la que la biblia habla?"
    "El cielo se escucha como una mopa trapeando"

    scene bg recepcion
    play sound "mopa.mp3"
    
    "Abro los ojos lentamente"

    show allen_neutral 

    "El piso es frio pero no está humedo en lo absoluto"
    "el aire huele a azufre y cloro, es recién ahi cuando noto su prescencia."

    show oliver_neutral at center 
    stop sound

    "Un chico rubio me observa con un rostro amable, tiene un uniforme de mantenimiento mal puesto"
    "unos cuernos sobresalen de su cabeza y a pesar de eso se ve algo angelical"

    oo "Oh, no esperaba ser yo quien recibiera a un nuevo empleado, ¿Como te llamas?"
    "Su semblante no cambio en lo absoluto al preguntar eso, pero mi estomago se revolvió ¿Empleado?"
    "El rubio parecía ajeno a mi mal estar, en cambio me ofreció una sonrisa calida."

    show oliver_feliz at center 

    oo "Me gustaría saber tu nombre, ¿Puedo?"
    "Me levanto del suelo algo tenso."

menu:
    "¿Quién pregunta?":
        a "Detesto hablar con desconocidos..."
        o "¡Disculpa! ¿Donde están mis modales? Mi nombre es Oliver y Hoy me encargo del mantenimiento."
        a "Soy Allen."
        o "Un gusto Allen, espero llevarnos bien"
        "Sonreí, él no era para nada intimidante, el sonido de una puerta abriendose interrumpió nuestra conversación..."

    "No es asunto tuyo.":
        "Mi voz tiembla al hablar"
        a "No es tu problema."
        "¡¿Por que le respondi asi a esta cosa?! Por suerte no pareció importarle demasiado."
        oo "Oh... Okay"
        "La habitación se inundó de un silencio incomodo por unos minutos hasta que el rubio volvió a hablar."
        oo "El jefe te llamará pronto."
        "Luego, el chico siguió haciendo su trabajo."
        "Suspiré intentando no sentir culpa, justo cuando abrí la boca para intentar solucionar las cosas el sonido de una puerta abriendose me interrumpió..."
    "Presentarme":
        a "Me llamo Allen, ¿Tú como te llamas?"
        o "¡Soy Oliver!"
        a "Un gusto, Oliver, ¿Podrias decirme que es este lugar?"
        "Justo cuando Oliver parecia dispuesto a responder el sonido de una puerta abriendose lo interrumpió..."

"La recepción fue invadida por un frío espectral, una figura alta e imponente cruzó esa puerta roja que no vió con anterioridad"
dd "Allen"
"La voz fué gruesa y demandante, su propio nombre sonaba como una orden."
dd "Deja de jugar y entra."
"Acto seguido, volvió a desaparecer por esa puerta."
a "Bien..."
o "Suerte..."
"Escucho antes de tragar saliva y entrar."

scene bg oficina
with fade
play music "oficina.mp3"

"El aura del lugar era intimidante e hizo que finalmente tome consciencia de la situación en la que me encontraba: No sé donde estoy, ni porqué, ni cómo llegué."
dd "Llegas tarde."
"El más alto frunció el ceño, yo sólo pude reir de los nervios."
a "No sabia que tenía horarios."
"El pelinegro carraspeó"

menu:
    "¿Dónde estoy":
        a "¿Donde estamos?"
        dd "En mi oficina"
        "La habitación quedó en silencio."

menu:
    "¿Porqué estoy aqui?":
        a "¿Porqué estoy aquí?"
        dd "¿Recuerdas lo ultimo que hiciste antes de llegar?"
        "Solté un suspiro."
        a "Salté de un edificio..."
        "Sólo recibí una mirada seria."

"Cuando acabó de juzgarme continuó hablando dejandome con más dudas que respuestas."
dd "El suicidio viene con obligaciones, Allen."
dd "Y yo soy el encargado de que las cumplas."
dd "Y para empezar..."
"El silencio que siguió despúes fue casi tortuoso."
dd "Quiero un café"
a "¿Huh?"
dd "Ve a la cafetería en el piso de abajo"
d "Dile al idiota que atiende que es para Demyan"
d "Un expresso sin azúcar y cuida que no escupa en el."
a "¿Escupir?"
"Demyan frunció el ceño"
d "Ese mocoso es capaz de hacerlo si lo descuidas, más te vale no darle la espalda."

scene bg escaleras with wipeleft

"Bajo las escaleras siguiendo las señales que dicen cafeteria"
"Este lugar es como una oficina normal despúes de todo, sólo tenía un aire más siniestro"
"Y demonios"
"Y demasiado calor para usar este traje."

scene bg cafeteria with fade 

"La cafetería está casi vacía."
"Solo hay alguien detrás del mostrador."
"Cabello rubio, ojos rojos, y una expresión de absoluto aburrimiento."

show aiden neutral at center
"Al acercarme, puedo ver que es joven, tal vez de mi edad, y mucho más bajo que los otros dos demonios."

hh "¿Qué quieres?"
"A pesar de su altura era bastante intimidante."
a "¿Un café? Para demyan."
"Su expresión cambió de inmediato."
"El chico se volteó para preparar el pedido sin siquiera preguntar que café era, cómo el demonio le indicó no quitó sus ojos del rubio."
"Cuando finalmente se volteó tenía una sonrisa burlona en su rostro"
h "Así que eres el nuevo, gracías por tomar mi lugar"
"Se sentia como si fuera un chiste que no estaba entendiendo"
hh "¿Que tal te va cayendo Demyan?"
a "Sólo me envió por un café"
hh "Siempre hace eso con los nuevos, ¿Un consejo? Agradece todo el tiempo que tengas lejos de él, sabe muy bien cómo arrebatar tu libertad."
a "Entendido."
hh "No seas timido, ¿Cómo te llamas?"







return