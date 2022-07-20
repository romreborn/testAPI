import requests
import json
import pyodbc

conn = pyodbc.connect('Driver={SQL Server}; Server=.;Database=Primacom;Trusted_Connection=yes')
conn.timeout =  60
conn.autocommit = True

url = "http://localhost:3000/api/dataGIS/"

payload = json.dumps({
  "custid": "'ALK'",
  "remregion": "'0'",
  "serviceType": "''",
  "partner": "''"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)


sqlstatment = ''
data = json.loads(response.text)
count = len(data)
x = 0
cursor = conn.cursor()
while x < count:
        
    try:
     
        cursor.execute("EXEC spDataRemote 'insert','',"+
           
            "'"+ data[x]['RemID1'] +"A','"+ data[x]['CustID'] + "','" + data[x]['CustID']+ "','"+ data[x]['RemDesc1'] + "','"+
            str(data[x]['lat1']) + "','"+ str(data[x]['lon1']) + "','" + data[x]['RemAddress1'] + "','"+ data[x]['RemRegion1'] + "'")
        print('inserted Data')
    except pyodbc.Error as err:
        print('Error %s' % err)
    except:
        print ('Eror')
    
    print('closed DB connection')
   
    x += 1
 
conn.close()

