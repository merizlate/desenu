files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
chunksize = 2

for i in range(0, len(files), chunksize):
    print(files[i:i+chunksize])

# Output:
# ['file1.txt', 'file2.txt']
# ['file3.txt', 'file4.txt']
# ['file5.txt']
