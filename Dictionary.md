* Merge two Python dictionaries
    For dictionaries x and y, z becomes a merged dictionary with values from y replacing those from x.

    In Python 3.5 or greater, :
    ```
    z = {**x, **y}
    w = {'foo': 'bar', 'baz': 'qux', **y}  # merge a dict with literal values
    ```
    In Python 2, (or 3.4 or lower) write a function:
    ```
    def merge_two_dicts(x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z
    ```    
    and
    ```
    z = merge_two_dicts(x, y)
    ```
