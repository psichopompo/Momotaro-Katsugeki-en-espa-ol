# Momotaro Katsugeki (PC Engine) — Diario de desarrollo de la traducción al castellano
<img width="1280" height="350" alt="xLwdNML - Imgur" src="https://github.com/user-attachments/assets/a736539e-2559-45eb-90be-39a8219a8555" />
El pasado 28 de julio publiqué la traducción al castellano de *Nekketsu Koukou Dodgeball-bu: Soccer Hen* para Mega Drive. Fue mi primer proyecto de *romhacking* y, para mi sorpresa, también la primera traducción conocida de ese juego a cualquier idioma. Después de tres días de trabajo intenso terminé con la sensación de haber aprendido muchísimo, lo suficiente, pensé, como para afrontar un segundo proyecto con bastante más confianza.

No podía estar más equivocado.

*Momotaro Katsugeki*, para PC Engine, ha terminado convirtiéndose en un desafío muy distinto. No porque el juego sea mejor o peor, ni porque el japonés resulte especialmente complicado, sino porque cada nuevo avance ha ido destapando problemas que ni siquiera imaginaba cuando decidí empezar esta traducción. Muy pronto comprendí que traducir el texto era sólo una pequeña parte del trabajo: antes había que entender cómo estaba construida la ROM, localizar fuentes, estudiar rutinas, adaptar gráficos, crear herramientas cuando hacían falta y, sobre todo, averiguar por qué las soluciones que parecían más evidentes muchas veces no funcionaban.

Y precisamente por eso nace este diario. No me he querido limitar a publicar un parche cuando todo haya terminado; me ha parecido mucho más interesante compartir el camino recorrido, los problemas que han ido apareciendo y las soluciones que, con mayor o menor acierto, nos han permitido seguir avanzando. Este texto es la versión final de ese diario: un resumen de todo el trabajo que permanece oculto detrás de un parche terminado y que, en la mayoría de los casos, nunca llega a verse.

---

## Resumen de lo conseguido

Para que nadie tenga que leerlo todo de golpe, éste es el estado del proyecto a fecha de hoy, en una lista rápida:

- **Prompt "PULSA BOTÓN RUN"** y menú **EMPEZAR / CONTINUAR** traducidos.
- **Selector CANTO DE JIZO / CARGAR** corregido y ensanchado.
- **Parrilla latina de passwords** completa, con cursor reprogramado.
- **Fuente adaptada**, con minúsculas y acentos (101 caracteres).
- **Pantalla de carga** sin bloque negro ni artefactos, y con varias partidas guardadas.
- **La prisión de la pantalla de passwords** resuelta: el botón II ahora vuelve atrás, y de forma condicional.
- **Charla de introducción** traducida y paginada, en minúsculas y con acentos.
- **Tutorial del inicio** traducido, con el bocadillo ensanchado.
- **Escena de los padres** traducida.
- **Nombres de las localizaciones del mapa** traducidos, con rótulos de aldea de caja ancha y ajustada al texto.
- **Bocadillos convertidos de vertical japonés a horizontal**, con marco apaisado, rabillo y flechas recolocados.
- **El canto de Jizo** por fin en una página limpia de tres líneas.
- **Menú RUN** traducido: Objetos, Artes, Comer, Usar, Tirar y los aliados.
- **El guion completo**: todos los aldeanos de todas las aldeas, las tiendas, el ermitaño con su quiz de 40 preguntas y sus 14 técnicas, y los diálogos repartidos por el mapa.
- **Los minijuegos** traducidos: el de piedra, papel o tijera, el de dados y los que se juegan manejando a Momotaro.
- **Los cuatro finales y los créditos** traducidos, con el staff en orden occidental.
- **Passwords secretos originales** verificados contra la parrilla latina.
- **Últimos retoques**: los nombres de tienda «Gema Solar» y «Gema Glacial», el «tu» en lugar del «vuestra» del aldeano, y un carácter fantasma que sobraba al final del minijuego oculto.

Queda un único fleco pendiente, la **firma** de la pantalla de título, del que hablo al final. Todo lo demás está cerrado.

---

## Mucho más que una traducción

Una de las cosas que más me sorprendió tras publicar mi anterior proyecto fue comprobar que mucha gente imaginaba que, gracias a la inteligencia artificial, este tipo de trabajos empiezan a ser casi automáticos. Después de apenas unos días inmerso en *Momotaro Katsugeki* puedo decir que la realidad es bastante diferente.

Quiero dejar clara una cosa desde el principio, porque me parece de justicia: **yo no tengo ni idea de romhacking**. No sé programar en ensamblador, no sabría leer una rutina de un procesador de los ochenta y no distingo un banco de memoria de otro. Todo el trabajo técnico de este proyecto lo hace la IA, y no es "ayuda": es la parte más dura y la que hace que esto exista. Sin ella yo no habría pasado del primer día.

Entonces, ¿qué pinto yo aquí? Pues resulta que bastante. Con el paso de los días hemos ido encontrando un reparto de tareas que funciona sorprendentemente bien, aunque no es una división tan limpia como podría parecer.

Yo pongo buena parte del **enfoque**: qué problema merece la pena atacar ahora, qué es importante, qué puede esperar y cuándo conviene abandonar temporalmente una línea de investigación. Yo **juego**: preparo partidas guardadas en puntos concretos, hago capturas, repito recorridos, pruebo comportamientos, comparo resultados y digo "esto no está bien". Yo pongo el **ojo**: veo que faltan cinco píxeles, que un sprite no empalma, que un rótulo está descentrado o que algo que técnicamente parece correcto no se comporta como debería. Yo hago buena parte de la **adaptación gráfica**: redibujo la pantalla de título, adapto letras, modifico fuentes, retoco tiles y rehago los elementos que necesitan una intervención artística. Yo tomo las **decisiones de traducción**: qué se traduce, cómo se formula, qué tono debe tener y qué solución encaja mejor con el espacio disponible y con el espíritu del juego. Y, sobre todo, pongo algo difícil de convertir en una lista: **intuición**. Una sensación de que quizá estamos buscando en el lugar equivocado, de que determinada prueba puede revelar algo importante o de que una solución que parece correcta va a traer problemas en otro sitio.

Pero tampoco sería correcto decir que la IA simplemente "hace la parte técnica": su papel es mucho más amplio. Puede analizar la ROM, localizar rutinas, seguir el flujo de ejecución, interpretar el motor de texto, calcular geometrías, escribir herramientas, plantear hipótesis y comprobar relaciones entre sistemas que yo ni habría considerado.

Y ahí aparece algo que no había previsto: **la colaboración no funciona en una sola dirección**. No se trata de que yo dé una orden y la IA la ejecute. Muchas veces soy yo quien se adelanta a lo que va a necesitar: si creo que hará falta observar determinado punto del juego, preparo una partida guardada concreta; si sospecho que dos rutinas están relacionadas, busco la forma de aportar capturas, breakpoints o pruebas que permitan comprobarlo; si veo un comportamiento extraño, no espero a que lo descubra, intento reproducirlo y le doy el material.

Otras veces ocurre al revés. La IA contempla posibilidades que yo jamás habría llegado a plantearme, detecta relaciones entre rutinas aparentemente independientes o señala que un problema que intentamos resolver en un punto concreto tiene su origen varias capas más abajo. Y entonces me toca a mí seguir esa pista, comprobar que no lleva a ninguna parte, o aportar una observación que cambie otra vez el enfoque.

Ahí está, para mí, la parte realmente interesante del proyecto. La intuición humana no aparece "alguna vez" como un golpe de suerte: está presente continuamente, al decidir qué probar, qué descartar, cuándo insistir y cuándo cambiar de dirección. Pero tampoco es infalible. Más de una vez una corazonada mía ha resultado equivocada y una medición la ha desmontado en segundos. Y al contrario: un análisis técnico impecable iba encaminado a una solución que sobre el papel parecía correcta, hasta que una prueba dentro del juego revelaba que algo no cuadraba.

Yo aporto contexto, criterio, observación, intuición y dirección; la IA aporta una capacidad de análisis y exploración técnica extraordinariamente amplia. Pero ninguno de los dos trabaja en un compartimento estanco. Cada descubrimiento modifica lo que sabe el otro, cada prueba puede cambiar la estrategia y cada problema puede hacer aparecer una solución que ninguno habría planteado al principio.

Y creo que ésa es la diferencia fundamental entre esto y la idea de "automatizar una traducción". No existe un botón al que pulsar y esperar: existe una investigación en la que hay que saber **qué preguntar, cuándo preguntarlo, qué información aportar, qué comprobar, qué poner en duda y hacia dónde mirar cuando parece que no queda ningún camino**. A lo largo de este diario iré mostrando ejemplos de todas estas situaciones, incluidos los errores, las hipótesis equivocadas y los callejones sin salida, porque precisamente ahí se entiende mejor cómo trabajamos.

---

## ¿Qué es Momotaro Katsugeki?

Aunque fuera de Japón sea un gran desconocido, *Momotaro Katsugeki* pertenece a una de las franquicias más queridas del país: la saga *Momotaro Densetsu* triunfó en el RPG y *Momotaro Dentetsu* se convirtió en un fenómeno con sus juegos de tablero, que siguen vendiendo millones de copias hoy.

*Momotaro Katsugeki* fue una propuesta diferente dentro de ese universo. En lugar de apostar por el rol o los tableros, trasladó a Momotaro al género de las plataformas y la acción, aprovechando además buena parte de lo que hacía tan especial al catálogo de PC Engine: escenarios muy coloridos, personajes enormemente expresivos, animaciones llenas de pequeños detalles y un sentido del humor constante.

Si tuviera que compararlo con otro juego conocido por aquí, probablemente la referencia más clara serían los *Ganbare Goemon*. Comparten esa misma mezcla de folclore japonés, fantasía, humor costumbrista y escenarios inspirados en un Japón feudal idealizado, todo ello acompañado por personajes caricaturescos con muchísimo carisma. Es ese tipo de juegos que consiguen arrancarte una sonrisa constantemente gracias a sus animaciones, expresiones y situaciones absurdas. Dentro de la propia franquicia existen también los *Momotaro Dengeki* de Game Boy, que recuerdan bastante a esta entrega y ayudan a hacerse una idea del estilo jugable que buscaba Hudson.

Pero precisamente todas esas virtudes esconden también el mayor obstáculo para cualquiera que haya pensado alguna vez en traducirlo. No sólo tiene una enorme cantidad de diálogos: muchos aparecen en bocadillos con escritura vertical y lectura de derecha a izquierda, y a eso se suman los textos integrados en gráficos y menús, que exigen adaptación manual. No es casualidad que, tras más de tres décadas, el juego siga sin traducción completa a ningún idioma. Hasta donde he comprobado sólo existe un intento muy temprano al inglés que apenas tocó algunos menús y se abandonó enseguida, sin llegar a resolver los retos técnicos de verdad.

Y quizá esa fue precisamente una de las razones por las que terminé eligiéndolo. Porque detrás de su aspecto desenfadado se escondía un desafío técnico muy superior al que imaginaba en un primer momento. *Y ahí fue donde comenzó realmente esta aventura.*

---

## Las primeras investigaciones

Cada proyecto comienza mucho antes de encontrar la primera línea de texto. Todo empezó con una pregunta sencilla: ¿cómo está construido realmente *Momotaro Katsugeki*? La experiencia del proyecto anterior servía de punto de partida, pero no podía dar nada por sentado: cada juego usa sus propias rutinas y organiza la información a su manera, por mucho que sean de la misma época.

Las sospechas estaban claras incluso antes de abrir la ROM. El mayor reto serían los diálogos en bocadillos verticales, escritos de arriba abajo y de derecha a izquierda. Mi idea inicial era convertir ese sistema en horizontal, mucho más natural para el castellano, siempre que fuera técnicamente posible. A eso había que añadir los textos integrados en gráficos, la pantalla de título, los menús, los punteros, las rutinas de impresión y la posible compresión de datos.

Las primeras horas no fueron de traducir, sino de comprender: identificar la estructura de la ROM, preparar herramientas para inspeccionar gráficos y código, y recopilar capturas de distintas zonas del juego como referencia visual. Y entonces llegó la primera buena noticia: muy pronto quedó claro que, al menos una parte muy importante del texto del juego, no estaba comprimida de forma global. Aquello abría una puerta enorme, porque antes incluso de comprender por completo el funcionamiento interno del motor de texto ya era posible empezar a localizar mensajes, estudiar la codificación utilizada y analizar cómo se organizaban los distintos bloques de diálogo. No era, ni mucho menos, el final del problema; en realidad, sólo era el comienzo. Pero por primera vez el proyecto dejaba de ser una idea para convertirse en una investigación con un camino real por delante.

Muy pronto nos dimos de bruces con un problema que yo no habría sabido ni nombrar. El PC Engine no lleva el procesador habitual de la época, sino uno propio con instrucciones que los programas de análisis no conocen. ¿La consecuencia? Que al leer el código, en cuanto aparecía una de esas instrucciones raras, todo lo siguiente salía mal: instrucciones inventadas, saltos a ninguna parte, basura. Estuvimos un buen rato persiguiendo fantasmas hasta caer en que el problema no estaba en el juego, sino en la herramienta que lo leía. La solución fue construir una a medida: unos cientos de líneas, nada del otro mundo, pero probablemente lo más rentable del proyecto.

La lección es muy de andar por casa: cuando algo no cuadra, a veces no falla lo que estás mirando, sino con qué lo estás mirando. A partir de ese momento empezaría el verdadero trabajo de ingeniería inversa: localizar las fuentes, entender la codificación del texto, seguir el rastro de los punteros y descubrir, paso a paso, cómo conseguía el juego mostrar cada uno de sus diálogos.

---

## La fuente y la tabla de caracteres

Uno de los primeros objetivos era averiguar cómo almacenaba el juego su texto. La incógnita era si nos encontraríamos una ROM completamente comprimida o si parte del guion estaría accesible, porque esa diferencia podía convertir un proyecto abordable en uno casi imposible. Por suerte, buena parte del texto aparecía almacenada en claro, con una codificación japonesa de un byte basada en katakana. Se podían localizar diálogos y entender cómo estaban organizados antes incluso de desentrañar el motor de texto. No era la solución, pero sí la primera puerta abierta.

El primer hallazgo importante fue que el juego no tiene una fuente, sino **dos**, y son completamente distintas: una para los diálogos y otra para los menús. Distinto tamaño de letra, distinta manera de guardarlas y, sobre todo, distinta forma de buscar cada carácter. Parece un detalle menor y ha sido una de las trampas más caras del proyecto. Varias veces medimos algo en una fuente, lo dimos por bueno y lo aplicamos en la otra, con resultados desastrosos. Al final se convirtió en una de nuestras reglas de trabajo, escrita con todas las letras: *lo medido en una fuente no vale para la otra*.

```
                 DIÁLOGO              MENÚ
banco            $1E                  $02
base en la ROM   0x3D660              0x4000
tamaño de glifo  8 bytes, 1 bpp       16 bytes (cuerpo + sombra)
cómo se indexa   tabla en 0x43F9B     directo
la usan          intro, tutorial,     rótulos de dificultad
                 diálogos, password
```

La tabla de caracteres tiene su propio truco. El juego usa una codificación de un byte: los códigos por debajo de **0xA0** pasan por una tabla de traducción situada en **0x43F9B**, que convierte el código en un número de glifo, mientras que los códigos a partir de **0xA1** van por lo que llamamos la "ruta katakana", en la que el código *es* directamente el glifo, sin tabla intermedia. Esa segunda ruta resultó ser la clave para meter minúsculas y acentos: como no pasa por la tabla compartida, **podíamos añadir caracteres nuevos sin riesgo de romper ninguna otra pantalla**. El conjunto final tiene 101 caracteres.

```
mayúsculas   A-Z         códigos $41-$5A (la ruta baja, tabla 0x43F9B)
minúsculas   a-z         códigos $A1-$BA (ruta directa, sin saltos)
acentos      á é í ó ú   ü ñ ç  y sus mayúsculas
signos       ¿ ¡ . , : ; … ' " - / ( ) % & +
```

Un detalle curioso: tres letras minúsculas (**b**, **c** y **p**) tienen además un código alternativo en la ruta baja, herencia de la parrilla de passwords.

Mezclados con el texto aparecen también bytes que no son letras, sino instrucciones para el motor: el **0x00** marca fin de línea, el **0xFC** fin de página, el **0xFE** espera de botón, el **0x3C** es un espacio, el **0x5C** alterna entre las dos fuentes, el **0xFB** es un marcador de posición para un dígito y el **0xFF** cierra el bloque. El **0xFB** tiene su propia historia, que cuento en el capítulo de la escena de los padres.

Y hubo un glifo con sorpresa: el código **0x24** resultó ser el kanji **両**, la moneda del juego, el *ryō*. Lo descubrimos volcando la fuente entera como imagen, que acabó siendo otra de nuestras reglas: *antes de dibujar un glifo, volcar la fuente completa*. Se ahorran muchas sorpresas.

A partir de ahí comenzó uno de los trabajos más importantes de toda la investigación: identificar qué significaba cada byte que aparecía mezclado con el texto. Pronto fueron apareciendo los primeros códigos de control, responsables de cambiar de bocadillo, finalizar un mensaje, introducir pausas o modificar la forma en que el juego representaba los diálogos. Cada nuevo código identificado permitía comprender un poco mejor el funcionamiento interno del motor de texto y acercaba la posibilidad de realizar una traducción completa.

Sin embargo, el descubrimiento que más me llamó la atención fue otro: los diálogos verticales no eran gráficos dibujados manualmente, como en un primer momento podía parecer, sino texto generado dinámicamente por el propio juego. Entre los caracteres aparecían una serie de separadores que todo apuntaba a que indicaban el cambio de columna en los bocadillos verticales. Aquello cambiaba completamente la perspectiva del proyecto, porque el problema ya no consistía únicamente en traducir el japonés al castellano, sino en encontrar la forma de convencer al propio juego de que dejara de escribir en vertical para hacerlo de una manera natural en nuestro idioma.

Fue uno de esos momentos en los que una investigación responde una pregunta y, al mismo tiempo, plantea otras diez mucho más difíciles. Pero también fue la primera vez que tuve la sensación de que el proyecto empezaba a dejar de ser una incógnita para convertirse en un problema que, con paciencia, podía llegar a resolverse.

---

## Adaptación gráfica y pixel art

Cuando pensamos en una traducción solemos imaginar únicamente el texto, pero en muchos juegos de principios de los noventa una parte importante del idioma no está almacenada como tal, sino integrada directamente en los gráficos. Pantallas de título, menús, carteles, indicadores y logotipos forman parte del propio apartado artístico del juego, y *Momotaro Katsugeki* no es una excepción.

Desde el principio quedó claro que una traducción completa exigiría mucho más que localizar los diálogos: también habría que adaptar una gran cantidad de elementos gráficos para que el resultado final pareciera un lanzamiento pensado desde el primer momento para el mercado español. Ésta es, por cierto, la parte del proyecto que sí llevo yo enteramente. Es curioso el contraste: mientras al otro lado se están desmenuzando rutinas de ensamblador, yo estoy peleándome con un editor de píxeles y contando cuadraditos.

Algunas tareas fueron relativamente sencillas, como sustituir pequeños textos japoneses integrados en gráficos, pero otras resultaron bastante más laboriosas. La pantalla de título, por ejemplo, obligó a replantear por completo el diseño original para crear una versión en castellano que mantuviera la personalidad del logotipo japonés sin limitarse a copiarlo literalmente. No se trataba simplemente de escribir otro texto, sino de respetar el ritmo, el equilibrio y el carácter del diseño original, adaptándolo al espacio disponible y a las limitaciones propias del hardware de PC Engine.

Algo parecido ocurrió con la tipografía: en algunos casos fue necesario modificar caracteres existentes y en otros crear letras completamente nuevas para que el castellano pudiera representarse con naturalidad, respetando siempre el estilo gráfico del juego. Mi objetivo nunca ha sido que el jugador perciba constantemente que está jugando a una traducción; al contrario, siempre que ha sido posible he intentado que cada elemento adaptado dé la impresión de haber formado parte del juego desde el primer día. Esa búsqueda de naturalidad ha terminado convirtiéndose en uno de los aspectos que más tiempo está consumiendo durante el proyecto, pero también en uno de los que más satisfacción produce cuando una pantalla empieza a parecer exactamente como la imaginabas.

---

## El arranque: el prompt y el menú principal

Una vez comprendida la estructura de la ROM y la codificación del texto, llegó el momento de poner los pies en el suelo y empezar a tocar pantallas reales. Y el punto de partida natural era, como no podía ser de otra manera, el arranque del juego.

Lo primero que aparece nada más encender es la pantalla de título, con el rótulo en japonés y, bajo él, un pequeño texto que invita a pulsar el botón de inicio. Ese primer texto era el "PULSA BOTÓN RUN", un mensaje sencillo, directo y perfecto para hacer las primeras pruebas con la fuente latina. Y aquí empezó el primer aprendizaje importante: no todo el texto del juego se dibuja de la misma manera. Algunos textos se escriben como caracteres normales, pero otros se generan proyectando bloques gráficos en la VRAM y mostrándolos después como sprites. Ese segundo caso es bastante más delicado, porque el juego sólo prepara tantos bloques como necesitaba el texto japonés original. Si la frase en castellano es más larga, los bloques adicionales no existen y acaban apareciendo con basura gráfica. Ese mismo patrón iba a repetirse en casi todas las pantallas: el texto en castellano casi siempre es más largo que el japonés, y el juego rara vez está preparado para esa diferencia.

El siguiente paso fue el menú principal, EMPEZAR / CONTINUAR. Aquí lo interesante no fue el texto en sí —dos palabras cortas que caben sin problema—, sino descubrir que **el flujo del juego cambia por completo según haya o no una partida guardada**. Esa bifurcación, que en principio parecía un detalle sin importancia, terminaría siendo una de las claves de todo el proyecto y protagonizando uno de los capítulos más largos de este diario.

La estructura es la siguiente: al elegir **EMPEZAR** (sin partida guardada) se accede directamente a la pantalla de introducción de la contraseña del canto de Jizo; si **hay una partida guardada**, al elegir **CONTINUAR** no se entra directo al password, sino al selector **CANTO DE JIZO / CARGAR**, y desde ese selector, **CANTO DE JIZO** te lleva a la pantalla de password y **CARGAR** te lleva a la pantalla de carga de partidas guardadas.

Y aquí hubo un detalle que nos habría ahorrado semanas, y que teníamos delante. Esa bifurcación no la decide una variable suelta que podamos consultar cuando queramos: la resuelve una rutina concreta del juego, que cuenta las partidas guardadas y devuelve el resultado. En el código tiene esta pinta:

```
$EA87  JSR $EAE6      ; ¿hay partida guardada?
$EA8A  BCC $EA94      ;   NO -> saltarse el selector
$EA8C  JSR $FBB3      ;   SÍ -> ir al SELECTOR
$EA94  JSR $FC18      ; password
```

Lo documentamos aquí, en la segunda pantalla del juego. Y luego pasamos días peleándonos con un problema que se resolvía exactamente con esas tres líneas. Lo cuento en el capítulo del botón II, que es donde toca pasar vergüenza.

Con el prompt traducido y el menú principal resuelto, el siguiente gran reto era la pantalla de passwords. Un capítulo que merece su propio espacio.

---

## El reto de la pantalla de passwords

Con buena parte de la ROM ya comprendida, quedaba el que sería uno de los mayores retos del proyecto. A simple vista, la pantalla de passwords parece de lo más sencillo: una cuadrícula de caracteres y unas pocas opciones. Por dentro mezcla fuente, gráficos generados en VRAM, sprites, tilemaps, lógica japonesa de kana, control de cursor y validación interna. Y todo diseñado alrededor del silabario japonés, así que al pasarlo a una parrilla latina no basta con cambiar los dibujos: hay que adaptar la lógica para que el cursor, los valores internos y la validación sigan funcionando. Lo que sigue resume bien la filosofía del proyecto: detrás de un cambio aparentemente pequeño suele esconderse una cantidad enorme de trabajo que el jugador nunca ve.

La pantalla original usa caracteres japoneses; para la traducción se sustituyó por una parrilla latina con letras, eñe y números. La distribución final es ésta:

```

A B C D E F G     a b c d e f g

H I J K L M N     h i j k l m n

Ñ O P Q R S T     ñ o p q r s t

U V W X Y Z       u v w x y z

    0 1 2 3 4     5 6 7 8 9

```

No es una simple tabla alfabética lineal. Opté por esta disposición porque visualmente encaja mejor en la pantalla y permite separar mayúsculas, minúsculas y números de forma clara. Fue una suerte que el total de los caracteres japoneses en la parrilla coincidiera exactamente con la suma de las letras del abecedario en mayúsculas y minúsculas más los números del 0 al 9: 64 caracteres en total. Esto era importante porque a cada carácter japonés había que asignarle uno latino.

Y aquí hubo un susto que merece contarse, porque la lección vale para cualquier proyecto. Metiendo las minúsculas y las vocales acentuadas para los diálogos, de pronto **la parrilla apareció plagada de letras Á** donde tenía que haber puntos, y el menú lateral mostraba "..RÁS" en vez de "ATRÁS". Lo primero fue comprobar si se habían pisado los datos de la parrilla: estaban intactos, byte por byte. El destrozo venía de otro sitio. Resulta que la tabla que traduce códigos a dibujos **es global**, y al meter los acentos se habían redirigido doce entradas. Una de ellas apuntaba al puntito que la parrilla usa como separador. La parrilla no es texto, es un mapa de tiles, pero el juego lo resuelve **con la misma tabla**, así que cada punto de la rejilla pasó a dibujar una "Á".

Lo interesante es por qué no se detectó antes. Se había hecho un inventario para comprobar que esos códigos no se usaban en ninguna parte, y dio el visto bueno. El fallo: se buscaron **sólo en los textos**. La parrilla no es un diálogo, así que el barrido ni la miró. La conclusión fue que esos códigos "no aparecen en ningún texto del juego", lo cual era rigurosamente cierto y completamente irrelevante.

> Comprobar que algo no se usa "en los sitios que conozco" no es comprobar que no se usa.

Y aún hubo una segunda regresión, porque de los doce códigos elegidos, cinco apuntaban a dibujos de katakana que sí estaban en uso y aparecieron superpuestos sobre el menú lateral. Al final el criterio que funcionó fue el más conservador: usar únicamente las casillas de la fuente que estaban **completamente vacías**.

La parrilla japonesa no es un rectángulo perfecto: tiene huecos. La latina tampoco (la última fila de mayúsculas se queda en seis letras y la de números arranca desplazada), así que hubo que reprogramar los saltos del cursor para que no se metiera en casillas vacías ni se saltara letras, con tratamiento propio para pasar de una fila a otra o bajar de las mayúsculas a los números. También hubo que redibujar buena parte del abecedario —los glifos originales estaban pensados para kana, que ocupa toda la celda, y las letras latinas quedan mejor con un pequeño margen— y arreglar un desajuste por el que, a partir de cierta letra, los glifos salían desplazados: el índice de la tabla no coincidía con la posición real en la fuente.

Debajo de la parrilla, el juego muestra la contraseña que vas escribiendo, con puntos gruesos marcando las posiciones vacías y barras separando los grupos. Al principio aparecían letras incorrectas en los huecos, porque los patrones de los puntos se solapaban con los de los nuevos caracteres latinos. Hubo que reasignarlos.

Las opciones laterales (introducir, borrar, espacio, terminar) estaban en japonés. Un detalle que descubrí probando: la que parecía significar "insertar" era en realidad el **espacio**, y el juego lo representaba con una interrogación, lo cual era de lo más confuso; lo cambiamos por un espacio en blanco de verdad. El mensaje de cabecera no cabía y hubo que ampliar los bloques gráficos que el juego reserva para esa línea, y lo mismo con el mensaje de error de contraseña incorrecta, que en castellano se salía de la caja: hubo que ensanchar el texto y el gráfico del marco.

Un punto importante: como cada casilla latina ocupa la posición de una sílaba japonesa, los valores internos no cambian y **las contraseñas originales siguen siendo válidas**. Los passwords secretos que trae el juego están comprobados y funcionan tecleados en la parrilla latina (los dejo al final, en un desplegable, para quien no quiera verlos). Y de paso apareció un detalle que resultó utilísimo después: **los secretos no pasan por el mismo camino que los normales**. Un password corriente atraviesa tres filtros (se desempaqueta, se descifra con su suma de control y se valida); los secretos se comparan tal cual contra una tabla. Eso los convirtió en una sonda perfecta: si un secreto funciona, toda la cadena desde la parrilla hasta la memoria está bien, sin necesidad de poner un solo punto de ruptura. Eso sí, sólo ejercitan treinta de las sesenta y cuatro casillas, así que no valen como prueba de que la entrada entera esté bien.

Al cambiar los caracteres de la parrilla, un password que en japonés era una palabra reconocible ahora aparece como una secuencia de letras latinas aparentemente aleatoria. Funciona igual, pero ha perdido la "gracia" de que se leyera como algo — un precio asumido, y una de las pocas pérdidas conscientes del proyecto.

---

## El selector CANTO DE JIZO / CARGAR

Después de la pantalla de passwords, el siguiente frente fue el selector *CANTO DE JIZO / CARGAR*. Recordemos el contexto: cuando hay una partida guardada, al elegir CONTINUAR el juego no va directo a la pantalla de password, sino que muestra este pequeño menú con dos opciones.

El problema era doble. Por un lado, el texto en castellano de "CANTO DE JIZO" y "CARGAR" no cabía en el bocadillo original, pensado para las palabras japonesas, mucho más cortas; el texto se salía por los lados y se cortaba. Por otro lado, al ensanchar el texto apareció un problema de solapamiento: las dos opciones compartían zona de memoria y, como "CANTO DE JIZO" era más largo, invadía el espacio que debía ocupar "CARGAR". El resultado era un texto ilegible en el que ambas líneas se mezclaban.

Para entenderlo había que saber cómo dibuja el juego estos menús. El texto no se escribe como caracteres normales: el juego genera bloques gráficos en la VRAM y luego los proyecta como sprites. Cada opción del menú tiene reservado un número fijo de bloques, calculado para el texto japonés. Al traducir a frases más largas, los bloques que faltan no se preparan, así que aparecen con basura gráfica o invaden los bloques de la opción vecina. La solución pasó por ampliar el espacio reservado para cada opción y reorganizar los destinos de memoria para que ninguna línea pisara a la otra.

Una vez resuelto el texto, tocaba el marco. El bocadillo original era demasiado estrecho y había que ensancharlo para que cupiera "CANTO DE JIZO" sin desbordar, pero sin descolocar el resto de la pantalla. El texto del selector está alineado a la izquierda, con un pequeño melocotón como puntero de selección; la frase más larga marca el ancho necesario, dejando un margen de unos 8 píxeles a cada lado, y el conjunto queda centrado en pantalla. Fue un trabajo de ajuste fino: ampliar el marco, recolocar el texto y asegurarse de que el melocotón siguiera señalando correctamente cada opción.

Durante esta fase hubo un momento de confusión importante: perseguimos durante horas "la lista de sprites" que proyectaba el texto del selector... y no existía. El texto del selector no se dibuja con sprites, sino en el plano de fondo. Lo que parecían patrones de letras eran, en realidad, el relleno negro y las esquinas del marco de la caja. Fue un buen recordatorio de que, en romhacking, a veces la hipótesis más razonable es exactamente la equivocada.

---

## La pantalla de carga de partidas guardadas

La tercera parada del flujo fue la pantalla de carga de partidas guardadas. Aquí el juego muestra la pregunta *"¿Cuál quieres cargar?"* y, debajo, la lista de partidas guardadas con su nombre y dificultad. El reto principal era el mismo de siempre: la pregunta en castellano es mucho más larga que el texto japonés, y el bocadillo no estaba preparado para ella. Pero esta pantalla tenía además dos problemas añadidos que terminaron siendo muy ilustrativos: el **bloque negro** y el **artefacto gráfico**.

En cuanto traducimos la pregunta, apareció un bloque negro que la tapaba parcialmente. Al ensanchar el texto de 3 a 5 bloques por línea, aparecieron unos sprites que ya no encajaban en ninguna parte y se quedaron flotando encima de la pregunta. La solución de aquel momento fue una chapuza, y lo digo sin acritud: **alinearlos** sobre las letras "uá" de la palabra "Cuál", de modo que el bloque negro dejara de verse como una mancha y pareciera parte del texto. Funcionaba, se veía igual en todos los emuladores y nos permitió seguir avanzando. Pero nunca me convenció. Recuerdo haber dicho entonces que ese bloque claramente no estaba donde debía y que aquello acabaría dando problemas. Tardó semanas, pero acabó dándolos, y de qué manera. La historia completa está más abajo, en su propio capítulo.

El segundo problema era más sutil: junto a la partida guardada aparecía un artefacto gráfico, un recuadro con píxeles sueltos, que curiosamente sólo se veía en un emulador concreto (Mesen) mientras que en otros pasaba desapercibido. El dato más revelador fue que la ROM japonesa original funcionaba perfectamente, es decir, el artefacto era 100% culpa de nuestra traducción. La causa estaba en la limpieza de la VRAM: al ensanchar las líneas de la pantalla de carga, las direcciones de memoria donde se dibuja el texto cambiaron, pero la rutina que limpia la VRAM seguía limpiando el rango antiguo, dejando sin limpiar las zonas nuevas, donde se acumulaba basura gráfica. La solución fue ampliar el rango de limpieza para que cubriera todas las líneas nuevas, y tras el ajuste el artefacto desapareció en todos los emuladores.

La lección de este capítulo: al ensanchar cualquier texto, no basta con que "se vea bien" a primera vista, hay que revisar todas las rutinas que dependen del ancho (la limpieza de memoria, los sprites sobrantes, los tiles reservados...) y, además, probarlo en varios emuladores, porque un bug puede ser invisible en uno y evidente en otro.

---

## La prisión de la pantalla de passwords

Hubo un momento del proyecto en el que dejé de pensar en la pantalla de passwords como un simple menú: empecé a verla como una prisión. Y no es una metáfora. Si el jugador entraba en ella, sólo existían dos formas de salir: introducir una contraseña válida... o pulsar el botón RESET de la consola. Así funcionaba el original y probablemente nadie en Hudson se planteó que resultara incómodo. Pero lo curioso era que el propio juego ya tenía la solución: en otros menús bastaba con pulsar el botón II para volver atrás. ¿Por qué precisamente ésta era la excepción?

La idea parecía tan sencilla que apenas le di importancia: pensé que era una mejora de calidad de vida para una tarde. No podía estar más equivocado. Desde ese momento el proyecto dejó de consistir en traducir un juego: ahora intentábamos enseñarle a hacer algo que nunca había sabido hacer.

Localizadas las rutinas de navegación, conseguimos que el botón II respondiera. Pulsabas y abandonabas la pantalla. Problema resuelto, o eso parecía: bastaron unos minutos de pruebas para ver que el cambio producía efectos inesperados en *otras* pantallas. Lo que vino después fue de las fases más desconcertantes de toda la investigación. Cada modificación arreglaba un problema y destapaba otro: bloques negros donde antes no había, textos ligeramente desplazados, pantallas que dejaban de actualizar zonas de la VRAM, retornos que conducían al lugar equivocado. Era como reparar un reloj tocando sólo los engranajes visibles: cada pieza estaba conectada con otra y ninguna venía con plano.

Uno de los errores más curiosos apareció al probar qué ocurría si el jugador intentaba salir sin tener ninguna partida guardada. Lo lógico era que no pasara nada. En cambio, terminábamos en la pantalla de carga y el juego permitía cargar una partida... inexistente. El resultado era digno de una película de ciencia ficción: escenarios rotos, variables con valores absurdos, el personaje con cantidades desorbitadas de vidas y dinero imposible de conseguir jugando. Otras veces la partida "funcionaba" de forma engañosa, que era todavía más traicionero. No era ningún secreto oculto: era el juego interpretando como partida válida unos datos que nunca habían sido pensados para eso. Y demostraba hasta qué punto una modificación aparentemente inocente puede alterar zonas del programa que en teoría no tienen nada que ver.

Durante esos días el trabajo dejó de parecerse a una traducción. Se generaban ROMs de prueba y se analizaban rutinas; yo cargaba cada versión, repetía el mismo recorrido veinte veces, hacía capturas, colocaba puntos de ruptura siguiendo instrucciones y contaba lo que veía. Muchas veces una explicación parecía impecable hasta que una prueba en pantalla demostraba que mirábamos el problema desde el sitio equivocado.

La mayor complicación fue que lo que funcionaba en un emulador fallaba en otro. Ciertos huecos de memoria arrancan con valores distintos según el emulador: un dato que en uno vale cero, en otro vale cualquier cosa, y nuestra comprobación tomaba caminos distintos según lo que encontrara. Llegamos a probar ocho versiones, cada una leyendo el dato de un sitio diferente; ninguna funcionaba en los dos emuladores a la vez y algunas ni arrancaban. Así que se tomó una decisión pragmática: que el botón II reseteara al título en todos los casos. Era lo más robusto —no rompía nada, funcionaba en todas partes y cumplía el objetivo de escapar de la prisión— y ahí se quedó la cosa durante semanas.

Mucho después, con el resto del proyecto avanzado, volví sobre el asunto: no me gustaba haber renunciado al comportamiento correcto. Y apareció la respuesta más humillante posible: **el juego ya sabía tomar esa decisión**. La tomaba cada vez que el jugador elegía CONTINUAR en el menú principal.

```
$EA87  JSR $EAE6      ; ¿hay partida guardada?
$EA8A  BCC $EA94      ;   NO -> saltarse el selector
$EA8C  JSR $FBB3      ;   SÍ -> ir al SELECTOR
```

Esa rutina cuenta las partidas guardadas, lleva ahí desde 1990, se ejecuta en cada arranque y está probadísima por el propio juego en todos los emuladores del mundo. Los ocho intentos anteriores fallaban por lo mismo: cada uno leía un dato **por su cuenta**, en un momento en que la memoria no estaba lista, y sobre valores que dependen del emulador. La solución no era leer mejor el dato: era **no leer ninguno** y dejar que lo hiciera el juego.

El parche final ocupa **diez bytes**:

```
$FF5A  JSR $EAE6     ; que decida el juego
$FF5D  BCC $FF65     ; sin partida -> título
$FF5F  LDX #$FF
$FF61  TXS
$FF62  JMP $EA8C     ; con partida -> selector
$FF65  JMP $E000     ; sin partida -> título
```

Funciona en Beetle, funciona en Mesen, y con partida guardada te lleva al selector mientras que sin ella te lleva al título. Exactamente lo que queríamos desde el principio.

Es la historia que mejor resume el proyecto: días peleándonos con memoria, emuladores y comportamientos raros para descubrir que la solución era llamar a una función que llevaba treinta y cinco años en la ROM, documentada desde la segunda pantalla del juego. Hay una tentación constante de escribir código nuevo, y casi siempre es mejor mirar antes si el juego ya sabe hacerlo.

Nadie que juegue pensará en esta mejora: entrará, pulsará el botón II, volverá atrás y seguirá jugando. Ése era justo el objetivo, porque las mejores modificaciones son las que parecen parte del juego original. Pero detrás de esa fracción de segundo hubo días de investigación, pruebas, hipótesis descartadas y una cadena de errores que nunca habrían aparecido limitándonos a traducir textos. Fue entonces cuando comprendí que esto ya no consistía sólo en localizar un juego japonés, sino en entenderlo lo bastante como para enseñarle cosas que nunca había hecho.

---

## La introducción y el idioma de los diálogos

Con la base estable, el siguiente objetivo fue traducir la charla de introducción que aparece al pulsar EMPEZAR, antes del selector de dificultad. Es el momento en que el juego te da la bienvenida, te explica que cualquiera puede superar *Momotaro Katsugeki* y te anima a elegir el Modo Fácil si es tu primera vez.

Localizar ese texto costó lo suyo: el puntero que el juego usa para leerlo se monta sobre la marcha, así que no basta con buscarlo en la ROM. Tras bastante trabajo apareció la rutina que lo carga. El texto japonés ocupaba 391 bytes y nuestra traducción necesitaba más espacio, así que hubo que reubicarlo en una zona libre y redirigir el puntero. Sólo había que tocar dos bytes; encontrarlos fue lo difícil.

Al insertar el texto en español apareció un problema inesperado: los diálogos no mostraban bien los acentos ni las minúsculas. Éste es uno de esos momentos en los que una investigación da un giro completo. Al principio dimos por hecho que había que dibujar glifos nuevos y buscarles hueco, un trabajo considerable. Pero al estudiar con calma cómo el juego convierte un código en un dibujo, apareció el detalle clave: **hay dos caminos distintos**, y uno de ellos no pasa por la tabla que comparten todas las pantallas. Eso significaba que podíamos añadir minúsculas y acentos **sin riesgo de romper la parrilla del password ni ninguna otra cosa**. De un problema que parecía requerir días pasamos a una solución limpia y segura.

Hay una peculiaridad que confunde a cualquiera que pruebe una versión intermedia: cuando el bocadillo todavía tiene el texto japonés pero ya está cargada la fuente latina, **el texto se ve como una ristra de símbolos raros**. Parece que algo se ha roto, pero no: los bytes japoneses caen en la ruta directa y se dibujan con las letras latinas que ocupan esas posiciones. En cuanto se inserta el texto en castellano, todo aparece perfecto. Me ha pasado en cada pantalla nueva, y en cada una he tenido que recordarme que es lo normal.

Un detalle importante de la charla es cómo se muestra en pantalla: el bocadillo sólo enseña 4 líneas a la vez, con 24 caracteres por línea, el texto va haciendo scroll y una flecha indica cuándo pulsar para continuar. Para la traducción montamos un pequeño repartidor automático: se le da el texto corrido y él lo parte en líneas de 24 caracteres sin cortar palabras, agrupándolas en páginas de 4. Las once páginas de la introducción están hechas así, y alguna línea queda clavada en el límite. Ese repartidor es el germen de algo más ambicioso: cuando toque traducir el grueso del guion, la idea es que el mismo sistema reparta automáticamente todos los diálogos del juego.

---

## El tutorial del inicio: el primer bocadillo ensanchado

Superada la introducción, lo siguiente era el pequeño tutorial que aparece nada más empezar a jugar, donde el juego te explica que esquives lo que cae del cielo y llegues a la meta. Cuatro frases cortas. Y aquí llegó el primer choque de verdad con la geometría del juego.

El bocadillo original permite **16 caracteres por línea**. En japonés sobra: el kana es muy compacto. En castellano no llega ni de lejos. Una frase tan simple como "¡Esquiva los ñordos que caen!" no cabe partida en dos líneas de 16. Así que tocaba ensanchar el bocadillo. Y ensanchar un bocadillo en este juego resultó ser bastante más complicado de lo que parece, porque no es un gráfico: es un rompecabezas de piezas pequeñas que el juego va colocando según una lista de instrucciones.

El juego tiene un motor que lee listas de registros de cinco bytes —`[patrón] [atributo bajo] [atributo alto] [dx] [dy]`—, donde cada registro coloca una pieza en una posición relativa a un punto de anclaje y la lista termina con un $FF. Un bocadillo típico se compone de una fila superior (esquina + relleno + relleno + esquina), una fila central (lateral izquierdo + TEXTO + lateral derecho) y una fila inferior (esquina + relleno + relleno + esquina, con espejo vertical), más el "rabillo" que apunta al personaje. Para ensanchar hay que reescribir esa lista: más piezas de relleno, más huecos de texto, y recalcular todas las posiciones. Además hay que ampliar la zona de memoria gráfica que el juego prepara, o las piezas nuevas mostrarán basura.

Y hay dos límites que no se pueden rebasar: las posiciones van **con signo** (de -128 a +127 respecto al ancla), así que si el bocadillo crece mucho y el ancla está en un extremo, las piezas del otro lado se salen de rango; y el PC Engine sólo puede dibujar **16 piezas por línea horizontal de pantalla**, y a partir de ahí las descarta sin avisar. Los dos nos han mordido, y más de una vez. El segundo, de forma especialmente cruel: el juego no da ningún error, simplemente deja de dibujar cosas.

Al final el tutorial quedó con 20 celdas por línea y un bocadillo de 188 píxeles, centrado en pantalla. Cuatro celdas más no parecen gran cosa, pero son la diferencia entre que una frase quepa o haya que reescribirla entera.

Y un detalle de traducción: una de las frases dice "¡Pulsa I y salta para esquivarlos!". Al principio habíamos escrito "II", por pura inercia —es el botón de salto habitual—, pero al comprobarlo contra la ROM japonesa, el texto original decía claramente **"botón I"**. Corregido. Es el tipo de detalle que sólo aparece si uno se molesta en volver al original en lugar de fiarse de lo que le parece lógico.

---

## La escena de los padres

La primera escena con diálogo de verdad del juego: los padres de Momotaro le dan dinero y unos *kibidango* antes de que parta hacia la isla de los ogros. Esta escena tenía de todo: bocadillo estrecho, tres líneas de texto, una imagen de los padres, una flecha de "continuar" y un misterio que nos tuvo un buen rato dándole vueltas.

El bocadillo de esta escena tiene tres líneas en lugar de dos, así que hubo que reescribir su lista entera: 20 celdas por línea, tres filas, 188 píxeles de ancho. Además hubo que bajar la imagen de los padres dos píxeles y mover la flecha catorce a la derecha para que quedara alineada con la curva de la esquina, como en otros bocadillos del juego. Sí, dos píxeles. Este proyecto va mucho de eso.

En el texto original de esta escena aparecían tres bytes idénticos seguidos, justo donde el juego dice cuánto dinero te dan. La primera hipótesis fue que servían para que el juego insertara ahí la cantidad, y como se rellenaban alineando a la derecha, en castellano quedaba una sangría fea antes del número. La pregunta era: ¿podemos quitarlos? El análisis inicial decía que no, porque "afectaría a todos los importes del juego". Pero al contarlos de verdad resultó que **en toda la ROM hay un único grupo de estos marcadores**, y es precisamente éste. Todos los demás importes llevan la cifra escrita directamente en el texto —seis variantes fijas, una por cantidad, ninguna usa marcadores—. Con ese dato, la prueba era de lo más tonta: cambiar los tres marcadores por el texto "50" y mirar en el juego si el dinero se sumaba igual. Se sumaba. Eran **sólo formato**, y la sangría desapareció.

Buen ejemplo de una regla que hemos aprendido a base de perder tiempo: *"afecta a todo el juego" hay que contarlo, no suponerlo*.

Al ajustar el texto surgió una duda interesante. Una frase dice "¡Llévate también un kibidango!" y otra "¡Momotaro obtiene un kibidango!". ¿Debía ser "un" o "unos"? En japonés los sustantivos no marcan número, así que hay que mirar el contexto. Y al leer el original apareció la respuesta:

```
「キビダンゴモ モッテイクガヨイ！」        <- la madre: SIN cantidad
モモタロウハ キビダンゴヲ ヒトツ テニイレタ！  <- el aviso: ヒトツ = "uno"
```

Las dos frases no dicen lo mismo: la madre usa un plural indefinido; el aviso especifica **uno**. Y el juego usa la misma plantilla para el dinero y para el dango, con la cantidad en el mismo sitio. Al final optamos por el singular en las dos: coincide con lo que el juego te da de verdad, y en castellano un contable pide artículo. Detalles así son los que hacen que una traducción se note trabajada o suene a máquina.

---

## Dos partidas guardadas: la historia del "uá"

Este capítulo es la continuación de aquel bloque negro que "resolvimos" alineándolo sobre las letras "uá". Y es, probablemente, mi historia favorita del proyecto.

Un día guardé una segunda partida. Tenía una en Normal y empecé otra en Fácil. Al entrar en la pantalla de carga, la segunda entrada aparecía **en la misma línea que la primera**, al final, separada por un hueco enorme y con el nombre cortado: sólo se leía "NOM". En la ROM japonesa original la pantalla funcionaba perfectamente; el fallo era nuestro.

El primer análisis apuntó a que ambas pantallas compartían un identificador interno y que nuestro parche se estaba aplicando donde no debía. Al comprobarlo contra una partida guardada real, el identificador **no coincidía**: hipótesis descartada. El segundo fue peor: se propuso revertir un cambio de la traducción que parecía sospechoso... que resultó ser **exactamente el arreglo del solapamiento de la pregunta**. Habríamos roto algo que llevaba semanas funcionando. Se libró por poco, y sólo porque insistí en repasar el diario del proyecto antes de tocar nada.

La respuesta estaba en cuánto espacio de memoria gráfica tiene reservado cada línea:

```
la pregunta      256 px de espacio
partida 1        128 px
partida 2        128 px
```

Al ensanchar, le habíamos dado **cinco piezas** (160 px) a la línea de la primera partida, pero esa línea sólo tiene 128 px asignados. La quinta pieza leía la zona siguiente... que es donde el juego escribe **la segunda partida**. O sea: el "NOM" cortado no era la segunda partida mal colocada, era la quinta pieza de la primera línea **mostrando el contenido de la segunda**. Al mirar esa zona de memoria apareció "NORMAL 1" entero y perfectamente escrito. La segunda partida nunca estuvo rota; simplemente la leía quien no debía.

Y aquí llegó lo bueno. Los sprites que habíamos escondido sobre las letras "uá" eran **exactamente esos invasores**: las piezas sobrantes de haber ensanchado las líneas de 3 a 5 sin comprobar cuánto espacio tenía cada una. Nunca fueron un "duplicado" que hubiera que ocultar; eran las líneas de las partidas 2, 3 y 4, leyendo memoria que no les correspondía. La chapuza de alinearlos sobre el "uá" los escondía, pero no los arreglaba. Y por eso el problema reapareció en cuanto guardé una segunda partida.

La solución definitiva fue devolver cada línea a sus cuatro piezas (128 px exactos, lo que tiene asignado). "MUY DIFÍCIL 1", el nombre más largo posible, mide unos 104 píxeles: cabe de sobra. La moraleja: aquella intuición de que "ese bloque no está donde debería" era correcta desde el primer día; lo que faltaba no era una idea mejor, sino **medir cuánto espacio tiene asignado cada línea** en vez de contar piezas a ojo. Y una cosa que me llevo de aquí: cuando algo "sobra", casi nunca sobra. Suele ser algo que se ha quedado sin sitio.

---

## El mapa y los nombres de las localizaciones

Con las pantallas de menú resueltas, tocaba entrar en el juego de verdad. Y el primer objetivo era el mapa: esa pantalla donde se ve el recorrido entre aldeas y aparece un cartelito con el nombre de cada una.

Lo primero fue localizar los nombres y traducirlos. Y ahí apareció algo bonito: **cada aldea es un cuento popular japonés**. Está la aldea de "la partida" (ponerse en camino), la de *Hanasaka Jiisan* (el que hace florecer los árboles), la de *Kintarō* (el niño forzudo), la de *Netarō* (el dormilón), la de *Urashima Tarō* (el de la tortuga), la de *Kachi-kachi Yama* (el monte crepitante), la de *Issun-bōshi* (el enanito), la de *Taketori* (el cortador de bambú) y *Onigashima*, la isla de los ogros.

Para traducirlos seguí un criterio mixto: **nombre propio** cuando el japonés nombra a un personaje (Kintaro, Urashima, Issunboshi) y **descriptivo** cuando nombra un lugar o un concepto (Partida, Florecer, Dormilón, Bambú, Ogros). Y mantener "Aldea" en las ocho que la llevan. Hay una pérdida consciente: **Kachiyama** se come uno de los dos "kachi" del original —*kachikachi* es la onomatopeya del chisporroteo del fuego, y el cuento va precisamente de eso—, pero "Aldea de Kachi-Kachi" se pasaba del límite por un carácter, así que hubo que elegir. Me fastidia, pero es lo que hay.

Al ir a insertar los nombres apareció un problema aparentemente serio: la tabla de caracteres del rótulo no tenía mayúsculas. Sin A, sin K, sin M; imposible escribir "Aldea de Kintaro". Se plantearon tres soluciones, todas laboriosas, y entonces hice la pregunta obvia, la del que no sabe nada de esto: *¿no podemos usar la fuente que ya tenemos, la de la intro y el password?* Resulta que **ya la estaba usando**. El rótulo no tiene fuente propia: lo que habíamos tomado por "una fuente sin mayúsculas" era en realidad una tabla intermedia, una especie de índice, y había una segunda vía de acceso que nadie había mirado, en la que las mayúsculas están donde uno esperaría que estuvieran. Esa pregunta ahorró una tarde entera de trabajo innecesario. A veces preguntar lo evidente sale rentable precisamente porque nadie se molesta en comprobarlo.

Con los nombres insertados, el rótulo del mapa seguía cortándose: sólo se leía "Aldea de". Pero al examinarlo apareció un detalle revelador: el contador interno decía **18 letras dibujadas**. El texto completo estaba en memoria; lo que faltaban eran piezas que lo mostrasen. Ensanchar el rótulo fue, con diferencia, lo más laborioso del capítulo: cinco versiones, cada una con su problema. La caja se fue 66 píxeles hacia abajo, fuera del mapa, porque la lista original la coloca con un truco de cálculo para situarla *por encima* del anclaje y al reescribirla con valores "limpios" se perdió. Después faltaban trozos de la caja y del icono vecino, por pasarnos del límite de dieciséis piezas por línea: al contarlas sólo se habían tenido en cuenta las del rótulo, y los iconos de las aldeas también ocupan. Y por último el rabillo no empalmaba con el marco, que resultó ser un problema de orden de dibujado.

Para que la caja ancha cupiera había que mover el rótulo de sitio en algunas aldeas. La tabla que da esas posiciones estaba localizada y parecía perfecta para el trabajo, pero antes de tocarla comprobamos quién más la usaba, y resultó que esa misma tabla **coloca también el icono de la aldea en el mapa**. Cambiar las posiciones habría movido las ocho aldeas de sitio, alterando la geografía del juego. La solución fue darle al rótulo su propia tabla de posiciones, dejando la original intacta, y dibujar el rabillo aparte, en la posición de siempre, para que siga apuntando a su aldea aunque la caja se haya desplazado. Esa idea, por cierto, salió de mirar la pantalla y pensar "bueno, si el rabillo ya apunta bien, dejadlo donde está y moved sólo el bocadillo".

Al probar la traducción noté algo raro: en el mapa el primer punto se llamaba "Aldea del Florecer", pero al entrar el rótulo decía "Aldea de la Partida". ¿Un pueblo dentro de otro? El análisis decía que el mapa leía la tabla desplazada una posición y la propuesta fue corregirlo. Menos mal que antes fui a comprobarlo, porque habría sido un error grave: en el segundo punto el mapa decía "Aldea de Kintaro" y dentro también, y en el tercero "Aldea del Dormilón" en los dos sitios, todo coherente. La explicación apareció avanzando en el primer nivel: **hay dos aldeas**; la primera es la natal de Momotaro, donde viven sus padres, y no tiene punto propio en el mapa. El desplazamiento no es un bug, es cómo el juego se la salta. Si lo hubiéramos "arreglado", habríamos roto la correspondencia entera. Segunda vez que una comprobación dentro del juego evita que se rompa algo que funcionaba.

---

## La caja que crece con el texto

Resuelto el rótulo, quedaba un detalle estético que me molestaba: la caja tiene un ancho fijo, pero los nombres no. "Isla Ogros" son diez letras dentro de un bocadillo pensado para veinte, con un hueco enorme a la derecha. El japonés no tiene ese problema porque sus nombres son todos de longitud parecida; el castellano es mucho más irregular.

En lugar de calcular el ancho sobre la marcha —que obligaría a rehacer la lista de piezas en cada fotograma—, se preparan varias cajas y se elige la que toca: 12 letras en una caja de 128 píxeles, 16 en una de 160 y 20 en una de 192. Una pequeña tabla dice qué ancho necesita cada nombre, sin cálculos por fotograma ni riesgo de que el juego vaya a tirones. Además, en el mapa el ancho condiciona **dónde** puede colocarse la caja: una de 128 píxeles cabe en sitios donde una de 192 se saldría de la pantalla, así que las posiciones se recalculan también según el ancho de cada nombre.

Y al mirar el original apareció algo que me hizo gracia: los japoneses **centraban el texto metiendo espacios** delante y detrás. Sin código, sin lógica, a mano. Exactamente lo que yo iba a proponer. Treinta y cinco años después, la solución sigue siendo la misma.

---

## La pieza grande: girar los bocadillos

Si tuviera que señalar el capítulo que más ha costado de todo el proyecto, sería éste. No por una dificultad concreta, sino porque cada solución destapaba tres problemas nuevos, y varios de ellos ni siquiera parecían tener relación con lo que estábamos tocando.

El japonés tradicional se escribe **de arriba abajo y de derecha a izquierda**, y así están montados todos los bocadillos: un cuadrado de seis por seis donde el texto empieza en la esquina superior derecha y baja. Para el castellano necesitábamos escritura horizontal y más ancho, porque nuestras palabras son mucho más largas. Era la pieza clave del proyecto: si todos los bocadillos comparten estructura, arreglado uno quedarían arreglados todos.

Y apareció algo que cambió el planteamiento por completo: el orden en que el juego coloca los caracteres **no está programado**, está en dos tablas que dicen, para cada una de las treinta y seis casillas, en qué punto de la memoria de vídeo va. Así que no había que reescribir la aritmética del motor: bastaba reordenar las tablas para que la casilla uno fuera la de arriba a la izquierda. **Setenta y dos bytes**, sin tocar el guion ni el código.

Antes de escribir nada se simuló un texto japonés conocido sobre las tablas permutadas, y menos mal: el primer modelo de la geometría estaba mal, porque había supuesto que cierto salto en memoria significaba "una casilla a la derecha" cuando era otra cosa. La simulación no daba líneas limpias y ahí se vio. Otra norma: *antes de permutar una tabla de posiciones, simular un texto conocido y comprobar que tiene sentido visual*. Con la corrección, el resultado fue exactamente el esperado:

```
ANTES (vertical)      DESPUÉS (horizontal)
|ナラドカボブ|         |ブキヤ    |
|ルクンッウキ|         |ボウグヲ   |
|ノチドテグヤ|         |カッテイケバ |
|ジンンイヲ |          |ドンドン   |
```

El texto salía horizontal y de izquierda a derecha. Yo respondí "buen trabajo" y pensé que lo más difícil estaba hecho. **Y entonces empezó lo bueno.**

Porque el texto ya era horizontal, sí, pero seguía metido en un bocadillo cuadrado pensado para el japonés. Había que girar el marco: hacerlo ancho y bajo, mover el rabillo que apunta al personaje, y ampliar el número de casillas por línea. El marco no es un dibujo: son doce sprites colocados uno junto a otro, más otro sprite suelto para el rabillo, que cambia de sitio según dónde esté el interlocutor. Rehacer esa lista para formar un marco apaisado fue el principio de una cadena de problemas que duró semanas.

Uno de mis primeros avisos: en el lado derecho faltaban cinco píxeles, en dos líneas concretas, justo donde el borde conecta con el lateral. La causa era una limitación de la consola que yo desconocía: el PC Engine sólo dibuja **dieciséis sprites por línea de barrido** y descarta el resto, siempre los últimos de la lista —en nuestro caso, el lateral y la esquina derechos—. Lo interesante es por qué la comprobación automática no lo vio: contaba los sprites por filas, y cada fila daba doce, dentro del límite. Pero miden dieciséis píxeles de alto y **las filas se solapan en sus bordes**: en la línea donde acaba una y empieza la siguiente se sumaban doce más doce, veinticuatro. El original no lo sufría porque su bocadillo era la mitad de ancho. El arreglo fue separar las tres filas. Norma: *las ranuras por línea de barrido se cuentan por línea, no por fila de la lista*.

Después vino una fase frustrante: el HUD se corrompía, el bocadillo no aparecía, el texto no se veía. Yo pasaba capturas del Sprite Viewer y volvíamos a intentarlo. El desatasco vino de una captura mía donde se leía "Size 32x16": se había asumido que esos sprites eran de dieciséis de ancho por treinta y dos de alto, y son justo al revés. Las consecuencias eran absurdas de tan simples: se colocaban sprites de treinta y dos píxeles cada dieciséis, así que cada uno tapaba la mitad del anterior y sólo se veía media letra, y la tabla que repartía las casillas estaba girada noventa grados, porque suponía que la siguiente estaba debajo cuando estaba al lado. De paso apareció un error de programación oculto todo ese tiempo: una rutina cargaba un valor en un registro y dos instrucciones después lo machacaba antes de usarlo, de modo que las dos primeras líneas escribían todas en el mismo sitio. Quedó apuntado tal cual en el diario, porque es justo: tres versiones fallando por no haber leído el formato con calma, y el dato estaba a un Sprite Viewer de distancia.

Y llegamos al problema que más quebraderos de cabeza ha dado, porque tardamos mucho en entender siquiera qué estábamos buscando. Al girar el bocadillo desapareció **la flechita que indica que puedes avanzar el texto** —esa que parpadea cuando el diálogo espera a que pulses— y, con ella, el **cursor del SÍ y el NO** que sale cuando la estatua de Jizo te pregunta si quieres oír la contraseña. Lo lógico era buscarlas en la lista de sprites del bocadillo y recolocarlas con el resto. No estaban. Se recolocaron los registros de la lista una y otra vez y las flechas no se movían ni un píxel.

Aquí hubo varios tropiezos documentados como errores propios, y uno me gusta especialmente por lo instructivo. En un momento dado se dio por hecho que cierta casilla del marco contenía la flecha, basándose en una captura mía del Sprite Viewer. Se tocó, y salieron artefactos justo ahí; se dio la causa por confirmada y se revertió. Pero era falso: al pintar esa casilla entera y mirarla en lugar de deducirla, resultaron ser píxeles sueltos sin forma, basura gráfica en la mitad no usada. El sprite que yo había capturado era el borde del marco, que en pantalla queda **cerca** de la flecha. Se había confundido proximidad con identidad.

La explicación real la dimos entre los dos, y es curiosa. Yo pasé capturas del visor de memoria con los dos estados del parpadeo, y comparándolas apareció el dibujo:

```
FE 7C 38 10   ->   #######.   flecha de continuar
                    .#####..   (triángulo hacia abajo)
                    ..###...
                    ...#....

1F 0E 04      ->   ...#####   cursor del SÍ/NO
                    ....###.   (triángulo hacia la derecha)
                    .....#..
```

Las dos flechas **no son sprites**: el juego las escribe directamente en la memoria de vídeo, como escribe las letras, dentro de una casilla del propio marco. Y aquí está lo bueno: **ninguna lista de sprites incluye esas casillas**. Se escriben, pero no hay nada que las muestre. O sea que no las habíamos roto nosotros —comprobado que esa rutina está intacta, byte por byte, desde mucho antes—; lo que pasaba es que el marco nuevo ya no coincidía con el sitio donde el juego las pinta a ciegas.

Y de paso apareció otro dato que resolvió una confusión de semanas: las dos casillas donde aparecen esas flechas están separadas por exactamente ocho posiciones, que es el mismo desplazamiento que usa el juego para alternar entre sus dos búferes de pantalla. **No son dos flechas distintas: es la misma, en las dos páginas.** Es una constante de este proyecto: cada cosa que parpadea o se mueve tiene su propio mecanismo, ninguno aparece en las listas donde uno esperaría, y ninguno se entera de que los demás han cambiado de sitio.

Este capítulo explica mejor que ninguno por qué un proyecto así lleva meses y no días. La conversión en sí eran setenta y dos bytes de tabla; todo lo demás —el marco, el rabillo, los sprites mutilados, el HUD corrupto, las flechas huérfanas— fueron consecuencias en cadena de tocar algo que el juego daba por inmutable desde 1990. Y es donde más claro se ve el reparto de tareas: yo no puedo leer una rutina, pero sí abrir el Sprite Viewer, hacer una captura y decir "aquí pone 32x16". Tres versiones de bloqueo se resolvieron con eso.

---

## La letra que no existía

Antes de contar las historias grandes de esta tanda quiero empezar por la más pequeña, porque resume bastante bien cómo funcionan estas cosas.

Teníamos un objeto en el inventario llamado "Capa". Cinco letras, nada del otro mundo. Pues bien: la **p** no aparecía; en su lugar salía un carácter japonés suelto, en mitad de la palabra, como si el juego se hubiera acordado de golpe de dónde venía. Lo curioso es que ese mismo problema llevaba tres versiones bloqueando el trabajo. Se habían probado dos códigos distintos para la **p** y ninguno funcionaba: uno daba un símbolo raro, el otro daba otro símbolo raro. Parecía que esa letra sencillamente no existía en el juego.

La explicación resultó ser que el juego no traduce un carácter en un paso, sino en tres, y nosotros sólo conocíamos el último: una tabla de sustitución previa cambia ciertos códigos por otros; una rutina decide, según el valor, cuál de las dos tablas de glifos usar; y sólo entonces se busca el dibujo de la letra. Esa primera tabla es la que lo estropeaba todo. Está guardada como dos listas paralelas —una con los códigos de entrada y otra, unos bytes más allá, con los de salida—, de modo que si la lees seguida, como si fueran parejas, sale ruido. Y precisamente por eso se había descartado tiempo atrás: parecía basura. Reconstruida la cadena completa, la respuesta apareció sola: la **p** es el código $5E, y sólo ése; los otros dos que se habían probado entraban por la ruta equivocada y acababan en dibujos que no tenían nada que ver.

Y de paso apareció una trampa que nos ha ahorrado disgustos después. Al final del nombre había un espacio de relleno, y el espacio, al pasar por esa cadena de tres pasos, acaba apuntando al dibujo número cero de la fuente. El dibujo número cero no está en blanco: es un cuadrado negro. Así que rellenar un nombre corto con espacios para que ocupe todo el hueco, que es lo natural, deja una hilera de bloques negros en el menú. La solución era simplemente no rellenar. Dos bytes cambiados en total. Tres versiones de bloqueo.

---

## El canto de Jizo y la página que no se borraba

En el juego hay una estatua de Jizo que te canta la contraseña de la partida. Te pregunta si quieres escucharla y, si dices que sí, te la recita.

En la traducción quedaba fatal. La pregunta se quedaba arriba, ocupando dos líneas, y la contraseña aparecía debajo a trozos: primero dos líneas, y al avanzar, la tercera sola en una página nueva. Todo revuelto. Yo lo veía clarísimo: la contraseña son tres líneas y el bocadillo tiene cuatro, caben de sobra en una página limpia. Me habían contado que no se podía, y no me lo creía.

Resulta que el bocadillo tiene cuatro filas de texto pero el juego sólo guarda treinta y dos casillas, que dan para dos. Hay una variable que decide qué mitad se está pintando: si vale 1 ó 2, las líneas de arriba; si vale 3, 4 ó 0, las de abajo. Ahí estaba el problema: al entrar al canto, esa variable conservaba el valor que había dejado la pregunta, así que se borraba la mitad equivocada. Para limpiar la página entera hay que volcar el buffer vacío **dos veces**, una por cada mitad.

Eso funcionó a la primera. Y aquí cometí un error del que aprendí bastante: cuando probé la versión y dije "mejor, pero aún no", en realidad estaba describiendo un problema de colocación, no un fallo. Ese cambio ya era bueno. En vez de dejarlo cerrado y ajustar encima, se encadenó un segundo cambio sin haber cerrado el primero, y acabamos con una versión que se colgaba y no sabíamos por cuál de los dos. Ahora es norma: si digo "mejor pero aún no", lo anterior se conserva.

La siguiente versión no arreglaba nada: el bocadillo se quedaba en blanco y el juego se congelaba. Eso sí, la música seguía sonando tan tranquila. Ese detalle, que parecía anecdótico, resultó ser la pista: si el juego se hubiera estrellado de verdad, el sonido se habría ido con él; que la música siguiera significaba que las interrupciones seguían corriendo y que el juego estaba, sencillamente, dando vueltas en un bucle sin salida. Y lo era: el bucle que borra las dos mitades restaba de dos en dos y comprobaba si había llegado al final... con la instrucción equivocada. Una comparación que en ese procesador se hace sin signo, de modo que cuando el contador pasaba de 1 a 255 en lugar de a -1, la condición de salida no se cumplía jamás. Vueltas infinitas, cada una borrando la pantalla otra vez.

Lo interesante no es el error, sino por qué no se detectó. El programa que genera la ROM lleva comprobaciones automáticas, y una de ellas simulaba ese bucle para verificar que terminaba. Dio el visto bueno, ¿por qué? Porque el simulador estaba escrito con el mismo malentendido: trataba la comparación como si fuera con signo. Estaba comprobando el código contra una idea equivocada de cómo funciona el procesador, no contra el procesador. De ahí salió una de las normas que más me gustan de todo el proyecto: *una comprobación que valida tu hipótesis en vez del hardware no vale absolutamente nada*.

El arreglo final fue **un byte**: cambiar el tipo de salto para que mirase el signo del resultado. Y con eso la contraseña salió por fin donde tenía que salir: tres líneas, página propia, empezando arriba.

---

## El menú RUN: buscar durante horas en el banco equivocado

Ésta es, con diferencia, la historia más larga de la tanda, y también de la que más he aprendido.

Al pulsar RUN se abre el menú de acciones del juego: los objetos que llevas, lo que puedes hacer con ellos y los compañeros que te acompañan. Todo seguía en japonés. La primera medición fue desalentadora: cada palabra tenía un hueco justísimo, los verbos en infinitivo no cabían por una o dos letras, y no parecía haber ninguna tabla que permitiera moverlos de sitio. La conclusión que se apuntó en el diario fue que esas palabras estaban clavadas donde estaban.

**Era falso.** Sí había tabla de punteros; estaba a la vista, y además venía en el juego original. El fallo fue de método, y es de los que enseñan. Se había buscado la tabla de una manera concreta —rastreando instrucciones que leyeran una lista con un índice— y, como no aparecía ninguna, se dio por hecho que no existía. Pero el motor de textos de este juego no funciona así: recibe la dirección **como parte del propio guion**, no la busca en una lista. Se estaba buscando la huella equivocada, y la ausencia de esa huella se tomó como ausencia del hecho.

Cuando se comprobó bien, la prueba fue casi divertida: en una de esas tablas hay dos entradas que apuntan al mismo sitio. Una palabra no puede estar físicamente en dos lugares a la vez; un puntero sí puede repetirse. Con eso quedaba demostrado.

Con las tablas localizadas ya se podían mover las palabras a cualquier hueco libre. Y aquí me llevé otra lección, aunque esta vez el error se cazó antes de escribir nada. Se contaron los huecos disponibles: 69 bytes. Se contó lo que hacía falta: 66. Cabía. Pues no cabía: los huecos estaban repartidos en trozos pequeños y las palabras no se pueden partir por la mitad, y al probar todas las combinaciones posibles resultó que no existía ninguna forma de encajarlas. *Sumar el espacio libre no demuestra nada si no compruebas cómo está repartido.* Y hubo un tercer susto, éste sí a punto de romper algo: uno de los bloques donde se iban a escribir las palabras tenía **la propia tabla de punteros metida en medio**. Parecía un hueco continuo y eran dos trozos separados. La comprobación automática lo pilló porque, después de escribir, vuelve a leer cada palabra siguiendo su puntero, igual que hace el juego: donde tenía que poner "Usar" leyó un galimatías.

Y después de todo eso, no se veía nada. Sacamos la versión, la probé... y el menú seguía exactamente igual. Ni una palabra traducida. Lo que había pasado es de manual: se habían encontrado unas palabras japonesas que encajaban con lo que buscábamos, y se dieron por buenas sin comprobar que fueran las que aparecen en pantalla. Eran otras —frases de diálogo parecidas, en otra parte de la ROM—. Las de verdad estaban en otro sitio completamente distinto.

Para localizarlas me pidieron colocar un punto de ruptura en una dirección concreta. Lo puse, no saltó. Lo volví a poner con más margen, tampoco. Y ahí estaba la clave, aunque no lo pareciera: la dirección estaba mal calculada. Estas consolas no tienen toda la ROM accesible a la vez —van asomando trozos por ventanas—, y el mismo dato tiene una dirección distinta según por qué ventana asome. Se había supuesto por qué ventana asomaba ese trozo, en vez de comprobarlo, cuando teníamos delante desde hacía horas otro trozo vecino que lo dejaba claro. Lo grave es que ese mismo error se había cometido ya tres veces en esta tanda, cada vez con una consecuencia distinta: un punto de ruptura que nunca saltaba, un hueco de memoria dado por bueno cuando no servía, y unos punteros que parecían corruptos y estaban perfectos. Los tres síntomas eran distintos y la causa la misma.

Con la ventana correcta, todo apareció de golpe: las tablas, las palabras, y también **los tres mensajes de error** que llevábamos buscando desde el principio, incluido el de "no se puede comer", que estaba dado por perdido. Y un detalle bonito: tres de esas frases no usan tabla, el juego arma la dirección a mano, partida en dos instrucciones seguidas —un puntero igual, sólo que escrito de otra manera—, y dos de esos mensajes decían lo mismo, así que ahora apuntan los dos a un único texto en español: tres punteros, una frase, veintiséis bytes ahorrados.

---

## Ocho celdas y ni una más

Con el menú por fin traducido, probé, y esto es lo que salió:

```
"No se come"   ->  se veía  "No se co"
"No se puede"  ->  se veía  "No se pu"
```

Ocho letras exactas en ambos casos. Las palabras cortas salían enteras; todo lo que pasaba de ocho, cortado. Lo primero fue mirar si ese límite se podía tocar, y la respuesta fue que no: el bucle que dibuja esos bocadillos no lleva ningún contador, escribe hasta que se acaba la frase. El corte no es del programa, es del marco: **el bocadillo mide ocho casillas** y lo que sobra se pinta literalmente fuera de la caja. Así que no había nada que arreglar; había que escribir en ocho.

Aquí el trabajo deja de ser técnico y pasa a ser de traducción pura, que muchas veces es lo más difícil. Para "Poderes" la solución vino de una captura mía: en el menú SELECT el mismo concepto ya estaba traducido como **Artes** desde hacía tiempo, y no tenía sentido usar dos palabras para lo mismo, así que "Artes" por coherencia. Cinco letras, y resuelve un problema que ni sabíamos que teníamos. Para el "no se puede usar" dimos vueltas: "Inútil" cabía, pero describe el objeto en lugar de la acción y en un menú de acciones chirría. Al final, **No puedo**, ocho letras justas. Y para el "no se puede comer", el más difícil, acabamos en **¡Puaj!**: una adaptación libre, pero transmite lo mismo, encaja con el tono del juego y cabe con los dos signos incluidos, que para mí importaba —los nombres de objeto no llevan puntuación, pero una interjección sin cerrar queda coja—. "Qué asco" habría cabido justo, sin sitio para los signos.

Y hubo un hallazgo por accidente. Probando el menú me encontré con algo que pensé que era un fallo nuestro: si coges el Dango, que es comida, y en vez de comértelo le das a "Usar", aparece la opción "Perro". Antes de dar la voz de alarma tiré de la ROM japonesa original para comparar, y allí está, exactamente igual: sale "Inu", perro. No es un error de la traducción, es una rareza del juego original, medio escondida detrás de una combinación que a nadie se le ocurriría probar. Me hizo gracia porque es justo lo contrario de lo que suele pasar: normalmente descubres tus propios fallos comparando con el original; esta vez el original me dio la razón. Eso sí, me deja una tarea por delante: varios de estos mensajes sólo aparecen haciendo cosas que no tienen sentido, y para verlos todos hay que ir probando combinaciones absurdas a propósito, algo que sólo se puede hacer jugando.

---

## Los once objetos que no eran los que decían

Este capítulo es corto pero me hace ilusión, porque es un caso en que la observación humana ganó a la deducción técnica por goleada.

En el menú que sale al pulsar SELECT aparece el inventario: once objetos con sus nombres. Un día, jugando, me di cuenta de que algo no cuadraba: cogía un objeto concreto y el nombre que salía no era el suyo, sino el de otro. Lo dije, y el análisis inicial fue que probablemente me estaba equivocando yo. El razonamiento era sensato: el juego no localiza los nombres por su posición física en la ROM, sino a través de una tabla de punteros, así que una lectura hecha "a ojo" sobre el orden de los datos no demuestra nada; muy probablemente los nombres estaban bien y lo que fallaba era la forma de leerlos.

Se siguió la cadena entera de punteros para comprobarlo, y resultó ser una tabla de dos niveles: cada entrada apunta a una sublista, y el primer puntero de esa sublista es el que da la cadena. Bastante más enrevesado de lo que parecía. El resultado fue que ambos métodos daban **exactamente el mismo emparejamiento**: la lectura era correcta, y los nombres estaban mal asignados de verdad.

```
kibidango (dango)   ->  decía "Onigiri"
hyouga    (glaciar) ->  decía "Remedio"
nichirin  (solar)   ->  decía "Banquete"
kakuremino (capa)   ->  decía "Caña"
onara     (pedos)   ->  decía "Aletas"
```

Diez de los once cruzados. Era un destrozo heredado de alguna versión antigua en la que se reubicaron cadenas sin actualizar las referencias, y llevaba ahí sabe Dios cuánto. Lo que me gusta de este episodio es lo que quedó escrito en el diario: la inclinación inicial era la equivocada, pero **no se escribió nada hasta comprobarlo**. Lo cómodo habría sido dar el asunto por cerrado. Todos los nombres están ya en su sitio.

---

## El guion completo: aldeanos, tiendas y ermitaño

Una vez que los bocadillos apaisados funcionaban de verdad, llegó el momento que todo lo anterior había estado preparando: traducir el grueso del guion. Aquí el reto ya no era inventar la rueda, sino aplicar a escala lo aprendido, y fue en esta fase donde el proyecto dejó de ser un conjunto de pantallas sueltas para convertirse en la traducción de un juego entero.

El guion estaba repartido en dos sistemas distintos que hubo que abarcar por completo. Por un lado, los diálogos principales del juego, almacenados de forma comprimida en la ROM con su propio diccionario y sus punteros; por otro, los textos de los bocadillos verticales —los de los aldeanos, las tiendas y el ermitaño—, cada uno con su maquetación en columnas. Traducir el conjunto supuso adaptar más de un centenar de textos, todos con la misma regla de oro: el castellano ocupa más que el japonés, y cada frase había que repartirla en el bocadillo de 20 celdas sin cortar palabras.

Los aldeanos de las nueve aldeas fueron un trabajo de traducción pura, con sus particularidades: cada uno tiene una personalidad, un dialecto de registro y, a menudo, dos versiones del mismo diálogo según si ya has derrotado o no a los ogros de su zona. Las tiendas añadieron su propia capa de dificultad, porque a los nombres y descripciones de los objetos se sumaba el texto de las despedidas y los avisos, todo encajado en cajas de tamaño fijo. Y el ermitaño, que vive en lo alto y enseña las artes, traía además el quiz de cuarenta preguntas con sus ciento veinte opciones de respuesta y la lista de las catorce técnicas que te va regalando — nombres como «Vuelo», «Salto», «Rodar», «Giro» o «Paropunte», cada uno con su hueco justísimo —.

Fue en esta fase donde se hizo más evidente una de las trampas recurrentes del proyecto: los textos japoneses que aún no habíamos traducido se pintaban con la fuente latina y aparecían como ristras de símbolos raros. Más de una vez creímos haber roto algo cuando en realidad sólo estábamos viendo kana dibujado con las letras equivocadas. A medida que el guion se completaba, esos "artefactos" iban desapareciendo solos, porque nunca fueron otra cosa que texto pendiente de traducir.

También fue aquí donde volvió a quedar clara la diferencia entre "funciona sobre el papel" y "funciona en pantalla". Con el guion entero traducido, hice una pasada completa jugando —todas las aldeas, todas las tiendas, los minijuegos, el quiz, el jefe final, los cuatro finales y las dos pantallas secretas— y de esa pasada salieron una tanda de detalles que jamás habrían aparecido leyendo la ROM: una «Ç» flotando sobre la posada de 1000 ryos (un resto de un *dakuten* japonés mal borrado), una despedida de tienda con colas de kana sueltas, una pregunta del quiz que no se entendía, el arte «Parapunte» mal escrito... Pequeñeces que, una a una, se fueron cazando y cerrando.

---

## Los minijuegos

Los minijuegos trajeron sus propios problemas, y alguno bastante divertido. En el de piedra, papel o tijera contra el ermitaño, la presentación salía con signos latinos corruptos, y el diagnóstico inicial era que se trataba de un gráfico que había que redibujar. No era un gráfico: era texto en claro por la ruta katakana, que se veía mal porque el latino ocupaba el espacio del kana. Bastó con traducirlo y maquetarlo para que saliera «¡Piedra, papel o tijeras!» y «¡Iguales!» completos.

En el de dados, al perder salía «¡Hasta la vist» —sin la «a» final y desplazado a la derecha—, y la causa era tan tonta como traicionera: entre dos frases había cinco espacios en vez de tres, y los dos de sobra empujaban la segunda línea fuera de la caja de 16 columnas. Quitar dos espacios, y listo.

Y en los minijuegos donde se maneja a Momotaro —el tutorial de esquivar los ñordos que caen y su variante oculta— apareció un bug especialmente escurridizo que merece párrafo aparte, porque resume muy bien cómo se cazan estas cosas. Después de mostrarse toda la explicación, quedaba un **carácter raro suelto** al final del bocadillo, y sólo en el minijuego oculto, no en el tutorial. Tras descartar que el texto estuviera en el guion comprimido (no estaba; vive en su propio bloque, como la intro y el tutorial), la comparación entre las dos variantes reveló el fallo exacto: la frase de cierre del minijuego oculto terminaba con dos bytes de control de "espera" pero le **faltaba el byte de fin de texto**, así que el motor seguía leyendo más allá y dibujaba el primer byte del bloque siguiente como un glifo suelto. Un byte cambiado, y el carácter fantasma desapareció.

---

## Los finales y los créditos

Los cuatro finales —Muy difícil, Difícil, Normal y Fácil— fueron de lo último en traducirse, y tuvieron que rehacerse desde cero: un primer intento quedó tan mal, con palabras partidas y nombres cortados, que David decidió anularlo y volver a empezar sobre la base limpia. La regla que lo salvó todo fue la del formato acordado: *nunca partir una palabra* —si no cabe, la palabra entera baja de línea—, la presentación de los enemigos con la frase en su línea y el nombre en la suya, y el staff en orden occidental, con la inicial cuando el nombre no cabe: «M. Kuya», «H. Iizuka». Cargos en mayúsculas, nombres sin punto final, frases sí.

Los créditos añadieron su propia dificultad, porque mezclan dos sistemas: una parte del texto vive en un bloque normal y otra en un bloque distinto con su propia maquetación, y el famoso «HUDSON SOFT» del final hubo que respetarlo tal cual. El «medetashi medetashi» del bocadillo de cierre —el "colorín colorado" japonés— y el cartel de «Banzai! Studio» de las secuencias quedaron localizados y adaptados, y los rótulos de las pantallas secretas (la «SALA DE SONIDO» y la «GALERÍA DE ARTE») se centraron y tradujeron por completo.

Mención aparte merecen los vítores que salen al superar cada fase, con los cerezos en flor de fondo. Sobre cada árbol aparecía el mismo cuadrado de artefactos, y el arreglo fue de los más delicados del proyecto: resultó que el cargador que pinta los cerezos barre más tiles de los que habíamos movido, de modo que una parte leía datos de la traducción como si fueran gráficos. Reordenar los índices dejó la pantalla **por debajo del propio original japonés en píxeles con fallo**, que es un buen marcador de cuándo algo queda de verdad cerrado.

---

## La firma de la pantalla de título

Y así llegamos al único fleco que queda abierto a día de hoy, y que me hace especial ilusión porque es, literalmente, el último.

Debajo del «©1990 HUDSON SOFT» de la pantalla de título queremos colocar una firma del equipo —un pequeño rótulo «TRADUCIDO» sobre las olas—, y resulta que las olas se dibujan por encima y lo tapan a medias. Lo que parecía un simple "poner un sprite ahí" se ha convertido en el enésimo problema de orden de dibujado de este proyecto: hay que insertar la firma en el punto exacto de la secuencia de la pantalla de título para que quede **por encima de las olas**, y los dos intentos que llevamos han fallado —uno la colocaba en el sitio equivocado, en la transición del mapa en lugar del título, y el otro corrompía la pantalla entera—.

Es la guinda perfecta, porque es un problema puramente estético, minúsculo comparado con todo lo anterior, y aun así se resiste. No cambia nada de lo jugable; es sólo el detalle de que la firma se vea limpia. Cuando caiga, caerá el último byte del proyecto.

---

## Cómo trabajamos: el diario y las normas

Este capítulo no va del juego, sino del método, y creo que es de las cosas más útiles que puedo compartir, porque ha cambiado por completo el ritmo del proyecto.

Todo lo que se investiga se apunta en un diario de trabajo. Ya van más de ciento sesenta entradas y unas quince mil líneas. Pero lo importante no es lo que se escribe cuando algo sale bien, sino lo que se escribe cuando sale mal:

> **Las hipótesis falsas no se borran.** Se marcan como descartadas, con el motivo.

Suena a burocracia y es exactamente lo contrario. Media docena de veces hemos estado a punto de repetir un error ya cometido, y el diario lo ha impedido. En una ocasión, un análisis proponía revertir un cambio que resultó ser el arreglo de un bug anterior: leer el diario evitó el desastre.

Cada vez que un error nos cuesta tiempo, se convierte en una norma. Ya pasan de doscientas treinta. Algunas son específicas de este juego, otras valen para cualquier proyecto:

- *Medir contra la pantalla, no contra la teoría.*
- *Una corrección también hay que medirla.*
- *Lo medido en una fuente no vale para la otra.*
- *Antes de dar por libre un hueco de memoria, comprobar qué hay dentro.*
- *Antes de dar por libre una dirección, comprobar quién la llama.*
- *Antes de parchear una ruta, comprobar que está viva.*
- *Un cambio debe ser seguro por construcción, no por comprobación.*
- *"Afecta a todo el juego" hay que contarlo, no suponerlo.*
- *Un sprite que "sobra" no sobra: es algo que se ha quedado sin sitio.*
- *Antes de inventar una variable, comprobar si el dato ya está a mano.*
- *Antes de dar una dirección, comprobar por qué ventana asoma ese trozo de ROM.*
- *Sumar el espacio libre no demuestra que quepa: hay que comprobar el reparto.*
- *Una comprobación que valida tu hipótesis en vez del hardware no vale nada.*
- *Que un texto encaje con lo que buscas no demuestra que sea el que sale en pantalla.*
- *Si el usuario dice "mejor, pero aún no", lo anterior es bueno: se conserva.*

Todas nacieron de errores reales. Varios de ellos están contados en este mismo diario.

Ninguna ROM se sobrescribe: cada versión se numera, se registra su firma y se anota qué bytes exactos cambian respecto a la anterior. Eso permite dos cosas muy valiosas: volver atrás sin miedo, y hacer bisección —si algo se rompe, se prueban las versiones intermedias hasta dar con la que introdujo el fallo—. Y la lección más útil de todas: no basta con que el programa que genera la ROM haga lo correcto, tiene que **comprobar** que lo ha hecho. Cada constructor incluye comprobaciones automáticas que verifican que el byte que se va a sustituir es el esperado, que el hueco donde se escribe está realmente vacío, que ninguna pieza se sale de la pantalla, que ninguna línea supera el límite y que las zonas que no debían tocarse siguen idénticas. Esas comprobaciones han cazado, sólo en la última fase, un salto que provocaba un bucle infinito, un parche escrito en una rutina que nadie ejecutaba, un cálculo mal hecho que leía fuera de una tabla, un bloque de datos a punto de escribirse encima del final de otro y una palabra que iba a caer justo encima de una tabla de punteros escondida en mitad del hueco. La más útil de todas es la más tonta: después de escribir cada palabra, volver a leerla **siguiendo su puntero**, igual que hace el juego, y comprobar que dice lo que tiene que decir.

Si algo he aprendido es que esto no funciona como mucha gente imagina. No es pedir "tradúceme el juego" y esperar: es una conversación larguísima en la que uno aporta conocimiento técnico y el otro contexto, criterio, ojos y muchas horas de emulador. También he aprendido a discutir: cuando algo no me cuadra lo digo, aunque no sepa por qué, y varias veces he tenido razón, no porque supiera más, sino porque yo miraba la pantalla mientras el análisis miraba el código. Al revés pasa igual de a menudo: suelto una teoría con toda mi convicción y una medición de treinta segundos la desmonta. Ese ir y venir es lo más interesante del proyecto.

---

## Los passwords del juego

Como comentaba en el capítulo de la parrilla, el juego trae una serie de passwords secretos que siguen funcionando tecleados en la parrilla latina. Los dejo aquí, en un desplegable, para quien no quiera verlos.

<details>
<summary>Ver los passwords secretos</summary>

- **Final Muy difícil:** `IJUOYIHSATUSAM`
- **Final Difícil:** `IKUYAKATIOT`
- **Final Normal:** `OKIHCIMATIHSOY`
- **Final Fácil:** `AMUKASARIKA`
- **Sound Test (SALA DE SONIDO):** `IWASAKICANTAMAL`
- **Graphics Test (GALERÍA DE ARTE):** `IWASAKIDIBUJAMAL`
- **Minijuego oculto (PIEDRA, PAPEL o TIJERA):** `PIEDRAPAPELTIJERA`
- **Intro del título:** `MOMOTAROERAFUERTE`

</details>

---

## Estado actual y cierre

A día de hoy el proyecto está, salvo por la firma, terminado. Han sido **un mes y una semana** de trabajo, unas doscientas versiones numeradas, un guion completo traducido y una lista de normas que ya supera las doscientas treinta. Y si tuviera que quedarme con una sola idea de todo el proceso, sería ésta:

> **Una IA no sustituye el proceso de investigación. Forma parte de él.**

Yo no sé romhacking. Lo que sé es qué quiero conseguir, mirar con atención, jugar mil veces la misma pantalla y decir "esto no está bien". El trabajo técnico, que es la parte durísima, lo hace la IA, y sin ella este proyecto no existiría. Pero mi parte tampoco sobra: preguntar lo obvio a veces destapa el atajo, una corazonada delante de la pantalla puede ahorrar días, y alguien tiene que jugar, mirar y decidir. Nos hemos equivocado los dos, bastantes veces, y casi siempre nos hemos corregido el uno al otro.

Creo que formamos un buen equipo. Y lo mejor es que hace un año esto habría sido sencillamente imposible.

Gracias por leer. Y, cuando salga la traducción, espero que la disfrutes con la misma ilusión con la que la hemos construido.
