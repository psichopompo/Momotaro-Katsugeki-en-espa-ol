#!/usr/bin/env python3
"""
traduccion.py - el guion de Momotaro Katsugeki en castellano.

REGLA DE ORO: aqui se guarda el texto en PROSA NORMAL, sin cortar.
El reparto en lineas lo hace la maquina (`repartir`) segun el ancho que
acabemos eligiendo. Asi, si cambiamos de 20 a 22 caracteres, no hay que
retocar ni una frase, y no se reparticiona a mano el texto que apruebe
David (norma 38).

Criterios seguidos
------------------
* Los puntos suspensivos se escriben con TRES PUNTOS normales.
  MEDIDO: el codigo $CF NO son puntos suspensivos, son DOS PUNTOS (el
  bitmap del glifo 207 tiene dos cuadrados, uno arriba y otro abajo), y
  ademas el juego japones lo usa 228 veces, asi que no se puede repuntar.
  El $3D del original es el punto centrado japones, cuyo glifo (165) fue
  pisado por el chat original. Coste de usar "...": +248 B y +3 paginas.
* Los nombres de objetos coinciden con los ya aprobados para el menu
  SELECT: Raquetas, Aletas, Fuego, Hielo, Capa, Dango, Onigiri...
* Registro: los ancianos y el ermitano hablan con giros mas arcaicos,
  los ninos con frases cortas. El original marca esas diferencias con
  dialectos rurales (ダ/ジャ/ゴワス) que en castellano no tienen
  equivalente directo.
* Fidelidad al japones, no a la traduccion inglesa (que no se ha usado).

MARCADAS CON # (?) las decisiones que conviene que David confirme.
"""

ANCHO = 20
LINEAS = 4

TEXTOS = {
 # ---------------------------------------------- Aldea de la Partida
 0: ["¡Momotaro! Si pulsas el botón II podrás atacar a los ogros..."],
 1: ["Si compras armas y armaduras, todo se te hará mucho más fácil..."],
 2: ["Para entrar en una tienda, pulsa la cruceta hacia arriba en la entrada."],
 3: ["Cuando les des su merecido a los ogros... ¡compra armas, compra armaduras, compra objetos! ¡Wahaha...!"],
 4: ["Si quieres ver lo fuerte que eres, pulsa el botón SELECT."],
 5: ["El ermitaño vive en lo alto... Deberías pedirle que te enseñe sus artes."],
 6: ["Si pulsas el botón RUN podrás usar artes y objetos... Claro que, si no tienes ninguno, no podrás usar nada..."],
 7: ["Salta con el botón I y ataca con el botón II... Yo mismo derroté a 1000 ogros de esta manera..."],
 8: ["Haz florecer los cerezos, por favor... ¡Te lo suplico!"],
 9: ["Oh... Qué hermosos están los cerezos... La aldea vuelve a florecer... Muchísimas gracias."],
10: ["Buaaa... Los ogros marchitaron los cerezos de esta aldea. ¡Con lo bonita que era! Buaaa..."],
11: ["Vaya... Qué perro tan fuerte... ¿Sabías que los perros de ahora lanzan bombas de mano?"],
12: ["A los ogros que giran sin parar no puedes vencerlos mientras dan vueltas..."],
13: ["Me he enterado hace poco de que el anciano de los cerezos ha abierto una tienda de objetos para ayudar a Momotaro..."],
14: ["Que quede entre nosotros... El punto débil del jefe es la diana que lleva en el cuerpo. Que quede entre nosotros... ¡No se lo cuentes a nadie!"],
15: ["Dicen que los cerezos son preciosos, pero en esta aldea florecieron antes de que yo naciera..."],
16: ["¿Así que estos son los cerezos...? Qué bonitos son... Al mirar estas flores el corazón se llena de alegría..."],
17: ["¿En esta aldea han vuelto a florecer los cerezos?"],
18: ["Ce-re-zos, ce-re-zos... Muchísimas gracias. Parece que la aldea ha recuperado la alegría de antaño... De verdad, gracias..."],

 # ---------------------------------------------- Aldea de Kintaro
19: ["Ésta es la aldea de Kintaro, al pie del monte Ashigara..."],
20: ["Por culpa de los caramelos Kintaro gigantes que caen del monte Ashigara no se pueden cosechar los cultivos... Tampoco se puede andar por fuera... ¡Esto es llover sobre mojado!"],
21: ["¿Has acabado con los ogros...? Gracias a ti esta aldea ha vuelto a vivir en paz como antaño... De verdad, muchas gracias..."],
22: ["¿Caramelos de Kintaro...? ¿Nadie quiere caramelos...? Buaaa... Con tanto caramelo tirado por ahí, mi negocio se ha ido a pique."],
23: ["¡Caramelos de Kintaro! ¡Caramelos de Kintaro! Ja, ja, ja... Gracias a que acabaste con los ogros, mi negocio va viento en popa..."],
24: ["Dicen que los ogros han puesto muchas escaleras en el monte Ashigara y arrojan cosas a los viajeros que intentan subir a la cima..."],
25: ["¿Dices que has acabado con los ogros...? Ay, de verdad, cuánto te lo agradezco..."],
26: ["En esta aldea vivimos de fabricar caramelos Kintaro."],
27: ["Para conmemorar vuestra hazaña, todos los vecinos hemos decidido fabricar a partir de ahora caramelos Momotaro..."],
28: ["Poder comer caramelos a montones está muy bien, pero papá y mamá lloran porque no hay negocio..."],
29: ["Oye, oye... ¿Sabías que con el faisán puedes volar libre por el cielo?"],
30: ["Con el guijarro de fuego no hay que temer a los ogros de por aquí."],   # (?) el menu lo llama «Fuego»
31: ["¿Vaya? ¿Llevas contigo al mono? Dicen que los monos siempre han sido buenos imitando... ¿Qué tal se le dará a ése?"],

 # ---------------------------------------------- Aldea de Netaro (nieve)
32: ["Ésta es la aldea de Netaro."],
33: ["Donde el suelo está helado, resbala y cuesta andar... Ve con cuidado..."],
34: ["Te daré un buen consejo... Por aquí conviene calzarse unas raquetas... Las venden en esa tienda de objetos."],
35: ["Qué frío... Desde que llegaron los ogros hace aún más frío por aquí. Los niños son inocentes y no lo notan... pero a los viejos el frío nos puede."],
36: ["Qué frío... Qué helada... Gracias a que acabaste con los ogros ahora se está algo más templado. De verdad, muchísimas gracias."],
37: ["Momotaro, acaba con los ogros, por favor... La abuela ya no aguanta el frío. Te lo suplico, acaba con ellos."],
38: ["Momotaro, gracias a ti la abuela parece estar un poco mejor. Muchísimas gracias..."],

 # ---------------------------------------------- Aldea de Urashima (mar)
39: ["Ésta es la aldea de Urashima."],
40: ["Yo, de joven, era buceadora y recogía caracolas en el mar. De lo que hay bajo el agua sé un rato..."],
41: ["¿Conoces las aletas de kappa? Con ellas se nada libremente bajo el agua. Las tienen en la tienda de objetos, más te vale comprarlas..."],
42: ["Dicen que sin el caparazón de tortuga no se puede uno sumergir en el mar... Pero ¿cómo se consigue?"],
43: ["Dicen que si salvas a una tortuga te presta su caparazón... Yo también quiero salvar una y bajar al fondo del mar."],
44: ["Hasta el Palacio del Dragón que visitó Urashima está ahora en manos de los ogros."],
45: ["Bendito seas... La paz ha vuelto al mar... Todo gracias a ti..."],
46: ["El mar se ha embravecido y no podemos salir a faenar... Como siga así acabaremos muriéndonos... ¿Qué podemos hacer?"],
47: ["Oh... El mar ha vuelto a su ser... Y también es gracias a ti... De verdad, muchísimas gracias."],
48: ["Si te ves en apuros, súbete al faisán y asciende. Lo dijo el autor del juego, así que es verdad..."],

 # ---------------------------------------------- Monte Kachikachi (fuego)
49: ["Del monte Kachikachi salen volando chispas, es peligrosísimo. Ten cuidado tú también, chaval. Si te alcanzan, el daño es grande..."],
50: ["Ay... qué calor... ¿Y si me quito el kimono de una vez? ...... ¿Qué miras tú?"],
51: ["Uf, parece que todo ha vuelto a la normalidad. Nunca he llevado bien el calor."],
52: ["Si caes en la lava recibirás daño... Lo que está anaranjado es lava... Ándate con mucho ojo..."],
53: ["Por culpa de los ogros ya no podemos acercarnos al monte. Y las aguas termales del Kachikachi eran nuestro único placer..."],
54: ["Gracias a ti podemos volver a las termas del Kachikachi... Mi mujer y yo seguiremos bañándonos juntos y viviremos en paz..."],
55: ["Sí, sí, abuelo, ya te oigo. Aunque no lo parezca, yo fui Miss Calabaza en mis tiempos. Hoy también hace buen día..."],
56: ["Sí, sí, abuelo, ya te oigo. Aunque no lo parezca, la calabaza era mi comida favorita. Hoy también hace buen día..."],
57: ["En las termas del Kachikachi, si te subes encima cuando brota el agua, te lleva hasta muy alto... Cuando no había ogros jugábamos mucho."],
58: ["¡Bien! Ahora podremos jugar en las termas como antes... ¡Gracias, Momotaro!"],

 # ---------------------------------------------- Aldea de Issun-boshi
59: ["Ésta es la aldea de Issun-boshi. No levantes la voz."],
60: ["Ésta es la aldea de Issun-boshi. Menos mal que todo ha vuelto a su ser."],
61: ["Ese ogro enorme de las afueras... Si despierta volverá a arrasar la aldea... Del miedo no pego ojo por las noches."],
62: ["Ay, de verdad, muchísimas gracias... Ahora podré dormir a pierna suelta. Para un viejo, dormir es el mayor placer. De verdad, gracias..."],
63: ["Por culpa de ese ogro no podemos jugar a voces... Y jugar bajito no tiene ninguna gracia."],
64: ["¡Bieeen! ¡Ya podemos gritar! Así es como hay que jugar. Y además podemos salir a jugar fuera. ¡Muchísimas gracias!"],
65: ["Ese ogro que duerme ahí fuera... Dicen que se hizo enorme con el mazo mágico... Y que desde entonces lleva todo el tiempo dormido ahí."],
66: ["¡Bravo! Derrotar a semejante ogro... Digno del mejor de Japón, Momotaro. A ese ogro de piedra lo usaremos para pasar."],
67: ["Para derrotar a ese ogro no queda más que entrar por su boca y armarla dentro. Pero dicen que en sus tripas hay muchos ogros temibles..."],
68: ["¡Cómo! ¿Tú has vencido a ese ogro...? Qué gran valor escondido en un cuerpo tan pequeño... Me quito el sombrero."],
69: ["Dicen que en el estómago del ogro el techo y el suelo son una trampa entera... Meterse ahí es una temeridad..."],
70: ["Vaya... ¿Estás sano y salvo? Increíble... Eres un joven de verdadero valor."],

 # ---------------------------------------------- Aldea de Taketori
71: ["Ésta es la aldea de Taketori."],
72: ["La princesa Kaguya ha aprendido hace poco a... ¡apostar! Dicen que anda probando suerte por todas partes. ¿Y si lo intento yo también?"],
73: ["Dicen que sobre las nubes hay un mundo donde viven los ogros... Nosotros jamás podríamos llegar..."],
74: ["¡Huyyy! ¿Que has subido sobre las nubes y has acabado con los ogros...? Menudo tipo estás hecho..."],
75: ["A los ogros no sólo hay que castigarlos: a veces conviene aprovecharlos. Sobre todo a los del taparrabos... ¡Ja, ja, ja!"],
76: ["A esta vieja la han engañado del todo: se cree que los ogros son dioses."],
77: ["La abuela ha vuelto en sí, y también es gracias a ti... Je, je, ¡gracias!"],
78: ["Oh, señor Fuujin, señor Fuujin... Nuestro dios protector... Siempre nos vela desde el cielo... Cuánto se lo agradecemos. Namu Amida Butsu, Namu Amida Butsu."],
79: ["¿Qué he estado haciendo yo hasta ahora...? Pero si sigo sano y salvo es gracias a Buda. Namu Amida Butsu, Namu Amida Butsu."],

 # ---------------------------------------------- El castillo de Enma
80: ["Momotaro, ya sólo podemos confiar en ti... Derrota a Enma con tu fuerza, te lo suplicamos..."],
81: ["No puedo más... Ya no lo aguanto... Viviendo en un sitio así uno acaba perdiendo la cabeza."],
82: ["Momotaro, sabía que llegarías hasta aquí... Bien vale la pena vivir muchos años."],
83: ["Mi espada se partió y se me acabaron las flechas. Enma es terriblemente fuerte... Si sigues adelante solo perderás la vida en vano. Si no quieres morir, no avances más."],
84: ["Mi padre fue a enfrentarse a Enma y nunca volvió... Momotaro, venga a mi padre... Te lo pido, también por toda la aldea... ¡Mucho ánimo, Momotaro!"],
85: ["Tras muchos años de estudio, el punto débil de Enma resultó ser, como imaginaba, la diana. La diana está dentro de su boca... Pero eso sólo sirve si logras llegar hasta él."],
86: ["Casi todos los aldeanos han huido ya... Momotaro... Las esperanzas de todos están puestas en ti... Castiga a Enma y trae la paz al mundo. Ve... Momotaro..."],
}


def repartir(texto, ancho=ANCHO, lineas=LINEAS):
    """Parte en lineas sin cortar palabras y agrupa en paginas.
    Devuelve lista de paginas; cada pagina es lista de lineas."""
    ls, ln = [], ''
    for p in texto.split():
        if not ln:
            ln = p
        elif len(ln) + 1 + len(p) <= ancho:
            ln += ' ' + p
        else:
            ls.append(ln)
            ln = p
    if ln:
        ls.append(ln)
    for l in ls:
        assert len(l) <= ancho, 'no cabe: %r (%d > %d)' % (l, len(l), ancho)
    return [ls[i:i + lineas] for i in range(0, len(ls), lineas)]


if __name__ == '__main__':
    import sys
    ancho = int(sys.argv[1]) if len(sys.argv) > 1 else ANCHO
    tot = 0
    for i in sorted(TEXTOS):
        for parr in TEXTOS[i]:
            pgs = repartir(parr, ancho)
            tot += len(pgs)
            print('[%2d] %d pagina(s)' % (i, len(pgs)))
            for pg in pgs:
                print('     +' + '-' * ancho + '+')
                for l in pg:
                    print('     |%-*s|' % (ancho, l))
                print('     +' + '-' * ancho + '+')
    print('\ntextos: %d   paginas: %d' % (len(TEXTOS), tot))


# ---------------------------------------------------------------------------
# MAQUETA FIJA (norma 38: no reparticionar el texto de David sin avisar)
#
# Cuando David da el reparto en lineas y paginas, manda el suyo y no el del
# algoritmo. Cada entrada es una lista de PAGINAS y cada pagina una lista de
# LINEAS, tal cual las dibujo el.
MAQUETA_FIJA = {
    34: [["Te daré un buen",
          "consejo... Por aquí",
          "conviene calzarse"],
         ["unas raquetas...",
          "Las venden en esa",
          "tienda de objetos."]],
    # 66: David pidio este reparto. Su primera linea, "ese ogro petrificado",
    # medía 20 y el ancho es 19; el eligio "ese ogro de piedra" (18).
    66: [["¡Bravo! Derrotar a",
          "semejante ogro...",
          "Digno del mejor de",
          "Japón, Momotaro. A"],
         ["ese ogro de piedra",
          "lo usaremos para",
          "pasar."]],
    40: [["Yo, de joven,",
          "era buceadora y",
          "recogía caracolas"],
         ["en el mar. De lo",
          "que hay bajo el",
          "agua sé un rato..."]],
}
