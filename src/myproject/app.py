from src.myproject.utils import greet, fetch_status

def main():
    print(greet("Hello Boris!"))
    print(greet("Hellow  all!"))
    print(fetch_status("https://example.com"))

if __name__ == "__main__":
    main()
