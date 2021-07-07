 
import requests
import json
 
      
class HttpRequestHelper():

        def makeHttpGETRequest(self,url):
                try:
                        r = requests.get(url)
                        response = r.json()
                        if r.status_code == 200:
                            return self.responseObj(True,r.status_code,response)
                        else:
                            return self.responseObj(False,r.status_code)
                except  requests.RequestException as e:
                        return self.responseObj()


        def responseObj(self, state = False ,code = None ,response = None):
                return {
                            "state": state ,
                            "status_code" : code,
                            "response": response
                    }