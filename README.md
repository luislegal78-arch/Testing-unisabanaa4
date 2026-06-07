# Testing Workshop - Universidad de Sabana

## 📋 Descripción del Proyecto

**Dominio**: Elegibilidad para Licencias de Conducción (`DriverLicense`)  
**Objetivo**: Aplicar TDD, BDD, AAA, clases de equivalencia y cobertura de código  
**Última actualización**: Junio 2026  
**Estado**: En desarrollo

## 👥 Integrantes

- Luis Eduardo Gonzalez Mejia

---

## 📁 Estructura del Proyecto

```
Testing-unisabanaa4/
│
├── 📂 src/
│   ├── 📂 main/java/com/unisabana/domain/
│   │   └── DriverLicense.java                    # Clase de dominio principal
│   │
│   └── 📂 test/java/com/unisabana/domain/
│       └── DriverLicenseTest.java                # Suite completa de pruebas
│
├── 📄 pom.xml                                     # Configuración Maven + Dependencias
├── 📄 README.md                                   # Este archivo
├── 📄 Equivalence-Classes.md                      # Mapeo de clases de equivalencia
├── 📄 BDD-Scenarios.md                            # Escenarios Given-When-Then
├── 📄 Results.md                                  # Resultados de cobertura JaCoCo
├── 📄 TDD-HISTORY.md                              # Ciclos Red-Green-Refactor
├── 📄 defectos.md                                 # Análisis de defectos identificados
├── 📄 integrantes.txt                             # Información del equipo
├── 📂 docs/                                       # Documentación adicional y capturas
├── 📂 tools/                                      # Utilidades y scripts
└── 📂 target/                                     # Artefactos compilados (generado)
    └── 📂 site/jacoco/                            # Reportes de cobertura HTML
```

---

## 🚀 Cómo Ejecutar

### Compilar y ejecutar pruebas
```bash
mvn clean test
```

### Generar reporte de cobertura JaCoCo
```bash
mvn clean test jacoco:report
```
El reporte se generará en `target/site/jacoco/index.html`

### Verificar cobertura mínima (80%)
```bash
mvn verify
```

### Ejecutar un test específico
```bash
mvn -Dtest=DriverLicenseTest#shouldRejectChildrenUnder16 test
```

### Extraer métricas de cobertura (PowerShell)
```powershell
[xml]$jc = Get-Content target/site/jacoco/jacoco.xml
$line = $jc.report.counter | Where-Object { $_.type -eq 'LINE' }
$pct = [math]::Round(($line.covered / ($line.covered + $line.missed)) * 100, 2)
"Cobertura LINE: $pct% ($($line.covered)/$($line.covered + $line.missed))"
```

---

## 📊 Métricas de Cobertura

### Resumen General

| Métrica | Valor | Estado |
|:-------:|:-----:|:------:|
| **Cobertura de Líneas** | 84.95% | ✅ Cumple (≥80%) |
| **Cobertura de Instrucciones** | 87.50% | ✅ Cumple (≥80%) |
| **Líneas Cubiertas** | 79 / 93 | ✅ OK |
| **Líneas No Cubiertas** | 14 / 93 | ⚠️ Identificadas |
| **Ramas Cubiertas** | 58 / 76 | ✅ OK |

### Desglose por Paquete

| Paquete | Instrucciones | Líneas | Estado |
|---------|:-------------:|:------:|:------:|
| `com.unisabana.domain` | 287/328 (87.50%) | 79/93 (84.95%) | ✅ Pass |

### Desglose por Clase

| Clase | Instrucciones | Líneas | Ramas | Estado |
|-------|:-------------:|:------:|:-----:|:------:|
| `DriverLicense` | 287/328 | 79/93 | 58/76 | ✅ Pass |

### Líneas No Cubiertas

Las 14 líneas sin cubrir corresponden a:
- Ramas de manejo de excepciones (edge cases específicos)
- Algunos mensajes de rechazo alternativos
- Estados condicionales en flujos secundarios

Para ver las líneas exactas:
1. Ejecuta: `mvn clean test jacoco:report`
2. Abre: `target/site/jacoco/index.html`
3. Navega a: `com.unisabana.domain` → `DriverLicense` → "Source"
4. Las líneas no cubiertas aparecen en rojo

---

## 📚 Clases de Equivalencia Cubiertas

| Clase | Rango | Valores Probados | Test Representativo |
|:-----:|:-----:|:----------------:|:-------------------:|
| **TOO_YOUNG** | < 16 | 0, 5, 10, 15 | `shouldRejectChildrenUnder16` |
| **ADOLESCENT** | 16–17 | 16, 17 | `shouldAllowRestrictedLicenseForAdolescents` |
| **YOUNG_ADULT** | 18–22 | 18, 20, 22 | `shouldAllowYoungAdults` |
| **ADULT** | 23–64 | 23, 30, 40, 64 | `shouldAllowFullLicenseAdults` |
| **SENIOR** | 65–80 | 65, 70, 75, 80 | `shouldAllowSeniorsWithRenewal` |
| **TOO_OLD** | > 80 | 81, 90, 100 | `shouldRejectOver80Years` |

---

## 🎯 Valores Límite Identificados

| Límite | Valor | Test | Justificación |
|:------:|:-----:|:----:|:-------------:|
| Justo antes mínima regular | **15** | `boundaryValue_Age15` | Transición a ineligible |
| Mínimo para licencia restringida | **16** | `boundaryValue_Age16` | Inicio de permiso restringido |
| Justo antes servicio público | **22** | `boundaryValue_Age22` | Requisito público no cumplido |
| Mínimo para servicio público | **23** | `boundaryValue_Age23` | Inicio elegibilidad pública |
| Máximo permitido | **80** | `boundaryValue_Age80` | Última edad válida |
| Justo después máximo | **81** | `boundaryValue_Age81` | Denegación por edad |

---

## 🏗️ Patrón AAA (Arrange-Act-Assert)

Todos los tests siguen esta estructura. Ejemplo aplicado a `DriverLicense`:

```java
@Test
@DisplayName("Should retrieve driver attributes correctly")
void shouldRetrieveAllAttributes() {
    // ARRANGE: Preparar datos de prueba
    DriverLicense person = new DriverLicense(
        "1001", 
        "Juan Pérez García", 
        25, 
        false,      // severeEyeDisability
        false,      // hearingDisability
        0,          // criminalRecords
        "REGULAR"   // licenseType
    );

    // ACT: Obtener atributos
    String name = person.getFullName();

    // ASSERT: Verificar el resultado esperado
    assertThat(name).isEqualTo("Juan Pérez García");
}
```

---

## 🔄 BDD: Escenarios Given-When-Then

Los tests siguen el estilo Given–When–Then en su descripción:

```java
@Test
@DisplayName("Given a 22-year-old When applying for public service license Then should be rejected")
void shouldRejectPublicServiceUnder23() {
    // Given
    DriverLicense youngDriver = new DriverLicense(
        "1", 
        "Young", 
        22, 
        false, 
        false, 
        0, 
        "PUBLIC_SERVICE"
    );
    
    // When
    boolean isEligible = youngDriver.isEligibleForLicense();
    
    // Then
    assertThat(isEligible).isFalse();
}
```

### Escenarios BDD Clave

| Escenario | Condición | Resultado Esperado |
|:----------|:----------|:------------------:|
| Solicitante 15 años | Solicita licencia regular | ❌ Rechazado |
| Solicitante 16 años | Solicita licencia restringida | ✅ Aceptado con restricción |
| Solicitante 22 años | Solicita servicio público | ❌ Rechazado (edad mínima 23) |
| Solicitante 70 años | Solicita renovación | ⚠️ Verificación médica requerida |
| Discapacidad visual severa | Solicita licencia | ❌ Rechazado |
| Antecedentes penales ≥1 | Solicita licencia | ❌ Rechazado |

---

## 📋 Matriz de Cobertura TDD

| Aspecto | Cobertura | Notas |
|:-------:|:---------:|:-----:|
| **Clases de Equivalencia** | 6 / 6 | ✅ 100% |
| **Valores Límite** | 6 / 6 | ✅ 100% |
| **Caminos Principales** | 95%+ | ✅ OK |
| **Manejo de Excepciones** | 90%+ | ✅ OK |
| **Edge Cases** | ~85% | ⚠️ 14 líneas sin cubrir |

---

## 🔧 Tecnologías y Dependencias

| Tecnología | Versión | Propósito |
|:-----------|:-------:|:---------:|
| **Java** | 11+ | Lenguaje base |
| **Maven** | 3.6+ | Gestor de dependencias |
| **JUnit 5** | 5.9.2 | Framework de testing |
| **AssertJ** | 3.24.1 | Assertions fluidas |
| **JaCoCo** | 0.8.8 | Cobertura de código |
| **Maven Surefire** | 3.1.2 | Test runner |

---

## 📖 Documentación Complementaria

Para la documentación completa del taller, consulte los siguientes archivos en el repositorio:

| Documento | Contenido |
|:----------|:----------|
| **[Equivalence-Classes.md](Equivalence-Classes.md)** | Mapeo detallado de clases de equivalencia y valores límite |
| **[BDD-Scenarios.md](BDD-Scenarios.md)** | Escenarios Given-When-Then |
| **[Results.md](Results.md)** | Resultados detallados de cobertura JaCoCo |
| **[TDD-HISTORY.md](TDD-HISTORY.md)** | Ciclos Red-Green-Refactor del desarrollo |
| **[defectos.md](defectos.md)** | Análisis de defectos identificados y resueltos |
| **[Wiki del Repositorio](https://github.com/luislegal78-arch/Testing-unisabanaa4/wiki)** | Documentación oficial del taller |

---

## 📊 Reportes Disponibles

### JaCoCo
```
target/site/jacoco/index.html              # Reporte HTML de cobertura
target/site/jacoco/jacoco.xml              # Reporte XML para parseo
target/site/jacoco/jacoco.csv              # Reporte CSV con métricas
```

### Surefire (Test Execution)
```
target/surefire-reports/
├── TEST-com.unisabana.domain.DriverLicenseTest.xml
├── TEST-com.unisabana.domain.DriverLicenseTest.txt
└── ... (otros reportes)
```

---

## ✨ Convenciones del Proyecto

### Nomenclatura de Tests
```
should<ExpectedBehavior>When<Condition>
```

Ejemplos:
- `shouldRejectChildrenUnder16`
- `shouldAllowRestrictedLicenseForAdolescents`
- `shouldThrowExceptionWhenAgeIsNegative`

### Estructura de Clases
- **Lógica de negocio**: `src/main/java/com/unisabana/domain/`
- **Tests**: `src/test/java/com/unisabana/domain/`
- **Configuración**: `pom.xml`

### Requisitos de Cobertura
- ✅ Mínimo: **80%** de líneas cubiertas
- ✅ Objetivo: **85%+** para producción
- ✅ Todas las clases de equivalencia cubiertas
- ✅ Todos los valores límite probados

---

## 🛠️ Comandos Útiles

```bash
# Compilar proyecto
mvn compile

# Ejecutar todos los tests
mvn clean test

# Ejecutar un test específico
mvn -Dtest=DriverLicenseTest#shouldRejectChildrenUnder16 test

# Generar reporte JaCoCo
mvn clean test jacoco:report

# Verificar cobertura mínima
mvn verify

# Limpiar artefactos compilados
mvn clean

# Ver información del proyecto
mvn help:describe -Dartifact=org.jacoco:jacoco-maven-plugin
```

---

## 📝 Notas Importantes

- ✅ El proyecto es **100% compilable**: `mvn clean test` sin pasos adicionales
- ✅ Cobertura objetivo: **≥ 80%** (actualmente **84.95%**)
- ✅ Todos los tests siguen nomenclatura estándar: `should<X>When<Y>()`
- ✅ Documentación oficial disponible en el Wiki del repositorio
- ✅ Reporte JaCoCo actualizado en cada ejecución de tests
- ⚠️ 14 líneas sin cubrir corresponden a edge cases opcionales

---

## 📞 Soporte y Contacto

Para preguntas sobre el proyecto:
- Revisar la [documentación en el Wiki](https://github.com/luislegal78-arch/Testing-unisabanaa4/wiki)
- Consultar los archivos `*.md` en la raíz del repositorio
- Abrir un issue en el repositorio

---

**Versión**: 1.0.0  
**Última actualización**: Junio 2026  
**Licencia**: Universidad de Sabana
