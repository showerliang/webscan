# Web Services API #

## Important Considerations ##

  1. All strings between [.md](.md) are variables.
  1. All returns are JSON.
  1. The default return is an associative array containing the error code and msg. If the error code is equal to 0 (zero) there is no errors.
  1. Arguments marked with `*` are optional.

## Concepts ##

  * Method
  * Instanced Object
  * Collection (list of instanced objects)

A string followed by / (slash) in an URL represents object members (method or object) and followed by . (dot) represents collection members.

ie:

  * **modify** is a method of an instanced object scanner:
```
/scanner/[name]/modify
```

  * **add** is a method of the collection of scanners:
```
/scanner.add
```

## Services ##

### Scanner ###

Show all configured scanners:
```
URL: /scanner
Args: None
Method: GET, POST
Returns: Collection containing all scanner objects.
```

Add a new scanner to the list:
```
URL: /scanner.add
Args: name, location*, description*, manufacturer, model, papersize*, isindexable*, user*, group*
Method: POST
Returns: Scanner object.
```

Get a scanner object:
```
URL: /scanner/[name]
Args: None
Method: GET, POST
Returns: Scanner object.
```

Modify a scanner configuration:
```
URL: /scanner/[name]/modify
Args: name*, location*, description*, manufacturer*, model*, papersize*, isindexable*, user, group
Method: POST
Returns: Scanner object.
```

Remove a scanner:
```
URL: /scanner/[name]/delete
Args: None
Method: DELETE
Returns: Default
```

Get the scanner status code (See ScannerStatusCode):
```
URL: /scanner/[name]/status
Args: None
Method: GET, POST
Returns: Default
```

Scan a page:
```
URL: /scanner/[name]/scan
Args: None
Method: GET, POST
Return: Page object.
```

### User ###

List all registered users:
```
URL: /user
Args: None
Method: GET, POST
Returns: Collection containing all user objects.
```

Add a new user:
```
URL: /user.add
Args: username, password, role
Method: POST
Returns: User object.
```

Get an user object:
```
URL: /user/[username]
Args: None
Method: GET, POST
Returns: User object.
```

Modify an user registry:
```
URL: /user/[username]/modify
Args: username*, password*, role*
Method: POST
Returns: User object.
```

Deletes an user:
```
URL: /user/[username]/delete
Args: None
Method: DELETE
Returns: Default
```

List all the scanned (and not used) pages:
```
URL: /user/[username]/page
Args: None
Method: GET, POST
Returns: Collection of page objects.
```

Delete a page:
```
URL: /user/[username]/page/[pageid]/delete
Args: None
Method: DELETE
Returns: Default
```

List all the generated documents:
```
URL: /user/[username]/document
Args: None
Method: GET, POST
Return: Collection of document objects.
```

Create a new document using the selected pages:
```
URL: /user/[username]/document.create
Args: docname, docdescript, pages (list of page ids)
Method: GET, POST
Return: Document object.
```

Delete a document:
```
URL: /user/[username]/document/[docname]/delete
Args: None
Method: DELETE
Return: Default
```

Download a document using the docname:
```
URL: /user/[username]/document/[docname]
Args: None
Method: GET, POST
Return: Downloadable PDF document.
```

### Auth ###

Authenticate an user:
```
URL: /auth/signin
Args: username, password
Method: POST
Returns: Default
```

Sign out an user:
```
URL: /auth/signout
Args: None
Method: GET, POST
Returns: Default
```