from ast import Pass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#install the driver
driver = webdriver.Chrome(ChromeDriverManager.install())

def urlLinker(wallet_type):
    if wallet_type == 'BNB':
        url = 'https://www.bscscan.com/'
    elif wallet_type == 'ETH':
        url = 'https://etherscan.io/'
    elif wallet_type == 'BTC':
        url = ''

#BTC ETH BNB
def getCollection(wallet_type, address):
    pass


#run the driver continuosly
while "__main__" == __name__:
    pass





