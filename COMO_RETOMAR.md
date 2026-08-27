# CÓMO RETOMAR — arranque rápido

**Fecha:** 2026-08-27 · **Estado:** Momotaro **v386 promocionada a OFICIAL**

Este fichero es lo primero que hay que leer. Si sólo vas a leer una cosa, que
sea ésta.

---

## Quién es quién

- **David** (*Psicopompo*, elotrolado.net) dirige el proyecto. La maquetación
  y las decisiones de diseño **las toma él**.
- Repo: `https://github.com/psichopompo/Momotaro-Katsugeki-en-espa-ol`

## Reglas de trato (no negociables)

- **Siempre en castellano.** Tutear.
- Reconocer los errores propios **explícitamente**, diciendo qué falló en el
  razonamiento. No maquillarlos.
- Distinguir **[HECHO]** (medido) de **[HIPÓTESIS]**.
- Estilo: ingeniero explicando su trabajo. Conciso. **No ser condescendiente.**
- **Una sola pregunta por mensaje**, al final, con `¿` de apertura.
- Capturas individuales, no rejillas.
- Si David contradice el análisis, **comprobarlo antes de descartarlo**: ha
  tenido razón SIEMPRE.
- No sacar una versión por cada cambio mínimo: agrupar.

## Reglas de trabajo (las que han costado sangre)

- **No se genera ROM hasta ver capturas de cómo quedan los cambios.**
- **Mirar la captura ENTERA antes de enviarla** (norma 352).
- **No dar por bueno un arreglo con prueba artificial** — borrar celdas o
  contar bytes no vale. Reproducir la escena como la vive el jugador (353).
- **La verdad es lo que se ve en pantalla, no el hex.**
- Un savestate tomado **después** del bug no dice cómo era la escena **antes**
  (354). Esto produjo un diagnóstico entero falso; ver entrada 229.
- Antes de tocar un cargador, **escribir su codec y probar el round-trip** (355).
- **NUNCA partir una palabra.** Si no cabe, la palabra entera baja.

## Traducción

Fidelidad y naturalidad, con **puntos finales**. Sin abreviaturas.
**Momotaro** sin `u` final. **Sólo** con tilde. Staff en orden occidental con
inicial si no cabe (`H. Iizuka`, nunca `IiDuka`). Cargos en MAYÚSCULAS. En
créditos, los nombres sin punto final; las frases sí.
Finales: Muy difícil / Difícil / Normal / Fácil.

---

## La ROM oficial

```
Momotaro/roms/Momotaro Katsugeki (Español).pce
MD5    eaf7751123990575182612e52f34192c
SHA-1  ddf3725339622c6754ee1dce02b3df1874508f1f
CRC32  A7493CFE
```

Parche: `Momotaro/parches/Momotaro Katsugeki (Español).ips`
(contra la japonesa virgen, round-trip verificado).

`momotaro_es_v386.pce` es el mismo fichero, con el nombre de trabajo.

**Probado por David:** primera fase completa, todos los aldeanos, todas las
tiendas, varios minijuegos, el quiz, el jefe final, los cuatro finales y las
dos pantallas secretas. Todo correcto.

---

## Arrancar en 30 segundos

```python
import sys; sys.path.insert(0, 'tools')
from pce import PCE
import estados, sat

p = PCE('roms/Momotaro Katsugeki (Español).pce')
estados.carga(p, 'states/7_item.state')
p.run(30)
p.png('/tmp/foto.png')          # MIRARLA ENTERA
p.press('START', frames=3, after=25)

v = sat.vram(p)                 # 64 KB
for d in sat.visibles(v):
    print(hex(d['cel']), d['x'], d['y'])
```

**Trampas del emulador:**
- Sin `retro_set_controller_port_device(0,1)` no llega ningún botón. Ya está
  puesto en `pce.py`.
- Botón de diálogo = **A**. Menú = **START**.
- `p.vram()` devuelve **0 bytes**: el core no la expone. Usar `sat.vram(p)`,
  que la saca del savestate.
- Los `.state` de David son RZIP: `estados.carga()` se encarga.

---

## Lo siguiente que toca

**Bug de los vítores (reclamado por David, con capturas ya guardadas).**
Al pasarse el primer jefe salen los vítores con cerezos en flor de fondo, y
**sobre cada árbol aparece el mismo cuadrado de artefactos**. Siempre el
mismo, sobre cada árbol.

Material en `Momotaro/capturas/bug_vitores/`:
`en_pantalla.png` (el bug tal cual se ve), `tilemap_1..4.png` (Tilemap Viewer
con los tiles señalados) y `tileviewer.png` (la VRAM entera).

Pistas de las capturas de David: tiles `$2D0`, `$2CE`, `$2B7`, `$2B9`, en
columnas 13-16 y filas 43-46 del tilemap, todos con **paleta 2**. Formato
4 bpp, tilemap 64x64 en `$0000`.

El resto de pendientes, en `Momotaro/docs/PENDIENTES.md` (registro único).

---

## Dónde está cada cosa

```
COMO_RETOMAR.md              este fichero
Momotaro/
  LEEME.md                   normas 12-356
  investigation.md           diario, 229 entradas
  roms/                      la japonesa virgen + la oficial + v386
  parches/                   el oficial + hitos (v334, v338, v378, v385, v386)
  states/                    56 savestates, todos verificados
  capturas/                  las vigentes + bug_vitores/
  docs/                      PENDIENTES.md, PROMPT_METODO.md, maquetación…
    historico/               informes de etapas cerradas
  tools/                     el toolkit (ver abajo)
    historico/               los build_* de versiones ya borradas
Nekketsu/                    proyecto aparte, terminado (v2.18)
```

**Herramientas vivas:**

| Fichero | Para qué |
|---|---|
| `tools/pce.py` | el emulador: `run/press/png/ram/poke/state` |
| `tools/sat.py` | `vram()`, `sat()`, `visibles()`, `celda()` |
| `tools/estados.py` | carga los `.state` de David (RZIP) |
| `tools/cg.py` | codec del CG comprimido, con round-trip |
| `tools/state.py` | secciones de un savestate |
| `tools/dis6280.py` | desensamblador HuC6280 (capstone NO sirve) |
| `tools/password.py` | teclea contraseñas |
| `tools/charset_*.py` | los tres juegos de caracteres |
| `tools/bin/*.so` | Beetle PCE, normal y con watchpoints |

**Las ROMs intermedias se borraron a propósito.** Los 33 parches IPS que
había reproducían su ROM byte a byte, así que cualquiera se regenera
aplicando su IPS sobre la japonesa. Se conservan los hitos.

---

## El método (`docs/PROMPT_METODO.md`)

Diario en `investigation.md`. **Las hipótesis falsas NO se borran**: se marcan
`[DESCARTADO]` y se explica por qué. Una medición → una causa → un arreglo →
una verificación. Prohibido escribir bytes a ciegas. Cada versión con
MD5/SHA-1/CRC32. Asserts con byte esperado, hueco libre y zonas intactas.
IPS contra la virgen con round-trip. `docs/PENDIENTES.md` es el registro único.
