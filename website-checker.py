print(" WEBSITE URL CHECKER ")
url = input("\nEnter a website URL: ")

if url.startswith("https://"):
    print("This website uses HTTPS (SECURE) ")
elif url.startswith("http://"):
    print("This website uses HTTP (NOT SECURE)")
else:
    print("This doesn't look like a complete URL ")