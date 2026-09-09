def solution(ineq, eq, n, m):
   conditions = {
        (">", "="): n >= m,
        ("<", "="): n <= m,
        (">", "!"): n > m,
        ("<", "!"): n < m,
    }
   return 1 if conditions[(ineq, eq)] else 0
