from django.shortcuts import render, HttpResponse
from scanner.scripts.get_stocks import calculate_passed_stocks as get_stock
from scanner.scripts.diffrenciate import diffrenciate_stocks as df_stocks
def index(request):
    return render(request, 'scanner/landing.html')

def scan(request):
    if request.method == 'POST':
        
        close_diff=int(request.POST.get('close_diff',None))
        close_range=request.POST.get('close_range',"").split(",")
        volume_diff=int(request.POST.get('volume_diff',None))
        volume_range=request.POST.get('volume_range',"").split(",")
        close_range = [int(i) for i in close_range] if len(close_range)>1 else []
        volume_range =  [int(i) for i in volume_range] if len(volume_range)>1 else []


        ##it is for getting stock data from api
        # try:
        #     time_intevel="ONE_DAY"
        #     start_date="2024-07-22 09:00"
        #     end_date="2024-07-24 09:00"

        #     get_stock(time_intevel,start_date,end_date)

        #     print("the paras" ,close_range,close_diff,volume_range,volume_diff)
        #     results=df_stocks(close_range,close_diff,volume_range,volume_diff)
        #     context = {
        #         'results': results,  
        #     }

        #     return render(request, 'scanner/scanned.html', context)
        
        # except Exception as e:
        #     error_message = f"Error fetching stock data: {e}"
        #     return (error_message)



        #filtering the stocks 
        try:
            print("the paras" ,close_range,close_diff,volume_range,volume_diff)
            results=df_stocks(close_range,close_diff,volume_range,volume_diff)
            context = {
                'results': results,  
            }

            return render(request, 'scanner/scanned.html', context)
        except Exception as e:
            error_message = f"Error fetching in choosing stocks ,we are in views: {e}"
            return (error_message)
          


