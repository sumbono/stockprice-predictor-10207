from app.libs.stock_name import stock_name_dict

def make_markdown_table(array):
    """ 
    Input:  Python list with rows of table as lists,
            First element as header. 
    Output: String to put into a .md file 
    
    Ex Input: 
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]] 
    """

    nl = "\n"

    markdown = nl
    markdown += f"| {' | '.join(array[0])} |"

    markdown += nl
    markdown += f"| {' | '.join(['---']*int(len(array[0])))} |"

    markdown += nl
    for entry in array[1:]:
        markdown += f"| {' | '.join(entry)} |{nl}"

    return markdown


stock_company_lst = [["STOCK", "COMPANY"],]
for k,v in stock_name_dict.items():
    vnc = v.split('|')
    stock_company_lst.append([vnc[0].strip(), vnc[1].strip()])
stock_company_table = make_markdown_table(stock_company_lst)

metadata = {
    "title":"StockPricesPredictor App",
    "description" : """StockPricesPredictor App API helps you to predict the stock-prices for next 7 days. 🚀
    
    Pre-trained stock models:

    | STOCK | COMPANY |
    ------------------------------
    | AAPL | Apple Inc. |
    | MSFT | Microsoft Corporation |
    | GOOGL | Alphabet Inc. |
    | GOOG | Alphabet Inc. |
    | AMZN | Amazon.com, Inc. |
    | TSLA | Tesla, Inc. |
    | META | Meta Platforms, Inc. |
    | NVDA | NVIDIA Corporation |
    | KO | The Coca-Cola Company |
    | VZ | Verizon Communications Inc. |
    | AMD | Advanced Micro Devices, Inc. |
    | INTC | Intel Corporation |
    | NFLX | Netflix, Inc. |
    | BYDDY | BYD Company Limited |
    | ENB | Enbridge Inc. |
    | OXY | Occidental Petroleum Corporation |
    | PANW | Palo Alto Networks, Inc. |
    | CRWD | CrowdStrike Holdings, Inc. |
    | LNG | Cheniere Energy, Inc. |
    | HPO | HP Inc. |
    | SNAP | Snap Inc. |
    | MDB | MongoDB, Inc. |
    | BBY | Best Buy Co., Inc. |
    | CHWY | Chewy, Inc. |
    | FSLR | First Solar, Inc. |
    | OKTA | Okta, Inc. |
    | CHPT | ChargePoint Holdings, Inc. |
    | EE | Excelerate Energy, Inc. |
    | RKLB | Rocket Lab USA, Inc. |
    | TELL | Tellurian Inc. |

    """,
    "version":"0.0.1",
    "contact":{
        "name": "Sumbono",
        "url": "https://github.com/sumbono",
        "email": "sumbono102@gmail.com",
    },
    "tags": [
        {
            "name": "predict",
            "description": "Predict stock prices for next 7 days.",
            "externalDocs": {
                "description": "Top 30 stocks on watchlists by Yahoo Finance Users (2th Sept 2022)",
                "url": "https://finance.yahoo.com/u/yahoo-finance/watchlists/most-added",
            },
        },
        {
            "name": "train",
            "description": "Train a new or retrain an existing model. based on the stock name",
            "externalDocs": {
                "description": "Stocks on each watchlists by Yahoo Finance",
                "url": "https://finance.yahoo.com/watchlists",
            },
        },
    ],
}