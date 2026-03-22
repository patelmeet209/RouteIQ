import os

dirs = [
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\utils",
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\feeds",
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\road_network",
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\llm",
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\app",
    r"c:\Users\Meet Patel\OneDrive\Desktop\Route_IQ\data\graph_cache"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
