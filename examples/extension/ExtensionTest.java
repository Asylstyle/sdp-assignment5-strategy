package extension;

import calculator.Calculator;

public final class ExtensionTest {
    private ExtensionTest() {
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator(new DivideStrategy());
        check(3.0, calculator.calculate(12, 4));
        check(-3.0, calculator.calculate(-12, 4));
        check(0.25, calculator.calculate(1, 4));
        check(0.0, calculator.calculate(0, 4));
        rejectsZero(calculator, 0.0);
        rejectsZero(calculator, -0.0);
        System.out.println("PASS: 6 extension checks");
    }

    private static void check(double expected, double actual) {
        if (Double.compare(expected, actual) != 0) {
            throw new AssertionError("Expected " + expected + ", got " + actual);
        }
    }

    private static void rejectsZero(Calculator calculator, double divisor) {
        try {
            calculator.calculate(1, divisor);
        } catch (ArithmeticException expected) {
            return;
        }
        throw new AssertionError("Expected ArithmeticException");
    }
}
