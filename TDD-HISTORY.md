# TDD History (Ejercicio DriverLicense)

Este archivo documenta tres ciclos de TDD (RED → GREEN → REFACTOR) representativos realizados durante el desarrollo de `DriverLicense`.

## Ciclo 1 — Validación de edad mínima
- RED: `shouldRejectChildrenUnder16` (añadido) — falla porque no existía la validación.
- GREEN: Implementación mínima en `DriverLicense` para devolver `TOO_YOUNG` y `isAdultForRegularLicense()` true/false.
- REFACTOR: Extraer constantes `MIN_AGE`, `MAX_AGE` y reorganizar categorías de edad.

## Ciclo 2 — Licencia de servicio público (mínimo 23 años)
- RED: `shouldRejectPublicServiceUnder23` (añadido) — prueba muestra rechazo para 22 años.
- GREEN: Implementación del método `isAdultForPublicService()` y `yearsUntilPublicService()`.
- REFACTOR: Consolidar lógica de umbrales en métodos reutilizables y añadir tests parametrizados.

## Ciclo 3 — Persistencia de razón de rechazo
- RED: `shouldStoreRejectionReasonWhenRejected` (añadido) — prueba espera que `rejectLicense("motivo")` almacene la razón.
- GREEN: Añadida la propiedad `rejectionReason`, actualización de `rejectLicense(String)` y `getRejectionReason()`.
- REFACTOR: Ajuste de mensajes por defecto en `getRejectionReason()` y actualización de `defectos.md` (DEF-006: CERRADO).

---
Notas: Para evidencia de TDD real, se recomienda crear la rama `tdd-evidence` con commits separados:
1. RED — solo el test (fallando)
2. GREEN — cambio mínimo para pasar el test
3. REFACTOR — mejoras de diseño sin cambiar comportamiento
# Historia TDD

Este documento documenta 3 ciclos Rojo → Verde → Refactor realizados durante el desarrollo de `DriverLicense`.

## Iteración 1: Validación de Edad Mínima
- **Rojo (test)**: `shouldRejectChildrenUnder16` — se añade test que falla para edad 15.
- **Verde (implementación mínima)**: validar edad mínima en constructor e `isAdultForRegularLicense()`.
- **Refactor**: extraer constantes `MIN_AGE_REGULAR` y `MAX_AGE` a variables estáticas.

Commits de ejemplo:
- `test: add shouldRejectChildrenUnder16 (RED)`
- `feat: implement min age check (GREEN)`
- `refactor: extract MIN_AGE and MAX_AGE constants (REFACTOR)`

## Iteración 2: Licencia de Servicio Público (mínimo 23 años)
- **Rojo (test)**: `shouldRejectPublicServiceUnder23` — nuevo test parametrizado para 22 años.
- **Verde**: implementar `isAdultForPublicService()` y `yearsUntilPublicService()` y validar en `isEligibleForLicense()`.
- **Refactor**: consolidar lógica de edad en `isAgeValidForLicenseType()`.

Commits de ejemplo:
- `test: add shouldRejectPublicServiceUnder23 (RED)`
- `feat: add public service age validation (GREEN)`
- `refactor: move license age rules to helper (REFACTOR)`

## Iteración 3: Discapacidad Visual y Antecedentes
- **Rojo (test)**: `shouldRejectWithSevereEyeDisability` y `shouldRejectWithCriminalRecords`.
- **Verde**: negar elegibilidad si `hasSevereEyeDisability` o `seriousCriminalRecords > 0`.
- **Refactor**: crear `hasCleanCriminalRecord()` y `canDriveWithEyeDisability()` helpers.

Commits de ejemplo:
- `test: add shouldRejectWithSevereEyeDisability (RED)`
- `feat: deny license for severe eye disability and criminal records (GREEN)`
- `refactor: extract health and record helpers (REFACTOR)`

---

Guardé estos ciclos como ejemplo de evidencias TDD; para evidencia de commits reales, usar el histórico de Git.
