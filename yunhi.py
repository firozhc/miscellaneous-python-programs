import requests


#url = "https://api.easypurl.com/rest/v1/json/EasyPurlGetCampaignList"
"""
base_url = "https://api.easypurl.com/rest/v1/json/EasyPurlCloneCampaign"
jobid = "1"
BaseCampaignId = "271132" 
clone_url = base_url+'/'+jobid+'/'+BaseCampaignId


"""
append_url = "https://api.easypurl.com/rest/v1/json/EasyPurlAppendMailingList"
filename = "258714.csv"

#append_url = "https://api.easypurl.com/rest/v1/json/EasyPurlAppendMailingListUniversal"
#filename = "samplefilewithuniversalheaders.csv"

campaignId = "271511"

url = append_url+"/"+filename+"/"+campaignId

print(url)


with open(filename,'rb') as f:
	
	pee = "{ \"UserCredential\": { \"UserName\": \"firozhc@easypurl.com\", \"Password\": \"mapps123#\" }, \"FileData\":"

	load = "\""+str(f.read()) + "\"}"

	#load = " \"Name, Gender \n Tom, Female }"

	payload = pee+load

	print(payload)


	headers = {
    	'Content-Type': "application/json",
    	'Cache-Control': "no-cache"
    	}


	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
	print(response.status_code)




#payload = "{ \"UserName\": \"firozhc@easypurl.com\", \"Password\": \"mapps123#\"}"



#{"JobId":"1","CampaignId":"271512","CampaignName":"Camp_11062018_160346_1"}

