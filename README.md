# Consulting-Associate-2023-Technical-Assessment-Q1
ALGO0001. Looking for Size
A shop has some T-shirts available. T-shirt size ranges from 1000XS (1000 'X's before 'S') to 1000XL (1000 'X's before 'L'). The sizes order in (XXXX...XXXS ≤ XS ≤ S ≤ M ≤ L ≤ XL ≤ XXXX...XXXL) from the smallest to the largest.

Customers will come to the shop and request T-shirts of different sizes. The shop can fulfill a request with a T-shirt with an exact size or a larger size. For example, a request of size M can be fulfilled with a T-shirt of size M / L / XL / XXXX...XXXL.

Your task is to help the shop to check if ALL requests can be fulfilled.

Input
The first line contains a number N (1 ≤ N ≤ 1000), the total number of T-shirts in shop.
The second line contains N strings representing the T-shirt sizes in shop.
The third line contains a number M (1 ≤ M ≤ N), the total number of requests.
The forth line contains M strings representing the requested sizes.

Example:

5
XL XXXXXXXXXL XXS M XXS
4
L M L XXS
Output
Print Yes if all the requests can be fulfilled. Otherwise print No.

Example:

Yes
Explanation:
There are 4 requests in the above example.

L can be fulfilled by XL
M can be fulfilled by M
L can be fulfilled by XXXXXXXXXL
XXS can be fulfilled by XXS
