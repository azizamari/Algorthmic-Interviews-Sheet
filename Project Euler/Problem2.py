# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fib(n,memo={}):
    if n in [0,1]: return n
    if n not in memo:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

sum=0
i=0
while True:
    f=fib(i)
    i+=1
    if f>4000000:break
    if f%2==0:sum+=f
print(sum)