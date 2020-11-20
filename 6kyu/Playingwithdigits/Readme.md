Some numbers have funny properties. For example:

```
89    --> 8^1 + 9^2 = 89 * 1
695   --> 6^2 + 9^3 + 5^4 = 1390 = 695 * 2
46288 --> 4^3 + 6^4+ 2^5 + 8^6 + 8^7 = 2360688 = 46288 * 51
```

**Given** a positive integer <code>n</code> written as 
abcd... (a, b, c, d... being digits) and a positive integer <code>p</code>

- we want to find a positive integer <code>k</code>, if it exists, 
such as the sum of the digits of <code>n</code> taken to the successive 
powers of <code>p</code> is equal to <code>k * n</code>.

**In other words**:

Is there an integer <code>k</code> such as :

<code>(a ** p + b ** (p+1) + c ** (p+2) + d ** (p+3) + ...) = n * k</code>

If it is the case we will return <code>k</code>, if not return <code>-1</code>.

**Note**: <code>n</code> and <code>p</code> will always be given as strictly positive integers.

```
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

https://www.codewars.com/kata/5552101f47fc5178b1000050
