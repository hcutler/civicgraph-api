**Get Categories**
----
  Returns json object with all categories in civic graph and their associated integer id.

* **URL**

  /api/categories

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** {"categories": [{"id": 1, "name": "Smart & Resilient Cities"}, {"id": 2, "name": "Data & Analytics"}, {"id": 3, "name": "General Civic Tech"}, {"id": 4, "name": "Social Services"}, {"id": 5, "name": "Jobs & Education"}, {"id": 6, "name": "GovTech"}]}
    
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `requests.exceptions.HTTPError: 404 Client Error: NOT FOUND`

  OR

  * **Code:** 405 METHOD NOT ALLOWED <br />
    **Content:** `requests.exceptions.HTTPError: 405 Client Error: METHOD NOT ALLOWED for url: http://civicgraph.io/api/categories`

* **Sample Call:**

  ```python
      url = "http://civicgraph.io/api/categories"
      data = '{"query":{"categories":[{}]}'

      response = requests.get(url, data=data)
      if (response.ok):
        jData = json.loads(response.content)
        for key in jData:
          print jData[key]
      else:
        print response.raise_for_status()
  ```
----

**Get Connections**
----
  Returns json object with all connections in civic graph (grouped by connection type) with source id and target id for each connection.

* **URL**

  /api/connections

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** {"connections": {"Collaboration": [{"source": 1, "target": 22}, {u'Employment': [{u'source': 116, u'target': 283}, ...... {"source": 586, "target": 337}], "Employment": [{"source": 116, "target": 283}, ......]}}
    
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `requests.exceptions.HTTPError: 404 Client Error: NOT FOUND`

  OR

  * **Code:** 405 METHOD NOT ALLOWED <br />
    **Content:** `requests.exceptions.HTTPError: 405 Client Error: METHOD NOT ALLOWED for url: http://civicgraph.io/api/connections`

* **Sample Call:**

  ```python
      url = "http://civicgraph.io/api/connections"
      data = '{"query":{"connections":{}}'
      response = requests.get(url, data=data)

      if (response.ok):
        jData = json.loads(response.content)
        for key in jData:
          print JData[key] #print all connection types
          print jData[key]["Employment"] #print only Employment connections
          print jData[key]["Collaboration"] #print only Collaboration connections
          print jData[key]["Data"] #print only Data connections
          print jData[key]["Funding"] #print only Funding connections
          print jData[key]["Relation"] #print only Relation connections
      else:
        print response.raise_for_status()
  ```