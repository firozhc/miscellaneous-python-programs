import requests
import json

###################################################################################
#Author: Firoz Hossain Chaudhuri
#Date: 12th June, 2018
#Description: This Script contains the functions to call Easypurl API
###################################################################################



#Get Campaign List Method
def GetCampaignList(UserId, Password):

	headers = {'Content-Type': "application/json", 'Cache-Control': "no-cache"}

	url = "https://api.easypurl.com/rest/v1/json/EasyPurlGetCampaignList"

	jsondata = { "UserName": UserId, "Password": Password}

	payload = json.dumps(jsondata)

	response = requests.request("POST", url, data=payload, headers=headers)

	returnval = json.loads(response.text)

	return returnval



#Clone Campaign Method
def CloneCampaign(JobId, CampaignId, UserId, Password):

	headers = {'Content-Type': "application/json", 'Cache-Control': "no-cache"}

	base_url = "https://api.easypurl.com/rest/v1/json/EasyPurlCloneCampaign" 

	url = base_url+'/'+JobId+'/'+CampaignId

	jsondata = { "UserName": UserId, "Password": Password }

	payload = json.dumps(jsondata) #Convert json dict to string for API transmission

	response = requests.request("POST", url, data=payload, headers=headers)

	returnval = json.loads(response.text)

	return returnval


#Append Mailing List Method
def AppendMailingList(CampaignId, filename, UserId, Password):

	headers = {'Content-Type': "application/json", 'Cache-Control': "no-cache"}

	base_url = "https://api.easypurl.com/rest/v1/json/EasyPurlAppendMailingListUniversal"

	url = base_url+"/"+filename+"/"+CampaignId

	with open(filename,'r') as f:

		FileData = str(f.read())

		f.close()

	jsondata = { "UserCredential": { "UserName": UserId, "Password": Password }, "FileData":FileData}

	payload = json.dumps(jsondata)

	response = requests.request("POST", url, data=payload, headers=headers)

	returnval = json.loads(response.text)

	return returnval



def main():

	UserId = "firozhc@easypurl.com"
	Password = "mapps123#"

	jobId = "1"
	
	#CampaignId = "271197"  #VA   Credence-Client
	
	#CampaignId = "271476"  #FHA  JFQ-Client
	
	#print(CloneCampaign(jobId, CampaignId, UserId, Password))

	
	filename = "samplefilewithuniversalheaders.CSV"

	campaignId = "271521"

	#print(AppendMailingList(campaignId, filename, UserId, Password))

	#print(GetCampaignList(UserId, Password))



if __name__== "__main__":
	main()
