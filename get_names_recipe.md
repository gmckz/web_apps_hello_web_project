# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

# Request:
GET /names?add=Eddie


# Request:
GET /names?add=Eddie,Leo



# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Names route
GET /names?add=Eddie


#Names route
GET /names?add=Eddie,Leo


```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# GET /names?add=Leo
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

# GET /names?add=Leo
# Expected response (200 OK):
"""
Alice, Eddie, Julia, Karim, Leo
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /names
    Parameters:
    add: Eddie
  Expected response (200 OK):
  "Julia, Alice, Karim, Eddie"
  ""
"""
def test_get_names(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
GET /names
    Parameters:
    add: Eddie,Leo
  Expected response (200 OK):
  "Alice, Eddie, Julia, Karim, Leo"
"""
def test_get_names_multiple_added():
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'