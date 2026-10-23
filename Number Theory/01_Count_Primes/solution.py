"""
Problem: Count Primes (LeetCode #204)
Sieve of Eratosthenes
Time Complexity: O(N log log N)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                # Mark multiples starting from p*p
                is_prime[p * p : n : p] = [False] * len(range(p * p, n, p))

        return sum(is_prime)

if __name__ == "__main__":
    sol = Solution()
    assert sol.countPrimes(10) == 4  # 2, 3, 5, 7
    assert sol.countPrimes(0) == 0
    assert sol.countPrimes(1) == 0
    print("✅ All Count Primes tests passed!")
