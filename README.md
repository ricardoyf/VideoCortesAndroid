<!-- app-release:start -->
[**Descargar APK actual v1.12**](https://github.com/ricardoyf/VideoCortesAndroid/raw/refs/tags/v1.12/release-artifacts/v1.12/VideoCortes-v1.12.apk) · [SHA-256](https://github.com/ricardoyf/VideoCortesAndroid/raw/refs/tags/v1.12/release-artifacts/v1.12/VideoCortes-v1.12.apk.sha256)

Versión objetivo conservada: [v1.11](https://github.com/ricardoyf/VideoCortesAndroid/releases/tag/v1.11).

`49fdc4010c46430965fc7c50326755684338a3c61b25e0ddb9305982fb795077`
<!-- app-release:end -->

# VideoCortes

APK Android para recortar videos con flujo rapido tipo LosslessCut:
P reproducir, I inicio, O final, E exportar y N siguiente.

Version 1.13:
- Al exportar cortes se conserva la extension original del video de entrada, por ejemplo `.MOV` en videos de iPhone.

Version 1.12:
- Ver LLC usa la misma prioridad de fechas que Carrusel: fecha en nombre tipo `202607...`, luego carpeta ano/mes y al final fecha de Android.
- Evita que cortes renombrados/modificados en agosto entren en agosto si el nombre indica julio.

Version 1.11:
- El rango de Ver LLC usa selectores tipo rueda para ano, mes y dia en fecha inicial y final.
- El filtro por fecha vuelve a ser estricto: solo reproduce fragmentos cuya fecha real de modificacion cae dentro del intervalo elegido.

Version 1.10:
- El rango de Ver LLC usa deslizadores separados de ano, mes y dia para fecha inicial y final.
- Es mas rapido para moverse por colecciones de mas de 10 anos.

Version 1.9:
- El rango de Ver LLC se elige con selectores moviles de fecha para ano, mes y dia, sin escribir texto.
- Los fragmentos editados sin fecha de modificacion disponible en Android no se descartan por error.

Version 1.8:
- Ver LLC incluye tambien fragmentos exportados por LosslessCut PC con rangos de tiempo en el nombre, por ejemplo `video-00.01.40.319-00.01.45.716-seg3.mp4`.
- La lista normal de trabajo omite tanto esos fragmentos editados como sus originales relacionados cuando estan en la misma carpeta.
- Se admiten tambien extensiones `.MTS` y `.M2TS`.

Version 1.7:
- Nuevo boton Ver LLC para reproducir cortes ya exportados.
- Pide fecha inicial y fecha final, busca recursivamente en la carpeta de trabajo, filtra archivos `-LLC-` por fecha de modificacion y los reproduce seguidos ordenados por nombre de archivo.

Version 1.6:
- Barra de desplazamiento manual para revisar libremente el video antes de exportar.
- La barra visual de segmentos tambien permite tocar/arrastrar para saltar a cualquier punto.

Version 1.5:
- Reproductor integrado con PlayerView oficial de Media3, mas parecido a Just Player internamente.
- Evita enganchar ExoPlayer a mano a TextureView.

Version 1.4:
- Reproductor real con AndroidX Media3/ExoPlayer, video fluido y audio.
- Mantiene la barra de segmentos y la exportacion rapida que ya funcionaba.

Version 1.3:
- Visor propio por fotogramas con MediaMetadataRetriever para evitar pantalla negra cuando el reproductor nativo no pinta el video.
- El boton P avanza la vista previa visual; I/O/E siguen usando esos tiempos para exportar.

Version 1.2:
- Reproduccion con SurfaceView + MediaPlayer para arrancar de forma mas estable.
- Version visible en una esquina de la aplicacion.

Version 1.1:
- Reproduccion con TextureView + MediaPlayer, descartada en v1.2 por arranque inestable en el movil.
- Selector Videos con miniaturas y orden por fecha, primero los mas recientes.
- Barra inferior de segmentos: I marca inicio, O anade segmento, E exporta todos los segmentos del video actual.

Los cortes se guardan como `nombre-LLC-00.00.00.000-00.00.10.000` conservando la extension original.
Al reabrir la app se omiten los originales que ya tengan cortes editados con rangos de tiempo en el nombre
o marcador `_MALO.txt`.
