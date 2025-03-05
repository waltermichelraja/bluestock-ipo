# Authentication API Endpoints

## **>> Register a New User**
**Endpoint:**  
```
POST /api/auth/register
```
**Headers:**  
```http
Content-Type: application/json
```
**Request Body (JSON):**  
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "testpassword123",
  "first_name": "John",
  "last_name": "Doe"
}
```
**Response (Success - 201 Created):**  
```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "tokens": {
    "refresh": "<refresh_token>",
    "access": "<access_token>"
  }
}
```
**Response (Failure - 400 Bad Request):**  
```json
{
  "username": ["This field is required."],
  "email": ["This field is required."],
  "password": ["This field is required."]
}
```

---

## **>> Login User**
**Endpoint:**  
```
POST /api/auth/login
```
**Headers:**  
```http
Content-Type: application/json
```
**Request Body (JSON):**  
```json
{
  "username": "johndoe",
  "password": "testpassword123"
}
```
**Response (Success - 200 OK):**  
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```
**Response (Failure - 401 Unauthorized):**  
```json
{
  "detail": "Invalid credentials"
}
```

---

## **>> Get Current User**
**Endpoint:**  
```
GET /api/auth/user
```
**Headers:**  
```http
Authorization: Bearer <access_token>
```
**Response (Success - 200 OK):**  
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```
**Response (Failure - 401 Unauthorized - No Token Provided):**  
```json
{
  "detail": "Authentication credentials were not provided."
}
```
**Response (Failure - 401 Unauthorized - Invalid Token):**  
```json
{
  "detail": "Token is invalid or expired"
}
```

---

## **>> Logout User**
**Endpoint:**  
```
POST /api/auth/logout
```
**Headers:**  
```http
Content-Type: application/json
```
**Request Body (JSON) - Requires Refresh Token:**  
```json
{
  "refresh": "<refresh_token>"
}
```
**Response (Success - 205 Reset Content):**  
```json
{
  "detail": "Successfully logged out"
}
```
**Response (Failure - 400 Bad Request - Invalid Token):**  
```json
{
  "detail": "Invalid token"
}
```

---

## **>> Summary**
| Action | Endpoint | Method | Required Fields |
|--------|----------|--------|----------------|
| Register | `/api/auth/register` | `POST` | `username`, `email`, `password`, `first_name`, `last_name` |
| Login | `/api/auth/login` | `POST` | `username`, `password` |
| Get User | `/api/auth/user` | `GET` | `Authorization: Bearer <access_token>` |
| Logout | `/api/auth/logout` | `POST` | `refresh` token in request body |

