class Exercises:

    def quadratic_solver(self, a, b, c):
        if a == 0:
            return -c/b
        delta = b**2 - 4*a*c
        if delta < 0:
            return 
        elif delta == 0:
            x1 = -b/(2*a)
            return x1
        else :
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            return x1, x2
        
    def recaman_sequence(self, n):
        seq = []
        seq.append(0)
        
        for i in range(1, n):
            a = seq[i-1] - i
            b = seq[i-1] + i
            
            if a > 0:
                if not a in seq:
                    seq.append(a)
                else:
                    seq.append(b)
                    
            else:
                seq.append(b)
                
        return seq
    
    def primes(self, n):
        A = [True]*(n+1)
        for i in range(2, int(n**0.5) + 1):
            B = [i**2 + k*i for k in range(n) if i**2 + k*i <= n]
            for j in B:
                A[j] = False
        return [i for i in range(len(A)) if A[i] == True and i>=2 and i <=n ]
    
    def n_first_primes(self, N):
        n0 = 2
        l = self.primes(n0)
        while len(l) < N:
            n0 = 2*n0
            l = self.primes(n0)
        return l[:N]
            
        
    def ex1(self, a, b, c):
        res = self.quadratic_solver(a,b,c)
        print('Result:', res)

    def ex2(self, n):
        res = self.recaman_sequence(n)
        print('The sequence is {}'.format(res))
    
    def ex9(self, n):
        res = self.n_first_primes(n)
        print('The list of {} first primes is {}'.format(n, res))