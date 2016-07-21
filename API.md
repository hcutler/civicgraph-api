**Get Categories**
----
  Returns json object with all categories in Civic Graph and their associated integer id.

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
  Returns json object with all connections in Civic Graph (grouped by connection type) with source id and target id for each connection.

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

----
**Get Entities**
----
  Returns json object with all entities in Civic Graph and data associated with each (`key_people, twitter_handle, grants_received, influence, locations, expenses, id, relations, followers, data_given, employments, type, description, grants_given, investments_made, nickname, gategories, name, collaborations, employees, data_received, url, revenues, investments_received`)

* **URL**

  /api/entities

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** [{u'key_people': [], u'twitter_handle': u'@yasminfodil', u'grants_received': [], u'influence': u'Local', u'locations': [{u'district': u'NY', u'locality': u'New York', u'country': u'United States', u'full_address': u'New York, NY', u'postal_code': None, u'coordinates': [40.782, -73.8317], u'country_code': u'US', u'address_line': None, u'id': 0}], u'expenses': [], u'id': 0, u'relations': [], u'followers': 1655, u'data_given': [], u'employments': [], u'type': u'Individual', u'description': u'I create experiences / services that solve public problems. Also - Adjunct Professor at @NYU_Wagner', u'grants_given': [], u'investments_made': [], u'nickname': u'Yasmin', u'categories': [{u'id': 3, u'name': u'General Civic Tech'}, {u'id': 4, u'name': u'Social Services'}, {u'id': 5, u'name': u'Jobs & Education'}, {u'id': 6, u'name': u'GovTech'}], u'name': u'Yasmin Fodil', u'collaborations': [{u'id': 911, u'entity_id': 290, u'details': None, u'entity': u'Alexander Howard'}], u'employees': None, u'data_received': [], u'url': u'http://yasminfodil.com', u'revenues': [], u'investments_received': []}, ......}]
    
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `requests.exceptions.HTTPError: 404 Client Error: NOT FOUND`

  OR

  * **Code:** 405 METHOD NOT ALLOWED <br />
    **Content:** `requests.exceptions.HTTPError: 405 Client Error: METHOD NOT ALLOWED for url: http://civicgraph.io/api/entities`

* **Sample Call:**

  ```python
      url = "http://civicgraph.io/api/connections"
      data = '{"query":{"connections":{}}'
      response = requests.get(url, data=data)

      if (response.ok):
        jData = json.loads(response.content)
        for key in jData:
          print JData[key]
      else:
        print response.raise_for_status()
  ```