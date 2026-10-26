package calculator;

/** A replaceable algorithm for a calculation with two operands. */
public interface OperationStrategy {
    double execute(double left, double right);
}
