package extension;

import calculator.AddStrategy;
import calculator.Calculator;

public final class ExtensionClient {
    private ExtensionClient() {
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator(new AddStrategy());
        System.out.println("Add: 12 + 4 = " + calculator.calculate(12, 4));
        calculator.setStrategy(new DivideStrategy());
        System.out.println("Divide: 12 / 4 = " + calculator.calculate(12, 4));
    }
}
