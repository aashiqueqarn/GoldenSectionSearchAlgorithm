import numpy as np
from sympy import symbols, sympify

class GoldenSearchAlgorithm:
    def __init__(self, boundary_a, boundary_b, uncertainty_interval, reciprocal_golden_ratio_d):
        self.boundary_a = boundary_a
        self.boundary_b = boundary_b
        self.uncertainty_interval = uncertainty_interval
        self.reciprocal_golden_ratio_d = reciprocal_golden_ratio_d

    @staticmethod
    def calculate_boundary_diff_l(boundary_a, boundary_b):
        return boundary_b - boundary_a

    @staticmethod
    def evaluate_equation(expression_string, symbol, symbol_value):
        expression_string = expression_string.replace('−', '-')
        expression_string = expression_string.replace('x', '*x')
        expression_string = expression_string.replace('**x', 'x')
        expression_string = expression_string.replace(' ', '')
        expression_string = expression_string.replace('x4', 'x**4')
        expression_string = expression_string.replace('x3', 'x**3')
        expression_string = expression_string.replace('x2', 'x**2')

        x = symbols(symbol)
        expression = sympify(expression_string)
        x_value = symbol_value
        result = expression.subs(x, x_value)
        return result

    def calculate_func(self, expression_equation, symbol):
        count = 0
        while self.calculate_boundary_diff_l(self.boundary_a, self.boundary_b) > self.uncertainty_interval:
            print("=" * 50)
            print("The iteration count is: ", count)
            count += 1
            x_1 = self.calculate_x_1(self.boundary_b, self.boundary_a)
            x_2 = self.calculate_x_2(self.boundary_a, self.boundary_b)
            print(f"The values are x1: {x_1} and x2: {x_2}")
            func_x_1 = self.evaluate_equation(expression_equation, symbol, x_1)
            func_x_2 = self.evaluate_equation(expression_equation, symbol, x_2)
            print(f"The function value for func_x1: {func_x_1}")
            print(f"The function value for func_x2: {func_x_2}")
            if func_x_1 > func_x_2:
                self.boundary_a = x_1
                self.boundary_b = self.boundary_b
                print("Functon func_x_1 is greater then func_x_2")
            else:
                self.boundary_b = x_2
                self.boundary_a = self.boundary_a
                print("Functon func_x_1 is less then func_x_2")

            print(f"The updated boundary [a, b]: [{self.boundary_a}, {self.boundary_b}]")
            print(f"The boundary difference L: {self.calculate_boundary_diff_l(self.boundary_a, self.boundary_b)}")

        print("=" * 50)
        print(f"Stopping criteria met. \nSince L = (b-a) = {self.calculate_boundary_diff_l(self.boundary_a, self.boundary_b)} which is less then uncertainty interval: {self.uncertainty_interval}")
        print(f"The final interval [a, b]: [{self.boundary_a}, {self.boundary_b}]")
        mid_point_x = (self.boundary_b + self.boundary_a) / 2
        print(f"The final midpoint x: {mid_point_x}")


    def calculate_x_1(self, boundary_b, boundary_a):
        result = boundary_b - self.reciprocal_golden_ratio_d * self.calculate_boundary_diff_l(boundary_a, boundary_b)
        return result

    def calculate_x_2(self, boundary_a, boundary_b):
        result = boundary_a + self.reciprocal_golden_ratio_d * self.calculate_boundary_diff_l(boundary_a, boundary_b)
        return result


a = -4
b = 0
golden_ratio = (1 + np.sqrt(5)) / 2
reciprocal_ratio_d = 1 / golden_ratio
evaluation_string = "(1/ 4)x4 − (5/ 3)x3 − 6x2 + 19x − 7"
goldenSearchAlgo = GoldenSearchAlgorithm(a, b, 0.2, reciprocal_ratio_d)
goldenSearchAlgo.calculate_func(evaluation_string, 'x')
