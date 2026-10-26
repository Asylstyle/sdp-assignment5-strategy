package calculator;

/** No test library needed: failures throw AssertionError and exit nonzero. */
public final class CalculatorTest {
    private static int checks;

    private CalculatorTest() {
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator(new AddStrategy());
        equal(16, calculator.calculate(12, 4));
        equal(-5, calculator.calculate(-2, -3));
        equal(0, calculator.calculate(0, 0));
        equal(0.75, calculator.calculate(0.5, 0.25));

        calculator.setStrategy(new SubtractStrategy());
        equal(8, calculator.calculate(12, 4));
        equal(-8, calculator.calculate(4, 12));
        equal(1, calculator.calculate(-2, -3));

        calculator.setStrategy(new MultiplyStrategy());
        equal(48, calculator.calculate(12, 4));
        equal(-6, calculator.calculate(-2, 3));
        equal(0, calculator.calculate(0, 5));
        equal(0.125, calculator.calculate(0.5, 0.25));

        calculator.setStrategy(new AddStrategy());
        equal(16, calculator.calculate(12, 4));
        rejectsNull(() -> new Calculator(null));
        rejectsNull(() -> calculator.setStrategy(null));
        equal(16, calculator.calculate(12, 4));

        // A new implementation works without changing the context.
        calculator.setStrategy((left, right) -> Math.max(left, right));
        equal(12, calculator.calculate(12, 4));
        equal(-2, calculator.calculate(-2, -3));

        calculator.setStrategy(new AddStrategy());
        equal(Double.POSITIVE_INFINITY, calculator.calculate(Double.MAX_VALUE, Double.MAX_VALUE));
        equal(Double.NaN, calculator.calculate(Double.NaN, 1));
        System.out.println("PASS: " + checks + " core checks");
    }

    private static void equal(double expected, double actual) {
        if (Double.compare(expected, actual) != 0) {
            throw new AssertionError("Expected " + expected + ", got " + actual);
        }
        checks++;
    }

    private static void rejectsNull(Runnable action) {
        try {
            action.run();
        } catch (NullPointerException expected) {
            checks++;
            return;
        }
        throw new AssertionError("Expected NullPointerException");
    }
}
