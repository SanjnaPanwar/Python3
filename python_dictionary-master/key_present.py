 a={'key1': 1, 'key2': 3, 'key3': 2}
 b={'key1': 1, 'key2': 2}
 for i in a and b:
     if a[i]==b[i]:
         print({i:a[i]},"is present")
