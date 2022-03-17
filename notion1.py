import requests, json

token1 = 'YOUR-SECRET-NOTION-INTEGRATION-TOKEN'   #  Substitute 

databaseID = 'YOUR-NOTION-DATABASE-ID'    #  Substitute 

headers = {
	"Authorization": "Bearer " + token1,
	"Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}


# To read a database
def readDatabase(databaseID, headers):
	readURL = f"https://api.notion.com/v1/databases/{databaseID}/query"

	response1 = requests.request("POST", readURL, headers=headers)
	data1 = response1.json()
	print(response1.status_code)
	print(response1.text)

	with open('./db.json', 'w', encoding='utf8') as f:
		json.dump(data1, f, ensure_ascii=False)

