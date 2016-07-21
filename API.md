**Get Categories**
----
  Returns json object with all categories in civic graph and their associated integer id.

* **URL**

  /api/categories

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]` ##NONE???!??!?

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
    **Content:** `{ error : "You are unauthorized to make this request." }` ##CHECK THIS???
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