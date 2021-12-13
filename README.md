<p>
    <h1 align="center">DATASORT</h1>
</p>
Returning the index and value of the original input. Current solution runs at O(n) * 0(n log n), this solution involves two operations. First we poplate a list with int values and sort it based off of the values while keeping the original index of that value.

```python

sortnLargest([4,5,6,7,2,3], 1)  # This wil return (3,7)
sortnLargest([4,5,6,7,2,3], 2)  # This wil return (2,6)

''' Error Responses '''
sortnLargest(['d', 'a'], 10)  # This will return (-1,-1)
```

