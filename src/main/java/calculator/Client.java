package calculator;

/** Client chooses algorithms; the same context is reused throughout the demo. */
public final class Client {
    private Client() {
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator(new AddStrategy());
        System.out.println("Add: 12 + 4 = " + calculator.calculate(12, 4));

        calculator.setStrategy(new SubtractStrategy());
        System.out.println("Subtract: 12 - 4 = " + calculator.calculate(12, 4));

        calculator.setStrategy(new MultiplyStrategy());
        System.out.println("Multiply: 12 * 4 = " + calculator.calculate(12, 4));
    }
}
