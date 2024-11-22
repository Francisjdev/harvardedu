import sys, requests
print(len(sys.argv))
if len(sys.argv)<2:
    sys.exit("missing command-line argument")   
try:
    bitcoin =float(sys.argv[1])
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except ValueError:    
    sys.exit("must be a a positive number")
except requests.RequestException:
    pass
r=response.json()
rate=r["bpi"]["USD"]["rate_float"]
print(r)
amount = float(rate)*bitcoin
print(f"{amount:,.4f}")  