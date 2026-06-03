# Equivalence Classes Mapping

Este documento mapea las clases de equivalencia y valores límite del dominio de `DriverLicense` a los tests existentes en la suite.

- **Edad negativa**: excepción
  - Test: `shouldThrowExceptionWhenAgeIsNegative` ([src/test/java/com/unisabana/domain/DriverLicenseTest.java](src/test/java/com/unisabana/domain/DriverLicenseTest.java))

- **Edad no realista (>150)**: excepción
  - Test: `shouldThrowExceptionWhenAgeIsUnrealistic` ([src/test/java/com/unisabana/domain/DriverLicenseTest.java](src/test/java/com/unisabana/domain/DriverLicenseTest.java))

- **Menores de 16 (TOO_YOUNG)**: rechazados
  - Test: `shouldRejectChildrenUnder16` (valores 0,5,10,15)

- **Adolescentes 16-17 (ADOLESCENT)**: licencia restringida
  - Test: `shouldAllowRestrictedLicenseForAdolescents` (16,17)

- **Jóvenes 18-22 (YOUNG_ADULT)**: licencia regular permitida
  - Test: `shouldAllowYoungAdults` (18..22)

- **Adultos 23-64 (ADULT)**: licencia regular y servicio público
  - Test: `shouldAllowFullLicenseAdults` (23,30,40,64)

- **Seniors 65-80 (SENIOR)**: licencia permitida con renovación
  - Test: `shouldAllowSeniorsWithRenewal` (65,70,75,80)

- **Mayores de 80 (TOO_OLD)**: rechazados
  - Test: `shouldRejectOver80Years` (81,90,100)

- **Discapacidad visual severa**: rechazado
  - Test: `shouldRejectWithSevereEyeDisability`

- **Sin discapacidad visual severa**: pasa la comprobación visual
  - Test: `shouldApproveWithoutEyeDisability`

- **Discapacidad auditiva**: permitida (con adaptaciones)
  - Test: `shouldAllowHearingDisability`

- **Antecedentes penales negativos (valor negativo)**: excepción
  - Test: `shouldThrowExceptionWhenNegativeRecords`

- **Antecedentes penales 0 (clean)**: aprobado
  - Test: `shouldApproveCleanRecord`

- **Antecedentes penales >=1 (serios)**: rechazado
  - Test: `shouldRejectWithCriminalRecords`

- **Documento vacío**: excepción
  - Test: `shouldThrowExceptionWhenDocumentEmpty`

- **Tipo de licencia inválido**: excepción
  - Test: `shouldThrowExceptionWhenInvalidLicenseType`

- **Tipos válidos**: `REGULAR`, `PUBLIC_SERVICE`
  - Test: `shouldAcceptValidLicenseTypes`

- **Aprobación de licencia para elegibles**
  - Test: `shouldApproveLicense`

- **Aprobar ineligible lanza excepción**
  - Test: `shouldThrowExceptionWhenApprovingIneligible`

- **Suspender y reactivar licencia**
  - Test: `shouldSuspendAndReactivate`

- **Persistencia de razón de rechazo**
  - Test: `shouldStoreRejectionReasonWhenRejected`


Siguientes pasos recomendados:
- Añadir enlaces directos a líneas de test si se requiere trazabilidad más fina.
- Generar tabla con cobertura por clase para verificar ausencia de clases no cubiertas.
# Clases de Equivalencia y Valores Límite (DriverLicense)

Este documento mapea las clases de equivalencia identificadas para `DriverLicense`, los valores límite y los tests que las cubren.

## Clases de Equivalencia

| Clase | Rango / regla | Test representativo | Justificación |
|-------|---------------|---------------------|---------------|
| TOO_YOUNG | Edad &lt; 16 | `shouldRejectChildrenUnder16` | No apto para licencia regular. |
| ADOLESCENT | 16-17 | `shouldAllowRestrictedLicenseForAdolescents` | Adolescente con licencia restringida. |
| YOUNG_ADULT | 18-22 | `shouldAllowYoungAdults` | Mayoría de edad para licencia regular, no servicio público. |
| ADULT | 23-64 | `shouldAllowFullLicenseAdults` | Elegible para servicio público y regular. |
| SENIOR | 65-80 | `shouldAllowSeniorsWithRenewal` | Renovación necesaria, aún elegible. |
| TOO_OLD | Edad &gt; 80 | `shouldRejectOver80Years` | Excede edad máxima legal para otorgamiento.

## Valores Límite (boundary values)

| Límite | Valor | Test | Por qué es importante |
|-------:|:-----:|------|----------------------|
| Justo antes mínima regular | 15 | `boundaryValue_Age15` | Transición a ineligible. |
| Mínimo regular | 16 | `boundaryValue_Age16` | Inicio de permiso restringido. |
| Justo antes servicio público | 22 | `boundaryValue_Age22` | Requisito público no cumplido. |
| Mínimo servicio público | 23 | `boundaryValue_Age23` | Inicio elegibilidad pública. |
| Máximo permitido | 80 | `boundaryValue_Age80` | Última edad válida sin denegación. |
| Justo después máximo | 81 | `boundaryValue_Age81` | Denegación por edad.

## Observaciones
- Cada clase está enlazada a tests en `src/test/java/com/unisabana/domain/DriverLicenseTest.java`.
- Las pruebas parametrizadas cubren varios valores dentro de cada clase, cumpliendo el requisito de ≥5 clases de equivalencia.
