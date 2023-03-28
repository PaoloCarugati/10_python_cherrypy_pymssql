import requests
#import json


def callGET(id=None):
    print("***** GET *****")
    if (id == None):
        getUrl = url
    else:
        getUrl = url + "/" + str(id)
    print("url: " + getUrl)
    response = requests.get(getUrl)
    print("status code: " + str(response.status_code))
    #print(response.content)
    json = response.json()
    print("response content:")
    print(json)
    print("***************")
    print("")
    print("")
    print("")


def callPOST(disco):
    print("***** POST *****")
    print("url: " + url)

    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    response = requests.post(
        url, 
        json=disco,
        headers=headers
    )
    print("status code: " + str(response.status_code))
    #print("response content:")
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")


def callPUT(id, disco):
    putUrl = url + "/" + str(id)
    print("***** PUT *****")
    print("url: " + putUrl)

    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    response = requests.put(
        putUrl, 
        json=disco,
        headers=headers
    )
    print("status code: " + str(response.status_code))
    #print("response content:")
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")


def callDELETE(id):
    print("***** DELETE *****")
    deleteUrl = url + "/" + str(id)
    print("url: " + deleteUrl)
    response = requests.delete(deleteUrl)
    print("status code: " + str(response.status_code))
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")




url = 'http://127.0.0.1:8080/dischi'
#print("url: " + url)


#singolo disco
#callGET(1)

#lista dischi
callGET()



disco = {
            "Title": "Duke",
            "Artist": "Genesis",
            "Year": 1981,
            "Company": "A&M"      
        }
#print(disco)

#inserimento nuovo disco
#callPOST(disco)

#callGET()

#modifica disco
disco["Year"] = 1980


"""
#eliminazione disco
callDELETE(5)
callGET()
"""