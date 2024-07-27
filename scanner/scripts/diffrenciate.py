import pandas as pd
# from scanner.scripts.get_stocks import calculate_passed_stocks as get_stock

# function for updating values for the next iteration
def update_values(toupdate,fromupdate):
    # print("fromupdate",fromupdate)
    for i in range(len(toupdate)):
        toupdate[i]=fromupdate.iloc[i+1]
    return    


data_shares = pd.read_csv('scanned.csv')




def diffrenciate_stocks(closing_range,close_diff,volume_range,volume_diff):
    # print("function run")
    results=[]
    # open_p ,high_p ,low_p ,close_p ,volume_p , name_p
    prev_values=[0,0,0,0,0,""]

    for index,row in data_shares.iterrows():
        # print("loop started")
        
        if index==0:
            update_values(prev_values,row)
            continue
        # if index>=100:
        #      continue
        # print('if passed')
        open_p, high_p, low_p, close_p, volume_p, name_p = prev_values
        date_time, open, high, low, close, volume, name = row
        
        if name!=name_p:#conditions if the stock we are working on is same or not
            update_values(prev_values,row)
            continue




      
        # print("calculation started")
        calculated_para={}

        if closing_range and not closing_range[0]<=close<=closing_range[1] :#if closing range is given and this is not in range then go to next itration
                update_values(prev_values,row)
                # print("c_range")
                continue

        if close_diff :
            if (close-close_p)*100/close_p>=close_diff if close_diff>0 else (close-close_p)*100/close_p<=close_diff:
                calculated_para['close_diff']=round((close-close_p)*100/close_p,2)
            else:
                update_values(prev_values,row)
                # print("c_diff",round((close-close_p)*100/close_p,2))
                continue

        if volume_range and not volume_range[0]<=volume<=volume_range[1] :
                update_values(prev_values,row)
                # print("v_range")
                continue
                
        if volume_diff : 
            if (volume-volume_p)*100/volume_p>=volume_diff if volume_diff>0 else (volume-volume_p)*100/volume_p<=volume_diff:
                calculated_para["volume_diff"]=round((volume-volume_p)*100/volume_p,2)
            else:
                update_values(prev_values,row)
                # print("v_diff",round((volume-volume_p)*100/volume_p))
                continue


        results.append({"date_time":date_time,
                        "open":open,
                        "high":high,
                        "low":low,
                        "close":close,
                        "volume":volume,
                        "name":name,
                        "calculated_para":calculated_para})

        update_values(prev_values, row)

    #*************************************************
    return results






# results=diffrenciate_stocks([100,10000000],10,[],200)
# for result in results:
#     print(result)
# print(len(results))