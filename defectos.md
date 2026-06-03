# Defectos Encontrados y Análisis

## Defecto #1: Validación de Edad Negativa (ARCHIVADO)

**ID**: DEF-001  
**Estado**: ARCHIVADO (clase `Registry` eliminada)  
**Severidad**: ALTA  

Nota: este defecto estaba documentado para la clase `Registry`; la clase fue eliminada del repositorio y las validaciones relevantes se migraron/validaron en otros artefactos. Mantengo el registro por trazabilidad.

---

## Defecto #2: Edad Máxima sin Límite

**ID**: DEF-002  
**Estado**: CERRADO  
**Severidad**: MEDIA  

### Descripción del Caso
Al crear un `Registry` con edad superior a 120 años (ej: 150), el sistema no rechaza.

### Resultado Esperado
`IllegalArgumentException` con mensaje: "La edad excede el máximo permitido: 120"

### Resultado Obtenido (ANTES)
Se permitían edades no realistas, comprometiendo la integridad del dominio.

### Causa Probable
Falta de límite máximo en la validación de edad.

### Solución Implementada
Se agregó validación de máximo en `validateAge()`:
```java
if (age > MAX_AGE) {
    throw new IllegalArgumentException("La edad excede el máximo permitido: " + MAX_AGE);
}
```

### Test que lo detecta
`RegistryTest.shouldThrowExceptionWhenAgeExceedsMaximum()`

---

## Defecto #3: Estado Civil Vacío sin Validación

**ID**: DEF-003  
**Estado**: CERRADO  
**Severidad**: MEDIA  

### Descripción del Caso
Al crear un `Registry` con estado civil vacío o null, no se valida.

### Resultado Esperado
`IllegalArgumentException` con mensaje: "El estado civil no puede estar vacío"

### Resultado Obtenido (ANTES)
Se permitía crear registros sin estado civil definido.

### Causa Probable
Falta de validación de string vacío/null en el constructor.

### Solución Implementada
Se agregó validación en `validateMaritalStatus()`:
```java
if (status == null || status.trim().isEmpty()) {
    throw new IllegalArgumentException("El estado civil no puede estar vacío");
}
```

### Test que lo detecta
`RegistryTest.shouldThrowExceptionWhenMaritalStatusIsEmpty()`

---

## Defecto #4: Estado Civil Inválido

**ID**: DEF-004  
**Estado**: CERRADO  
**Severidad**: MEDIA  

### Descripción del Caso
Se permite crear un `Registry` con estado civil no permitido (ej: "VIVO", "UNKNOWN").

### Resultado Esperado
`IllegalArgumentException` indicando estado civil inválido

### Resultado Obtenido (ANTES)
Se aceptaban valores arbitrarios de estado civil.

### Causa Probable
Falta de validación contra lista de estados permitidos.

### Solución Implementada
Se agregó validación con regex en `validateMaritalStatus()`:
```java
String validStatuses = "SINGLE|MARRIED|DIVORCED|WIDOWED";
if (!status.matches(validStatuses)) {
    throw new IllegalArgumentException("Estado civil inválido: " + status);
}
```

### Test que lo detecta
`RegistryTest.shouldThrowExceptionWhenMaritalStatusIsInvalid()`

---

## Defecto #5: Marcar Persona Fallecida Dos Veces (ARCHIVADO)

**ID**: DEF-005  
**Estado**: ARCHIVADO (clase `Registry` eliminada)  
**Severidad**: BAJA  

Nota: historial preservado. La clase `Registry` ya no forma parte del código activo.

---

## Nuevo Defecto #6: `rejectLicense` no persiste motivo de rechazo

**ID**: DEF-006  
**Estado**: ABIERTO  
**Severidad**: BAJA  

### Descripción del Caso
El método `rejectLicense(String reason)` asigna `status = "REJECTED"` pero no guarda ni expone la razón de rechazo.

### Resultado Esperado
La razón de rechazo debe guardarse en un campo (`rejectionReason`) y ser accesible mediante `getRejectionReason()` o similar.

### Resultado Obtenido
La razón no se almacena; `getRejectionReason()` actualmente es un diagnóstico calculado, no la razón pasada a `rejectLicense`.

### Causa Probable
Falta de atributo para persistir el motivo y de tests que verifiquen su almacenamiento.

### Prueba sugerida
Agregar un test: `shouldStoreRejectionReasonWhenRejected()` que invoque `rejectLicense("motivo")` y verifique `getRejectionReason()` contiene "motivo".

### Prioridad
Baja — funcionalidad recomendada para trazabilidad/UX.

### Estado de la corrección
**DEF-006: CERRADO** — Se implementó `rejectionReason` en `DriverLicense` y se agregó el test `shouldStoreRejectionReasonWhenRejected()`.

---

## Observación sobre cobertura JaCoCo
Ver `Results.md` para resumen del reporte de cobertura (`target/site/jacoco/index.html`).

---

## Resumen de Defectos

| ID | Descripción | Estado | Severidad | Test |
|-----|-------------|--------|-----------|------|
| DEF-001 | Edad negativa | ✅ CERRADO | ALTA | shouldThrowExceptionWhenAgeIsNegative |
| DEF-002 | Edad > 120 | ✅ CERRADO | MEDIA | shouldThrowExceptionWhenAgeExceedsMaximum |
| DEF-003 | Estado civil vacío | ✅ CERRADO | MEDIA | shouldThrowExceptionWhenMaritalStatusIsEmpty |
| DEF-004 | Estado civil inválido | ✅ CERRADO | MEDIA | shouldThrowExceptionWhenMaritalStatusIsInvalid |
| DEF-005 | Marcar muerto 2x | ✅ CERRADO | BAJA | shouldThrowExceptionWhenMarkingDeceasedTwice |

---

**Lecciones Aprendidas**:
- Los tests ayudaron a identificar falta de validaciones en el dominio
- La validación en el constructor es crítica para mantener invariantes del dominio
- Los casos límite frecuentemente revelan defectos en la lógica
