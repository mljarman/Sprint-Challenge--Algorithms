#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): There is a while loop so if the number of inputs increase, the number of operations needed also increase proportionately.


b) O(n^2): There are two loops and one is nested so inputs are being iterated n*n times.


c) O(n): This uses recursion and calculates the number of ears for n bunnies. If the number of bunnies increase the number of recursive calls increases and likewise the number of calculations. It's linear.

## Exercise II

Thinking about eggs and how they can't even survive the fall from my counter to the floor, I think it is safe to say without any testing that if an egg can survive on a drop from f-1, that f would be 1. No innocent eggs would even need to be destroyed in the process.

If eggs weren't so fragile, I think going floor by floor would take time and a lot more eggs than running an experiment like a binary search. If we had f floors, we could cut the floors in half, or perhaps, depending on our knowledge of the experiment and initial hypotheses, begin at less than half of the floors. For this exercise we will start at the middle floor. Drop an egg, if it doesn't break we can split the remaining upper floors and perform the experiment again trying to find the highest floor we can successfully drop an egg without it breaking.

On the other hand, if the egg drops from mid-way and breaks, we would follow the same procedure and cut the lower remaining levels in half and continue performing the experiment of dropping an egg and then moving in increments higher or lower to find the highest floor we can drop an egg without it breaking.

If we went floor by floor the time complexity would be O(n), but if we used a binary search method the time complexity would be O(log n) because we're splitting the number of floors we have to test each time and hopefully finding the highest floor possible quickly and with dropping and breaking a less amount of eggs.
