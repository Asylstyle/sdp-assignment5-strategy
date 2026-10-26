# Validation record

Validated locally on Windows on 2026-10-26 using official Eclipse Temurin
OpenJDK 17.0.20.1+1, downloaded as a portable archive and checksum verified.
No global Java installation or credentials were changed.

Compilation used --release 17 -Xlint:all -Werror for both the core and extension.

```text
Add: 12 + 4 = 16.0
Subtract: 12 - 4 = 8.0
Multiply: 12 * 4 = 48.0
PASS: 19 core checks
Add: 12 + 4 = 16.0
Divide: 12 / 4 = 3.0
PASS: 6 extension checks
```

The rendered UML PNG was visually inspected for readable compartments, exact
signatures, correct arrow directions and unclipped labels. Its SVG and editable
PlantUML model are included. Java CI repeats the compilation and execution on JDK 17.
