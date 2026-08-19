# CÓMO RETOMAR — Momotarou Katsugeki (PC Engine) · traducción al castellano

> **Lo primero: borra `workspace.zip` en cuanto lo hayas descomprimido.**
> Ocupa espacio y se queda obsoleto en cuanto se saque una versión nueva.

---

## 1. Quién es quién

Diriges el proyecto con **David** (alias *Psicopompo*, foro elotrolado.net).
Repo: `https://github.com/psichopompo/Momotaro-Katsugeki-en-espa-ol`

**David no es romhacker.** Dirige, aporta ideas, edita gráficos y prueba en
emulador y hardware. Sabe manejar breakpoints si le das instrucciones
exactas. **Sus mediciones en pantalla son la fuente de verdad**: ha tenido
razón en todas las ocasiones en que ha contradicho el análisis.

### Cómo hablarle

- **Siempre en castellano. Tutear.**
- Reconocer los errores propios **explícitamente**, diciendo qué falló en el
  razonamiento. No maquillarlos.
- Distinguir **[HECHO]** (medido, con evidencia) de **[HIPÓTESIS]**.
- Estilo: ingeniero explicando su trabajo. Conciso. No generador de parches.
- **Una sola pregunta por mensaje**, al final, con `¿` de apertura.
- Capturas individuales, no rejillas.
- No sacar una versión por cada cambio mínimo: agrupar.
- La maquetación la decide él (norma 38).
- Si algo sale mal, **revertir** al último estado bueno en vez de parchear
  parches (norma 107).
- **No usar Claude ni depender de él.**

David: *«Yo siempre voy a por todas»* — prefiere la solución completa.

---

## 2. Estado actual

**ROM buena: `Momotaro/roms/momotaro_es_v272.pce`**

```
MD5    3043e0bdeffaae160e295b95c9400e4e
SHA-1  ff624798c5b2038c5302a0a44d8b3a384f21c73d
CRC32  8EB08FDE
```

Parche: `Momotaro/parches/momotaro_v272.ips` (contra la ROM virgen, con
round-trip verificado).

### Qué se ha cerrado en esta tanda

| Versión | Qué |
|---|---|
| v264 | La `p` de «Capa» (`$5E`, no `$B0`) |
| v268 | **Password del Jizo en página limpia**, 3 líneas, arriba |
| v269 | Menú RUN del banco `$21`: No vale / Comer / Usar / Tirar / Sin nadie / Perro / Faisán / Mono |
| v270 | El `$01` duplicado del «Nada» (`0x42ED9`, `0x42F45`) |
| v271 | **Menú RUN real del banco `$0C`** + repunte |
| v272 | Artes / No puedo / ¡Puaj! (ajuste al ancho de 8) |

Versiones intermedias borradas. Se conservan v264, v268, v269, v270, v271,
v272, la v263 del otro chat y la **virgen (INTOCABLE)**.

---

## 3. Método obligatorio

Está en `Momotaro/docs/PROMPT_METODO.md`. Resumen:

1. **Una medición → una causa → un arreglo → una verificación.**
2. **Prohibido escribir bytes a ciegas.**
3. Diario `investigation.md`, **27.600 líneas, FUSIONADO de las dos ramas**:
   tronco común hasta la línea 10.737, luego `# RAMA A` (el otro chat) y
   `# RAMA B` (esta, la que produce la v272). **Las dos ramas tienen
   numeración solapada**: la entrada 162 de una no es la de la otra. Buscar
   en las dos antes de dar algo por sabido.
   Las hipótesis falsas **no se borran**: `[DESCARTADO]` con el motivo.
4. Cada versión con MD5 / SHA-1 / CRC32.
5. Desensamblar todo salto escrito a mano **desde la ROM ya escrita**.
6. Los constructores llevan `assert` que comprueban: byte esperado antes de
   escribir, hueco libre, zonas intactas, y **relectura del resultado**.

### El assert que más veces ha salvado la sesión

Releer la cadena **siguiendo el puntero como hace el motor** y comparar con
el texto esperado. Cazó que «Tirar» se estaba escribiendo encima de una
tabla de punteros.

Y el aviso correspondiente (norma 212): **un assert que compara el código
contra tu propio simulador no verifica nada si el simulador está mal.** Un
`BCS` simulado con signo dio por bueno un bucle infinito y colgó la v267.

---

## 4. Los cinco errores que más caros han salido

Están todos en el LEEME como normas. Léelos antes de tocar nada.

**1. Dar por supuesta la ventana MPR (norma 232).** Pasó **tres veces**:
`$DE69`, `0x4379D` y el banco `$0C`. Un banco se mapea donde se mapea, no
donde parece por su offset. El `$0B` y el `$0C` van a **`$C000`**; el `$21`
a **`$A000`**. Consecuencias reales: un breakpoint que nunca saltaba, y una
búsqueda de punteros que decía «ninguna» cuando sí los había.

> **Antes de dar una dirección CPU, verifícala contra una referencia
> conocida del mismo banco.** Ej.: `0x16A73` = `$CA73` fija el banco `$0B`.

**2. Confundir «encaja» con «es» (norma 236).** Traduje `ﾄﾞｳｸﾞ ﾎｼｲ` del banco
`$21` porque coincidía con el nombre *dougu*. Era diálogo. Las etiquetas
reales estaban en el banco `$0C`. **Confirmar siguiendo el código o con un
breakpoint, nunca por parecido del texto.**

**3. Sumar huecos sin comprobar el reparto (norma 219).** 69 B libres y 66 B
necesarios no significa que quepa: con huecos fragmentados y cadenas
indivisibles hay que **resolver el empaquetado**. Best-fit se encajona con
ajustes exactos; usar backtracking.

**4. Buscar la huella equivocada (norma 216).** Concluí que no había tabla
de punteros porque no encontraba `LDA tabla,X`. El intérprete de script
recibe el puntero **como operando del guion**, no con direccionamiento
indexado. Cómo se demuestra que unas words son una tabla: una entrada
**repetida**, destinos que **teselan** las cadenas sin huecos, presencia en
la **ROM virgen**, e invocación como `[cmd][word]`.

**5. Sacar conclusiones de una diferencia (norma 228).** Medí que 133 glifos
de `0x3D660` diferían de la virgen y deduje que el original era katakana.
Falso: al restaurarla salieron líneas horizontales. **`0x3D660` no es la
fuente japonesa.**

---

## 5. Mapa técnico

### Bancos y ventanas (verificado)

```
banco $0B   ROM 0x16000-0x18000  ->  $C000-$DFFF   código del bocadillo
banco $0C   ROM 0x18000-0x1A000  ->  $C000-$DFFF   MENÚ RUN
banco $1E   ROM 0x3C000-0x3E000  ->  $4000-$5FFF
banco $20   ROM 0x40000-0x42000  ->  $8000-$9FFF   motor de texto
banco $21   ROM 0x42000-0x44000  ->  $A000-$BFFF   inventario, tiendas
```

### Cadena de decodificación de glifos (3 pasos, no 1)

```
1. sustitución previa $AB34 — DOS arrays paralelos de 7 bytes:
     origen  0x42B4C:  20 21 2D B0 A2 A3 24
     destino 0x42B54:  3C 5C 5F 5F 5B 5D 3E
   (leerla "en pares intercalados" da ruido)
2. $CB1B elige ruta:
     si (cod-$30) < $54  -> BAJA: idx = rom[0x43F9B + cod - $30]
     si no               -> ALTA: idx = rom[0x41C73 + cod - $20]
3. glifo en 0x3D660 + idx*8
```

Alias obligatorios: **`b=$5B`, `c=$5D`, `p=$5E`**. Solo `$5E` da la `p`.
El glifo `$00` **no está en blanco** en el menú SELECT: pinta un cuadrado
negro. Pero **sí** es transparente dentro del bocadillo (norma 221).

### Menú RUN — banco `$0C`

```
tabla 0x197F2   [0] $DC50 Objetos   [1] $DFBC Artes
                [2] $D807 password  [3] $D810 debug     (los dos en japonés)
tabla 0x19A61   [0] $DC1F ¡Puaj!    [1] $DFAF No puedo

punteros INMEDIATOS (LDA #lo / STA $BF / LDA #hi / STA $C0):
  0x199BC/0x199C0 -> $DBF9  Faltan momos
  0x199C5/0x199C9 -> $DFAF  No puedo
  0x199F0/0x199F4 -> $DFAF  No puedo
```

**El bocadillo tiene 8 CELDAS de ancho.** El bucle `$D619` no corta: escribe
hasta el `$00` y lo que sobra se pinta fuera del marco. Toda etiqueta ≤ 8.

### Menú RUN — banco `$21`

```
tabla $B1AC (0x431AC)  No vale / Comer / Usar / Tirar
tabla $B1CC (0x431CC)  Sin nadie / Perro / Faisán / Mono
```

⚠️ **La tabla `$B1CC` vive DENTRO del bloque de cadenas** (`0x431CC`, en
medio). No son 55 B seguidos: son 24 + 23 en dos trozos.

### Password del Jizo (v268)

```
$CA73  JSR $CABD                    borra las dos mitades
$CABD  21 B  JSR $9C29 / LDA #3 / STA $3657 / PHA / JSR $9B7C / PLA
              SEC / SBC #2 / CMP #1 / BPL / RTS
$CAAA  JMP $DE69                    continuar en la misma página
$DE69  15 B  JSR $9B7C / JSR $9C29 / LDA #3 / STA $3657 / CLX / JMP $CA78
```

El bocadillo tiene 4 filas pero el buffer solo 32 celdas = 2 filas. `$3657`
elige la mitad: **1 o 2 → filas A (1-2)**, **3, 4 o 0 → filas B (3-4)**.

### Huecos libres verificados

```
banco $0B:  0x17E78-0x18000   (tras la rutina del password)
banco $0C:  0x19C0B (6 B), 0x19C2B (12 B), 0x19C5A (6 B), 0x19FC5 (59 B)
banco $21:  0x42F7D (4), 0x42FAA (5), 0x4300E (3), 0x43094 (4),
            0x430C2 (3), 0x4311A (5), 0x43173 (5), 0x43432 (4)
```

---

## 6. Qué queda pendiente

### 1. `Faltan momos` mide 12 caracteres — RIESGO ABIERTO

Traducción de `ﾜｻﾞﾉﾓﾓｶﾞﾅｲ` (ahora en `$DBF9`). Si usa el bocadillo de 8
celdas se verá **«Faltan m»**. **No está medido**: puede que use un marco
más ancho, porque el japonés original también era largo.

**Lo primero que hay que preguntarle a David.** Alternativas ya contadas:
«Sin momo» (8), «Faltan» (6), «No hay» (6), «Pocos» (5).

### 2. El «Nada» de las aldeas

El `$01` duplicado de `0x42ED9` y `0x42F45` era un bug real y está
corregido, pero **David seguía viendo mal el menú de aldea**. Es probable
que ese menú lea de otro sitio, sin localizar. Medir antes de tocar.

### 3. Mensajes del menú que solo se ven provocándolos

Varios mensajes del menú RUN solo aparecen haciendo cosas absurdas a
propósito: darle a Comer a algo que no se come, Usar una comida, gastar una
técnica sin momos. **No hay forma de verificarlos salvo jugando**, así que
David los irá cazando poco a poco. Es normal que aparezcan informes sueltos
sobre ellos.

Ojo con un falso positivo ya resuelto: el **«Perro»** que sale al elegir
Usar sobre el Dango **no es un error nuestro**, está igual en la ROM
japonesa (norma 240).

### 4. Las tiendas — es TEXTO SIN TRADUCIR, no un bug

**Ojo, aquí me equivoqué y está corregido (norma 250).** Medí el volcado de
David, vi un pico de exactamente 16 sprites por línea y concluí saturación.
Pero 16 es el límite, no un exceso: **16 caben**.

La rama A lo tenía medido en 19 volcados (su entrada 212): las tiendas
llegan a **11 de 16**. Ni se acercan.

La causa real: los rangos de códigos **solapan**. Nuestro texto usa
`$A1-$B4` para `a..t` y el katakana ocupa `$B1-$C5`. El mismo byte es letra
o kana según la fuente activa. Quedan **58 tramos, 7.786 bytes** de japonés
sin traducir que hoy se pintan con la fuente latina.

**Los artefactos son texto japonés sin traducir y se irán solos** conforme
avance el guion. No hay que repartir sprites.

### 5. El hilo del foro

`Momotaro/docs/Hilo_Momotaro_v5.txt`, en **BBCode**. **Límite duro del foro:
100.000 caracteres**, y ojo con cómo se mide: el editor cuenta los saltos de
línea como **CRLF (2 caracteres)**, así que la métrica buena es
`len(texto) + texto.count('\n')`, no `len(texto)`. Con ~1.150 líneas son
1.150 caracteres invisibles de diferencia (norma 253).

Ahora mismo va por **99.029** contando bien, con 971 de margen. Para añadir
algo hay que recortar otro tanto. La v3 se borró por
obsoleta; la v4 la editó David online y de ahí sale la v5.

Estilo, y esto importa: **párrafos narrativos, no frases sueltas**. Hay que
contar lo que se ha hecho, los triunfos y los problemas, las decisiones
fortuitas y los errores. Los capítulos técnicos van dentro de `[spoiler]`.

Al tocarlo, comprobar siempre: balance de etiquetas BBCode, y que el índice
coincida **en el mismo orden** que los títulos reales de los capítulos.

### 6. Japonés pendiente

`Momotaro/docs/JAPONES_PENDIENTE.md`: 30 cadenas del banco `$21` con offset,
katakana, romaji y una columna para la traducción. **Ojo:** ese listado se
hizo antes de descubrir que el menú vive en el `$0C`, así que puede
contener cadenas que no se ven en pantalla. Verificar antes de traducir.

---

## 7. Herramientas

```
tools/dis6280.py       desensamblador HuC6280. USO: rom off_hex n_DECIMAL carga_hex
                       (capstone NO sirve: lee TAM como nop y se desincroniza)
tools/charset_oficial.py  el codificador validado. encode() / CHAR_TO_CODE
tools/state.py         extrae secciones de savestates de Mesen
tools/vdc_slots.py     simulador del límite de 16 sprites/scanline
tools/audita_vram.py   qué celdas usa el juego de verdad
tools/build_v272.py    el último constructor bueno — copiar de aquí
tools/historico/       constructores viejos
```

Un constructor nuevo se copia de `build_v272.py` y mantiene la estructura:
verificar la base por MD5 → comprobar lo que hay antes de escribir →
escribir → **releer siguiendo el puntero** → comprobar zonas intactas →
generar IPS con round-trip → imprimir hashes.

---

## 8. Ficheros

```
Momotaro/
├── LEEME.md                  estado + normas 12-253   <- LEER PRIMERO
├── investigation.md          diario, 160 entradas
├── roms/
│   ├── Momotarou Katsugeki (Japan).pce   INTOCABLE
│   ├── momotaro_es_v272.pce              LA BUENA
│   ├── momotaro_es_v268/269/270/271.pce  puntos de retorno
│   └── momotaro_es_v263.pce              del otro chat
├── parches/momotaro_v272.ips
├── states/                   savestates + volcado de VRAM de las tiendas
├── tools/                    herramientas + constructores
└── docs/
    ├── PROMPT_METODO.md      el método, en detalle
    ├── JAPONES_PENDIENTE.md  30 cadenas por traducir
    ├── PASSWORDS_SECRETOS.md
    └── Log_completo_hasta_v83.txt

Nekketsu/                     PROYECTO TERMINADO — NO TOCAR
├── rom/Nekketsu_Soccer_MD_ES_v2_8.md   la final
├── rom/jp.md                           la japonesa
├── entrega/                            parches y textos publicados
└── investigation.md
```

**Nekketsu está terminado y publicado. No se toca.** Se incluye solo como
referencia de método y por si David pregunta algo.

---

## 9. Primer mensaje sugerido

> He leído el LEEME, el diario y este documento. Estado: **v272**
> (`3043e0bdeffaae160e295b95c9400e4e`), con el password del Jizo en página
> limpia y el menú RUN traducido en los bancos `$21` y `$0C`.
>
> Antes de seguir necesito una medición tuya, porque es un riesgo que dejé
> abierto: **«Faltan momos» son 12 caracteres y el bocadillo del menú tiene
> 8 celdas**. Si usa ese marco se verá «Faltan m».
>
> ¿Puedes provocar ese mensaje (usar una técnica sin momos suficientes) y
> decirme si el texto sale completo o cortado?
