# Testing Workshop - Universidad de Sabana

## Descripción del Proyecto

**Dominio**: Elegibilidad para Licencias de Conducción (`DriverLicense`)
**Objetivo**: Aplicar TDD, BDD, AAA, clases de equivalencia y cobertura de código

## Integrantes

- Luis Eduardo Gonzalez Mejia

## Contenido del Wiki

Para la documentación completa del taller, consulte el **[Wiki del Repositorio](https://github.com/LEGM121/testing-unisabana/wiki)**.

### Secciones del Wiki:

1. **[Inicio](https://github.com/LEGM121/testing-unisabana/wiki)** - Dominio, alcance y equipo
2. **[TDD: Red-Green-Refactor](https://github.com/LEGM121/testing-unisabana/wiki/TDD-History)** - 3+ iteraciones
3. **[Patrón AAA](https://github.com/LEGM121/testing-unisabana/wiki/AAA-Pattern)** - Arrange-Act-Assert
4. **[Clases de Equivalencia](https://github.com/LEGM121/testing-unisabana/wiki/Equivalence-Classes)** - Tabla y justificación
5. **[BDD: Given-When-Then](BDD-Scenarios.md)** - Escenarios
6. **[Resultados](Results.md)** - JaCoCo y conclusiones
7. **[TDD History](TDD-HISTORY.md)** - Ciclos Rojo/Verde/Refactor
7. **[Defectos](https://github.com/LEGM121/testing-unisabana/wiki/Defects)** - Análisis de defectos

## Cómo Ejecutar

### Compilar y ejecutar pruebas:
```bash
mvn clean test
```

### Generar reporte de cobertura:
```bash
mvn clean test jacoco:report
```

El reporte se generará en `target/site/jacoco/index.html`

### Verificar cobertura mínima:
```bash
mvn verify
```

## Estructura del Proyecto

```
testing-unisabana/
├── src/
│   ├── main/java/
│   │   └── com/unisabana/domain/
│   │       └── DriverLicense.java     # Clase de dominio principal
│   └── test/java/
│       └── com/unisabana/domain/
│           └── DriverLicenseTest.java # Suite de pruebas
├── pom.xml                            # Configuración Maven + JaCoCo
├── .gitignore                         # Exclusiones Git
├── integrantes.txt                    # Información del equipo
└── README.md                          # Este archivo
```

## Clases de Equivalencia Cubiertas (DriverLicense)

| Clase | Rango | Tests |
|-------|-------|-------|
| TOO_YOUNG | < 16 | `shouldRejectChildrenUnder16` |
| ADOLESCENT | 16-17 | `shouldAllowRestrictedLicenseForAdolescents` |
| YOUNG_ADULT | 18-22 | `shouldAllowYoungAdults` |
| ADULT | 23-64 | `shouldAllowFullLicenseAdults` |
| SENIOR | 65-80 | `shouldAllowSeniorsWithRenewal` |
| TOO_OLD | > 80 | `shouldRejectOver80Years` |

## Valores Límite Identificados

| Límite | Valor | Test | Justificación |
|--------|-------|------|---------------|
| Mayoría de edad | 18 | `boundaryValue_AgeEighteen` | Transición minor→adult |
| Justo antes mayoría | 17 | `boundaryValue_AgeSeventeen` | Último día menor |
| Jubilación | 65 | `boundaryValue_AgeSixtyfive` | Edad legal jubilación |
| Justo antes jubilación | 64 | `boundaryValue_AgeSixtyfour` | Último año activo |
| Cambio niño→adolescente | 13 | `boundaryValue_AgeThirteen` | Inicio adolescencia |
| Último año infantil | 12 | `boundaryValue_AgeEleven` | Fin infancia |

## Patrón AAA (Arrange-Act-Assert)

Todos los tests siguen la estructura. Ejemplo aplicado a `DriverLicense`:

```java
@Test
@DisplayName("Should retrieve driver attributes correctly")
void shouldRetrieveAllAttributes() {
    // ARRANGE: Preparar datos de prueba
    DriverLicense person = new DriverLicense("1001", "Juan Pérez García", 25, false, false, 0, "REGULAR");

    // ACT: Obtener atributos
    String name = person.getFullName();

    // ASSERT: Verificar el resultado esperado
    assertThat(name).isEqualTo("Juan Pérez García");
}
```

## BDD: Escenarios Given-When-Then

Los tests siguen el estilo Given–When–Then en su descripción. Ejemplo:

```java
@Test
@DisplayName("Given a 22-year-old When applying for public service license Then should be rejected (too young)")
void shouldRejectPublicServiceUnder23() {
    // Given
    DriverLicense youngDriver = new DriverLicense("1", "Young", 22, false, false, 0, "PUBLIC_SERVICE");
    // When
    boolean isEligible = youngDriver.isEligibleForLicense();
    // Then
    assertThat(isEligible).isFalse();
}
```

## Requisitos

- Java 11+
- Maven 3.6+
- JUnit 5
- AssertJ
- JaCoCo

## Notas

- El proyecto es totalmente compilable: `mvn clean test` sin pasos adicionales
- Cobertura objetivo: ≥ 80%
- Todos los tests siguen nomenclatura: `should<Expected>When<Condition>()`
- El Wiki contiene documentación oficial (no PDF)

---

**Última actualización**: Mayo 2026  
**Estado**: En desarrollo

## Pruebas locales y evidencia

### Ejecutar todas las pruebas
- Compilar y ejecutar todas las pruebas unitarias:

```powershell
mvn clean test
```

### Ejecutar un test específico (método)
- Ejecutar una sola clase o método de prueba (útil para reproducir un fallo):

```powershell
mvn -Dtest=DriverLicenseTest#shouldRejectChildrenUnder16 test
```

### Generar reporte de cobertura JaCoCo
- Generar el reporte HTML/CSV/XML (suponiendo JaCoCo configurado en `pom.xml`):

```powershell
mvn clean test jacoco:report
```

- Abrir el reporte en Windows:

```powershell
# desde la raíz del proyecto
Start-Process target\site\jacoco\index.html
# o en PowerShell: Invoke-Item target\site\jacoco\index.html
```

### Informes de ejecución (Surefire)
- Los informes de los tests están en `target/surefire-reports/` (TXT y XML). Ahí encontrará los logs de cada caso y el XML `TEST-*.xml` con el resumen.

### Capturar evidencias (PNG) del reporte JaCoCo
- Puede tomar una captura manual del `target/site/jacoco/index.html` o usar utilidades headless (Chrome/puppeteer) o el script del repo si existe:

```powershell
# ejemplo (si dispone de Python y el script):
# python tools/generate_png_captures.py target/site/jacoco

# ejemplo con Chrome headless (requiere path a Chrome/Chromium en PATH):
# chrome --headless --screenshot=jacoco.png --window-size=1200,900 file:///%CD%/target/site/jacoco/index.html
```

Incluya las PNG resultantes en `docs/` o en el README con rutas relativas para que GitHub las muestre.

### Extraer porcentaje de cobertura desde JaCoCo (PowerShell)
- Ejemplo rápido para leer el contador de líneas en `jacoco.xml`:

```powershell
[xml]$jc = Get-Content target/site/jacoco/jacoco.xml
$line = $jc.report.counter | Where-Object { $_.type -eq 'LINE' }
$pct = [math]::Round(($line.covered / ($line.covered + $line.missed)) * 100, 2)
"Cobertura LINE: $pct% ($($line.covered)/$($line.covered + $line.missed))"
```

## Clases de Equivalencia y Valores Límite (ejemplo resumido)
La siguiente tabla es un ejemplo aplicado al dominio `DriverLicense`. Adapte según sus reglas de negocio.

| Dominio | Clase de equivalencia | Rango / condición | Valor límite relevante |
|--------:|-----------------------|-------------------|------------------------|
| Edad | TOO_YOUNG (rechazo) | < 16 | 15 (borde) |
| Edad | ADOLESCENT (restringido) | 16-17 | 16, 17 |
| Edad | ADULT (completa) | 18-64 | 18 (borde inferior), 64 |
| Edad | SENIOR (condicional) | 65-80 | 65, 80 |
| Edad | TOO_OLD (rechazo) | > 80 | 81 (borde) |

Justificación de los bordes: los tests deben cubrir inmediatamente antes y después de cada umbral (p. ej. 15,16 y 17,18) para detectar errores en las comparaciones `>=`/`>`.

## Escenarios BDD clave (Given–When–Then)
- Given un solicitante de 15 años When solicita licencia Then debe ser rechazado.
- Given un solicitante de 16 años sin antecedentes When solicita licencia restringida Then debe ser aceptado con restricción.
- Given un solicitante de 22 años para licencia de servicio público When solicita licencia Then debe ser rechazado (edad mínima 23).
- Given un solicitante de 70 años con historial médico When solicita renovación Then aplicar verificación médica (condicional).

## Resultados y conclusiones técnicas
- Cobertura: abra `target/site/jacoco/index.html` y capture la métrica de `LINE`/`BRANCH` para el informe. Objetivo del taller: ≥ 80%.
- Fallos: revise `target/surefire-reports/TEST-*.xml` y los archivos `*.txt` para traza y excepciones.
- Recomendación: mantenga tests unitarios pequeños y deterministas; use mock/fake para dependencias externas; añada tests que cubran todos los bordes identificados en la tabla de equivalencia.

---

**Última actualización**: Junio 2026  
**Estado**: En desarrollo
