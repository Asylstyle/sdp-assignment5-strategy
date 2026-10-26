# Assignment 5 — Strategy Pattern

Option B: a small Java 17 calculator. No frameworks or external dependencies.

## Build and run

From the repository root with JDK 17 on PATH (PowerShell, cmd, or a POSIX shell):

```text
javac --release 17 -d out src/main/java/calculator/*.java src/test/java/calculator/*.java
java -cp out calculator.Client
java -cp out calculator.CalculatorTest
```

Expected demo: Add **16.0**, Subtract **8.0**, Multiply **48.0**.
The same Calculator switches strategy at runtime.

## Structure

- `src/main/java/calculator/`: interface, context, three strategies, client
- `src/test/java/calculator/`: dependency-free regression tests
- `examples/extension/`: a fourth strategy and a separate client
- [REPORT.md](REPORT.md): complete technical report and UML
- [DEFENSE_RU.md](DEFENSE_RU.md): short Russian defense walkthrough

## Add a strategy without changing existing classes

The extension adds division in its own package. Compile and run it after the core build:

```text
javac --release 17 -cp out -d out examples/extension/*.java
java -cp out extension.ExtensionClient
```

Implement `OperationStrategy.execute`, then select that implementation in a client.
No edits to Calculator, existing strategies, or the original Client are required.


