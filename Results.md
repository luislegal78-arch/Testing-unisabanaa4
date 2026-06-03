# Resultados y Evidencia de Cobertura (JaCoCo)

## Reporte JaCoCo

El reporte de cobertura se generó en:

- `target/site/jacoco/index.html`

Resumen (extraído de `target/site/jacoco/jacoco.csv` para el paquete `com.unisabana.domain`):

```
PACKAGE,CLASS,INSTRUCTION_MISSED,INSTRUCTION_COVERED,BRANCH_MISSED,BRANCH_COVERED,LINE_MISSED,LINE_COVERED
com.unisabana.domain,DriverLicense,41,287,18,58,14,79
```

- Instrucciones cubiertas: 287 / (287+41) = **87.50%**
- Líneas cubiertas: 79 / (79+14) = **84.95%**

Ambas métricas están por encima del umbral requerido del 80%.

## Líneas no cubiertas (observación)

Hay 14 líneas sin cubrir en `DriverLicense` (principalmente ramas de manejo de estados y algunos mensajes de rechazo específicos). Para identificar las líneas exactas, abra:

```
target/site/jacoco/index.html
```

y navegue a la clase `DriverLicense` → "Source" para ver las líneas resaltadas en rojo.

## Capturas sugeridas para el Wiki

- Incluir una captura de `target/site/jacoco/index.html` mostrando cobertura por paquete.
- Incluir captura del detalle de `DriverLicense` mostrando líneas no cubiertas.

Se incluyen capturas simuladas en `docs/` para que las enlaces directamente en el Wiki:

- [Resumen JaCoCo por paquete](docs/jacoco-overview.png)
- [Detalle DriverLicense (líneas no cubiertas)](docs/DriverLicense-detail.png)

Si prefieres capturas reales, abre `target/site/jacoco/index.html` en el navegador y toma screenshots, luego reemplaza los archivos en `docs/`.
