def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    
    sum = num1 + num2
    diff = num1 - num2
    product =  num1 * num2
    div= num1 / num2
    flo_div= num1 // num2
    remainder= num1 % num2
    expo= num1 ** num2     
        
   
    
    result = {'sum':sum,'diff':diff,'product':product,'div':div,'flo_div':flo_div,'remainder':remainder,'expo':expo}
    return result