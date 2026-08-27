# INFORME DE TRASPASO — Momotarou Katsugeki en castellano

**Fecha:** 2026-08-27 · **Estado:** v386 promocionada a **ROM OFICIAL**

Este informe basta para que un chat nuevo retome el proyecto sin contexto
previo. Léelo entero antes de tocar un byte.

---

## 1. El proyecto

Traducción al castellano de **Momotarou Katsugeki** (PC Engine, 512 KB, HuCard).

- **Dirige: David** (*Psicopompo*, elotrolado.net). Las decisiones de diseño y
  de maquetación **son suyas**.
- Repo: `https://github.com/psichopompo/Momotaro-Katsugeki-en-espa-ol`
- ROM base: `Momotarou Katsugeki (Japan).pce`, MD5 `ec7358edb3672a8aa8850623eec72a71` — **INTOCABLE**

### La ROM oficial

```
roms/Momotaro Katsugeki (Español).pce
MD5    eaf7751123990575182612e52f34192c
SHA-1  ddf3725339622c6754ee1dce02b3df1874508f1f
CRC32  A7493CFE
```

Parche: `parches/Momotaro Katsugeki (Español).ips` (contra la virgen,
round-trip verificado). `momotaro_es_v386.pce` es el mismo fichero.

**Testeada por David:** primera fase completa, todos los aldeanos, todas las
tiendas, varios minijuegos, el quiz, el jefe final, los cuatro finales y las
dos pantallas secretas. Todo correcto. Falta el testeo del juego completo.

---

## 2. Cómo tratar con David

No es opcional. Está aquí porque saltárselo ha costado disgustos reales.

- **Siempre en castellano.** Tutear.
- Reconocer los errores propios **explícitamente**, diciendo qué falló en el
  razonamiento. No maquillarlos, no diluirlos.
- Distinguir **[HECHO]** (medido) de **[HIPÓTESIS]**.
- Estilo: ingeniero explicando su trabajo. Conciso. **No ser condescendiente.**
  No insistir en que descanse.
- **Una sola pregunta por mensaje**, al final, con `¿` de apertura.
- Capturas individuales, nunca rejillas.
- **Si David contradice el análisis, comprobarlo antes de descartarlo: ha
  tenido razón SIEMPRE.**
- No sacar una versión por cada cambio mínimo: agrupar.

### Órdenes permanentes

- **No se genera ROM hasta ver capturas de cómo quedan los cambios.**
- **No se toca el bocadillo apaisado.** David: *«ese bocadillo comparte formato
  con otros, así que podríamos romper algo. Además nos lo curramos bastante.
  Los textos en castellano necesitan bocadillos horizontales más grandes.»*
- **No bloquear el menú RUN cuando habla el abuelo.** David: *«El abuelo sólo
  aparece en fases de acción, donde podemos necesitar abrir el menú en
  cualquier momento para curarnos, usar un arma, etc.»*

---

## 3. Las normas que más han costado

Están todas en `LEEME.md` (12-356). Las críticas:

| # | Norma |
|---|---|
| **352** | **Mirar la captura ENTERA antes de enviarla.** Se mandaron 5 capturas como prueba de un arreglo y el bug estaba visible en las cinco. |
| **353** | No dar por bueno un arreglo con prueba artificial (borrar celdas, contar bytes). Reproducir la escena como la vive el jugador. |
| **354** | Un savestate tomado **después** del bug no dice cómo era la escena **antes**. Diagnosticar sobre el estado dañado y llamarlo diseño original produjo un diagnóstico entero falso. |
| **355** | Antes de tocar un cargador de datos, escribir su codec y probar `encode(decode(x)) == x` byte a byte, y validar el decode contra la VRAM real. |
| **356** | Un volcado puede subir mucho más de lo que se usa. Medir qué celdas **referencia la SAT** frente a cuáles **se sobrescriben**. |
| 346 | **El word 2 del SAT es el patrón POR DOS**: `celda = (word2 >> 1) & 0x3FF`. |
| — | **La verdad es lo que se ve en pantalla, no el hex.** |
| — | **NUNCA partir una palabra.** Si no cabe, la palabra entera baja. |

### Traducción

Fidelidad y naturalidad, con **puntos finales**. Sin abreviaturas.
**Momotaro** sin `u` final. **Sólo** con tilde. Staff en orden occidental con
inicial si no cabe (`H. Iizuka`, nunca `IiDuka`). Cargos en MAYÚSCULAS. En
créditos, nombres sin punto final; frases sí.
Finales: Muy difícil / Difícil / Normal / Fácil.

---

## 4. Arrancar en 30 segundos

```python
import sys; sys.path.insert(0, 'tools')
from pce import PCE
import estados, sat

p = PCE('roms/Momotaro Katsugeki (Español).pce')
estados.carga(p, 'states/7_item.state')
p.run(30)
p.png('/tmp/foto.png')              # MIRARLA ENTERA
p.press('START', frames=3, after=25)

v = sat.vram(p)
for d in sat.visibles(v):
    print(hex(d['cel']), d['x'], d['y'])
```

### Trampas del emulador (medidas, no supuestas)

- Sin `retro_set_controller_port_device(0,1)` **no llega ningún botón**. Ya
  está en `pce.py`.
- Botón de diálogo = **A**. Menú = **START**.
- **`p.vram()` devuelve 0 bytes**: el core no expone la VRAM. Usar
  `sat.vram(p)`, que la saca de la sección `VRAM` del savestate.
- Los `.state` de David son RZIP (`#RZIPv\x01#` + 16 B + zlib) y el core traga
  desde el offset 16 del descomprimido. `estados.carga()` se encarga.
- **capstone en modo 65C02 NO sirve**: lee `TAM ($53)` como `nop` y se
  desincroniza. Usar `tools/dis6280.py`.
- Al desensamblar, traducir bien el banco: `PC` → `ROM = banco*0x2000 + (PC & 0x1FFF)`.
  Equivocarse de banco da código basura que parece real.

### El toolkit

| Fichero | Para qué |
|---|---|
| `tools/pce.py` | emulador: `run/press/png/ram/poke/peek/state` |
| `tools/sat.py` | `vram()`, `sat()`, `visibles()`, `celda()` |
| `tools/estados.py` | carga los `.state` de David |
| `tools/cg.py` | codec del CG comprimido, con round-trip |
| `tools/state.py` | secciones de un savestate |
| `tools/dis6280.py` | desensamblador HuC6280 |
| `tools/password.py` | teclea contraseñas |
| `tools/charset_*.py` | los tres juegos de caracteres |
| `tools/bin/mednafen_pce_libretro.so` | Beetle PCE estándar |
| `tools/bin/mednafen_pce_trace.so` | con watchpoints (`watch`, `watch_write`, `log_on`) |

Recompilar el core (si hiciera falta, ~16 s):
```
git clone --depth 1 https://github.com/libretro/beetle-pce-libretro.git /tmp/bpce
cd /tmp/bpce && make -j2
```
Hooks en `HuC6280::RunSub` (antes de `RdOp(PC)`) y `HuC6280::WrMem`; exportar
símbolos añadiendo `mkt_*;` a `link.T`.

---

## 5. Conocimiento técnico vigente

### Contraseñas y rejilla

Cursor `$3C91` (col) / `$3C92` (fila), buffer `$3C94`. **14 columnas, no 16.**
La fila 2 empieza por **Ñ**, no por O. Se acepta con **START**.

```
fila 0  A B C D E F G  a b c d e f g   códigos $01..$0E
fila 1  H I J K L M N  h i j k l m n   códigos $0F..$1C
fila 2  Ñ O P Q R S T  ñ o p q r s t   códigos $1D..$2A
fila 3  U V W X Y Z    u v w x y z     códigos $2B..$36
fila 4      0 1 2 3 4 5 6 7 8 9        códigos $37..$40
```

Muy difícil `wCpeIfP` · Difícil `GoFIBM` · Normal `cJQIep` · Fácil `rGAPad`
Sound test `BqdGlCIWÑI` · Graphics test `BqdGlDWÑI`

### El bocadillo del abuelo (cerrado en v386)

- Identificador **`$368F`**: `2` = bocadillo del abuelo, `1` = aldeano,
  `0` = resto. Idea de David, confirmada en 12 escenas.
- Listas de sprites: `celda = $170 + byte0`.
  - `0x47C02..0x47C97` lista compartida, 30 registros (aldeanos/Jizo/tiendas)
  - `0x47C99..0x47CA0` tabla de punteros — **INTOCABLE**
  - `0x47CA1..0x47CFA` lista del abuelo, 18 registros → `$1C4-$1CA`,
    `$1D4-$1DA`, `$1DC`, `$1DD`
  - `0x47CFC..0x47FFF` **LIBRE, 772 B**
- El rabillo **no va en la lista**: lo emite `$9A78` aparte, eligiendo entre
  las 4 variantes de `$9ADD` según `$368F`.
- Un sprite de 32 px **redondea su celda a par**: el VDC ignora el bit 0.

### El menú RUN

```
$3B50  menú abierto      $3B51  nivel activo (0,1,2)   $3BA2  ventana que se dibuja
$D59B  JSR $DFC3   dibuja marco+texto sólo si $3BA2 == $3B51   (cueva de la v383)
$D3C7  redibujado del AVANCE          $D3E4  JMP $DFD2 (retroceso, cueva v385)
$D304  calcula destino VRAM; tabla en $D320 (ROM 0x19320), 12 entradas
$D268  sube el CG del menú  <-- el que causaba el bug del bocadillo
tabla de coordenadas ROM 0x195A6: los 4 pares a $50/$61 (centrado, v383)
```

Bloques de sprite en banco `$17`, tabla `$4730` (ROM `0x2E730`): 4 filas de 3
bloques; los terceros de cada fila tienen **4 registros**, los otros 2.

### El CG comprimido (`tools/cg.py`) — descubierto en la v386

Descompresor en `$861F` (banco `$20`, ROM `0x4061F`); rutina de byte en `$867F`.

Formato: por celda, 4 grupos de 4 llamadas (`Y` = 0, 1, `$10`, `$11`). Cada
llamada = 1 byte de máscara + literales; bit a 1 lee literal nuevo, bit a 0
repite el anterior (A=0 en la posición 0); escribe 8 bytes en `Y, Y+2, … Y+14`.

Stream del menú en **ROM `0x22CA0`**: 1 byte de cuenta + datos.
Original: 58 celdas, 1329 B. Ahora: 3 bloques (4+4+26 celdas), 755 B.

### Otros hallazgos

- **`$3BA6`** elige tabla de glifos: `0`→`$9CF3`, `1`→`$9CB3`. Con `$3BA6=1`
  el código `$C6` da `$7F` (ú minúscula), no la Ú.
- **`$37F8`** = dificultad en los créditos: 0=Fácil, 1=Normal, 2=Difícil,
  3=Muy difícil. Tabla `$DD07` (ROM `0x03D07`).
- **Fuentes:** diálogo 1bpp en `0x3D660 + glifo*8` (A-Z = `$70`-`$89`); menú
  2bpp en `0x4000 + (g-$30)*16`, con sombra
  `dilatar(cuerpo,{(+1,0),(0,+1),(+1,+1)}) - cuerpo`.
- **Vocales acentuadas de David** (v379): Á=`$C2` É=`$C3` Í=`$C4` Ó=`$C5`
  Ú=`$C6`; cuerpo en filas 2-6, base en la 6, tilde diagonal de 2 px.
- **Tres charsets:** `charset_oficial.py` (menú, alias b=$5B c=$5D p=$5E),
  `charset_vitores.py` (motor `$9B0B`, bytes directos), `charset_rotulos.py`
  (motor `$AAB4`, alias b/c + e=$3D o=$62). **El Sound Test usa ASCII puro**
  (A=`$41`).

---

## 6. Lo siguiente que toca

### ⭐ Artefactos sobre los cerezos de los vítores — es el siguiente

Al pasarse el primer jefe salen los vítores con cerezos en flor de fondo, y
**sobre cada árbol aparece el mismo cuadrado de artefactos**. Siempre el
mismo, sobre cada árbol.

Material en `capturas/bug_vitores/`: `en_pantalla.png` (el bug tal cual),
`tilemap_1..4.png` (Tilemap Viewer con los tiles señalados) y `tileviewer.png`.

Datos de las capturas de David: tiles `$2D0`, `$2CE`, `$2B7`, `$2B9`;
columnas 13-16, filas 43-46; **paleta 2**; tilemap 64x64 en `$0000`, 4 bpp.
Savestate: `states/Vitores.state`.

[HIPÓTESIS sin comprobar] Que sea siempre el mismo cuadrado sobre cada árbol
sugiere que la copa referencia celdas que otra cosa reutiliza — el mismo
patrón que tenía el bocadillo. **Medirlo antes de darlo por bueno.**

### El resto (en `docs/PENDIENTES.md`, registro único)

1. Bug gráfico bajo la cabeza del ogro rosa (final Difícil).
2. Tabla `0x24DE` (presentación de enemigos, 38 entradas de 8 B): apunta a
   offsets japoneses.
3. 15 `$00` de relleno en `0x4A476-0x4A483`: páginas fantasma.
4. Colas invisibles en descripciones de objeto (`e vida.`, `écnica.`…).
5. Texto de vítores 4 px por encima del bocadillo; posadero «¡Buenos días!
   ¡A por los» (falta «ogros.»); abuelo «El perro te acompaña» sin punto final.
6. Backup RAM (`0x1F51E`, 674 B) y 5 mensajes sueltos del menú (`0x435E6`,
   `0x4363D`, `0x4366B`, `0x4369C`, `0x436CC`).
7. **Salvedad documentada:** la lista compartida `0x47C02` tiene 4 registros
   (`$1D0-$1D3`) que pisan el juego 0 del menú. Inofensivo hoy porque
   bocadillo y menú nunca coexisten salvo con el abuelo.

---

## 7. El workspace

```
COMO_RETOMAR.md              arranque rápido (leer primero)
Momotaro/
  LEEME.md                   normas 12-356 + estado
  investigation.md           diario, 230 entradas
  roms/                      japonesa virgen + oficial + v386
  parches/                   oficial + hitos (v334, v338, v378, v385, v386)
  states/                    56 savestates, todos verificados
  capturas/                  8 vigentes + bug_vitores/
  docs/                      PENDIENTES.md (registro único), PROMPT_METODO.md,
                             MAQUETACION_*, QUIZ.md, GUION_para_traducir.md,
                             Log_completo_hasta_v83.txt, este informe
    historico/               informes de etapas cerradas
  tools/                     el toolkit
    historico/               los build_* de versiones borradas
Nekketsu/                    proyecto aparte, TERMINADO (v2.18)
```

**Las ROMs intermedias se borraron a propósito**, tras comprobar que los 33
IPS las reproducen byte a byte sobre la japonesa. Cualquiera se regenera.

**Los savestates no se borraron por corrupción**: se cargaron los 58 y los 58
funcionaban. Sólo se quitaron basura de macOS y 5 duplicados exactos por MD5.

### El método (`docs/PROMPT_METODO.md`)

Diario en `investigation.md`. **Las hipótesis falsas NO se borran**: se marcan
`[DESCARTADO]` y se explica por qué fallaron — la entrada 229 corrige a la 228
y las dos siguen ahí. Una medición → una causa → un arreglo → una verificación.
Prohibido escribir bytes a ciegas. Cada versión con MD5/SHA-1/CRC32. Asserts
con byte esperado, hueco libre y zonas intactas. IPS contra la virgen con
round-trip.
