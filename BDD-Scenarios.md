# BDD Scenarios Mapping

Los escenarios BDD (Given/When/Then) del dominio `DriverLicense` y su mapeo a pruebas existentes.

- **Scenario: Rechazo por ser menor de edad**
  - Given: una persona con edad < 16
  - When: solicita licencia regular
  - Then: la solicitud es rechazada (`TOO_YOUNG`)
  - Test: `shouldRejectChildrenUnder16` — [src/test/java/com/unisabana/domain/DriverLicenseTest.java](src/test/java/com/unisabana/domain/DriverLicenseTest.java)

- **Scenario: Adolescente obtiene licencia restringida**
  - Given: edad 16-17
  - When: solicita licencia regular
  - Then: obtiene `ADOLESCENT` y puede conducir con restricciones
  - Test: `shouldAllowRestrictedLicenseForAdolescents`

- **Scenario: Servicio público requiere 23 años**
  - Given: persona de 22 años
  - When: solicita licencia de servicio público
  - Then: es rechazada y `yearsUntilPublicService()` devuelve 1
  - Test: `shouldRejectPublicServiceUnder23`

- **Scenario: Discapacidad visual severa impide licencia**
  - Given: persona con discapacidad visual severa
  - When: valida elegibilidad
  - Then: rechazada por visión
  - Test: `shouldRejectWithSevereEyeDisability`

- **Scenario: Antecedentes penales impiden licencia**
  - Given: persona con 1 o más antecedentes graves
  - When: solicita licencia
  - Then: rechazado por antecedentes
  - Test: `shouldRejectWithCriminalRecords`

- **Scenario: Registrar razón de rechazo**
  - Given: persona rechazada por cualquier motivo
  - When: se invoca `rejectLicense("motivo")`
  - Then: `getRejectionReason()` contiene "motivo"
  - Test: `shouldStoreRejectionReasonWhenRejected`

Referencias: ver la suite completa en [src/test/java/com/unisabana/domain/DriverLicenseTest.java](src/test/java/com/unisabana/domain/DriverLicenseTest.java)
# Escenarios BDD (Given–When–Then) para DriverLicense

Lista de escenarios clave (mapeados a tests existentes):

- Given a 15-year-old When applying for regular license Then should be rejected
  - Test: `shouldRejectChildrenUnder16`

- Given a 16-year-old When applying for regular license Then restricted license allowed
  - Test: `shouldAllowRestrictedLicenseForAdolescents`

- Given a 22-year-old When applying for public service license Then should be rejected
  - Test: `shouldRejectPublicServiceUnder23`

- Given a 23-year-old When applying for public service license Then should be approved
  - Test: `shouldApprovePublicService23Years`

- Given a person with severe eye disability When checking eligibility Then should be rejected
  - Test: `shouldRejectWithSevereEyeDisability`

- Given a person with criminal records When checking eligibility Then should be rejected
  - Test: `shouldRejectWithCriminalRecords`

Cada escenario se formula en formato Given–When–Then dentro del `@DisplayName` del test correspondiente.
