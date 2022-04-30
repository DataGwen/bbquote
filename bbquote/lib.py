import requests as rq

URL = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"

def get_quote():
    response =  rq.get(URL).json()[0]
    return response['quote'], response['author']

def main():
    quote, author = get_quote()
    print(f"'{quote}' \n>>> {author}")

if __name__ == "__main__":
    main()
