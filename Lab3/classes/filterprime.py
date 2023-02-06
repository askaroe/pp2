class Filter_prime():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   

    def filter_primes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)

prime_filter = Filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filter_primes(nums))
print(prime_numbers)
#result: [2, 3, 5, 7]
