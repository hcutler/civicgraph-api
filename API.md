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
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```