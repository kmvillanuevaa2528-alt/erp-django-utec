# Sprint 1 Planning — ERP Django
## Semanas W04–W06 · Espiral 2: Modelado de Datos y ORM

**Sprint Goal:**
Al finalizar el Sprint 1, el ERP tendrá un esquema de base de datos
completo implementado en Django, con 8 entidades, relaciones verificadas,
panel admin funcional y una suite de ≥ 15 pruebas de modelo pasando.

**Duración:** W04 (diseño) · W05 (implementación) · W06 (validación + M2)

---

'@
$actual = [IO.File]::ReadAllText($p)
[IO.File]::WriteAllText($p, $cabecera + $actual, $enc)
## Sprint 1 — Estado final W06

| Tarea | Estado |
|---|---|
| Diseño ER + aprobación | ✅ W04 |
| Implementar models.py × 6 apps | ✅ W05 |
| makemigrations 0001_initial + migrate | ✅ W05 |
| Registrar admin.py | ✅ W05 |
| clean() en Producto, DetalleVenta, Pedido | ✅ W06 |
| Migración 0002_validators_pedido | ✅ W06 |
| Instalar y configurar django-jazzmin | ✅ W06 |
| Suite 15+ tests de modelo | ✅ W06 (17 tests) |

## Hito M2 — ALCANZADO ✅
- showmigrations: [X] en 5 apps (0001 + 0002)
- Tests: Ran 66 tests → OK
- Admin: 8 modelos con Jazzmin
- URL producción: https://erp-django-utec.onrender.com/admin/
- Fecha: ___/___/_____
