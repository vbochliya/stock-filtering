
from datetime import datetime
import pandas as pd
from SmartApi.smartConnect import SmartConnect 
import pyotp


obj=SmartConnect (api_key='........?')

totp= pyotp.TOTP ('......................?')
totp=totp.now()
# print("pasrse: totp is :", totp)
attempts=5
while attempts >0:
    attempts= attempts-1
    data = obj.generateSession("......?","...?", totp) 
    # print(data)
    if data['status']:
        print("\nsmartapi login successful")
        break
refreshToken= data['data']['refreshToken']

feedToken=obj.getfeedToken()
# print('\n'+feedToken)

userProfile= obj.getProfile(refreshToken)
# print('\n')
# print(userProfile)







# Function to fetch candle data for a given Token
def fetch_candle_data(exch_seg,Token,time_intevel,start_date,end_date,index):
    print(index," stock is here ..........................")
    atmpt=5
    for attempt in range(atmpt):
        try:
            historicParam = {
                "exchange": exch_seg,
                "symboltoken": Token,
                "interval": time_intevel,
                "fromdate": start_date,
                "todate": end_date
            }
            
            candle_data = obj.getCandleData(historicParam)
            
            if not candle_data['status']:
                if attempt<atmpt-1:
                    continue
                print(f"No data returned from getCandleData for {Token}")
            else:
                print(f"data for {Token} received")
                return candle_data['data']
            
        except Exception as e:
            if attempt<atmpt-1:
                continue
            print(f"Error while fetching/trying candle data for {Token}")
            return None



# Iterate through each row of the DataFrame and fetch candle data
def calculate_passed_stocks(time_intevel,start_date,end_date):

    equity_df = pd.read_csv('eq_shares.csv')

    results = []

    for index, row in equity_df.iterrows():

        Token = row['Token']
        Name = row['Name']
        exch_seg = row['exch_seg']

        candle_data = fetch_candle_data(exch_seg,Token,time_intevel,start_date,end_date,index)
        if candle_data:
            for candle in candle_data:
                candle.append(Name)
  
            # print(candle_data)
            results.append(candle_data)



    
    
    import csv

    csv_file = 'scanned.csv'

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
    
        for row in results:
            for r in row:
                writer.writerow(r)

    print(f'CSV file {csv_file} has been created successfully.')







    print('stocks scanned and logging Out!')
    atmpt=5
    for attempt in range(atmpt):
        try:
            logout=obj.terminateSession('V50334031')
            print("\nLogout Successfull")
            break
        except Exception as e:
            if attempt<atmpt-1:
                continue
            print("\nLogout failed: {}".format(e.message))

    return results







if __name__ == "__main__":
    print('directly called the script')
    time_intevel="ONE_DAY"
    start_date="2024-07-22 09:00"
    end_date="2024-07-24 09:00"
    calculate_passed_stocks(time_intevel,start_date,end_date)
else:
    print('called from other module to the script')
    
