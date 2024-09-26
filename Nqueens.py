def solve_n_queens(n):
    solutions = []

    def solve(queens):
        row = len(queens)
        if row == n:
            solutions.append(queens)
            return
        for col in range(n):
            if col not in queens and all(row - i != queens[i] - col and row - i != col - queens[i] for i in range(row)):
                solve(queens + [col])

    solve([])
    return solutions

def print_solutions(solutions):
    solution_number = 1
    for solution in solutions:
        print(f"Solution {solution_number}:")
        for i in range(len(solution)):
            print(f"  Queen {i + 1} is at row {i + 1}, column {solution[i] + 1}")
        print()
        solution_number += 1

n = int(input("enter the number of queens: "))
solutions = solve_n_queens(n)
print_solutions(solutions)


