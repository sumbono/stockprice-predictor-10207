from enum import Enum

class StockName(str, Enum):
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOGL = "GOOGL"
    GOOG = "GOOG"
    AMZN = "AMZN"
    TSLA = "TSLA"
    META = "META"
    NVDA = "NVDA"
    KO = "KO"
    VZ = "VZ"
    AMD = "AMD"
    INTC = "INTC"
    NFLX = "NFLX"
    BYDDY = "BYDDY"
    ENB = "ENB"
    OXY = "OXY"
    PANW = "PANW"
    CRWD = "CRWD"
    LNG = "LNG"
    HPQ = "HPO"
    SNAP = "SNAP"
    MDB = "MDB"
    BBY = "BBY"
    CHWY = "CHWY"
    FSLR = "FSLR"
    OKTA = "OKTA"
    CHPT = "CHPT"
    EE = "EE"
    RKLB = "RKLB"
    TELL = "TELL"


stock_name_dict = {
    "AAPL" : "AAPL | Apple Inc.",
    "MSFT" : "MSFT | Microsoft Corporation",
    "GOOGL" : "GOOGL | Alphabet Inc.",
    "GOOG" : "GOOG | Alphabet Inc.",
    "AMZN" : "AMZN | Amazon.com, Inc.",
    "TSLA" : "TSLA | Tesla, Inc.",
    "META" : "META | Meta Platforms, Inc.",
    "NVDA" : "NVDA | NVIDIA Corporation",
    "KO" : "KO | The Coca-Cola Company",
    "VZ" : "VZ | Verizon Communications Inc.",
    "AMD" : "AMD | Advanced Micro Devices, Inc.",
    "INTC" : "INTC | Intel Corporation",
    "NFLX" : "NFLX | Netflix, Inc.",
    "BYDDY" : "BYDDY | BYD Company Limited",
    "ENB" : "ENB | Enbridge Inc.",
    "OXY" : "OXY | Occidental Petroleum Corporation",
    "PANW" : "PANW | Palo Alto Networks, Inc.",
    "CRWD" : "CRWD | CrowdStrike Holdings, Inc.",
    "LNG" : "LNG | Cheniere Energy, Inc.",
    "HPQ" : "HPO | HP Inc.",
    "SNAP" : "SNAP | Snap Inc.",
    "MDB" : "MDB | MongoDB, Inc.",
    "BBY" : "BBY | Best Buy Co., Inc.",
    "CHWY" : "CHWY | Chewy, Inc.",
    "FSLR" : "FSLR | First Solar, Inc.",
    "OKTA" : "OKTA | Okta, Inc.",
    "CHPT" : "CHPT | ChargePoint Holdings, Inc.",
    "EE" : "EE | Excelerate Energy, Inc.",
    "RKLB" : "RKLB | Rocket Lab USA, Inc.",
    "TELL" : "TELL | Tellurian Inc."
}