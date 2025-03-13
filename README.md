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

---

# Stocks API Endpoints

## **>> Get All Stocks**
**Endpoint:**  
```
GET /api/stocks/
```
**Response (Success - 200 OK):**  
```json
[
  {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "currency": "USD",
    "exchange": "NASDAQ"
  },
  {
    "symbol": "GOOGL",
    "name": "Alphabet Inc.",
    "currency": "USD",
    "exchange": "NASDAQ"
  }
]
```
**Response (Failure - 500 Internal Server Error):**  
```json
{
  "error": "Failed to fetch stock list"
}
```

---

## **>> Get Stock Data**
**Endpoint:**  
```
GET /api/stocks/<symbol>/
```
**Response (Success - 200 OK):**  
```json
{
  "symbol": "AAPL",
  "name": "Apple Inc.",
  "industry": "Technology",
  "sector": "Consumer Electronics",
  "market_cap": 2500000000000,
  "currency": "USD",
  "price": 180.50,
  "exchange": "NASDAQ",
  "website": "https://www.apple.com"
}
```
**Response (Failure - 500 Internal Server Error):**  
```json
{
  "error": "Failed to fetch stock details"
}
```

---

## **>> Search Stocks**
**Endpoint:**  
```
GET /api/stocks/search/<query>/
```
**Response (Success - 200 OK):**  
```json
{
  "stocks": [
    {
      "symbol": "AAPL",
      "name": "Apple Inc.",
      "currency": "USD",
      "stockExchange": "NASDAQ"
    },
    {
      "symbol": "AMZN",
      "name": "Amazon.com Inc.",
      "currency": "USD",
      "stockExchange": "NASDAQ"
    }
  ]
}
```
**Response (Failure - 500 Internal Server Error):**  
```json
{
  "error": "Failed to fetch stock symbols"
}
```

---

## **>> Get Stock Historical Data**
**Endpoint:**  
```
GET /api/stocks/<symbol>/history/
```
**Response (Success - 200 OK):**  
```json
{
  "symbol": "AAPL",
  "historical": [
    {
      "date": "2024-03-01",
      "open": 178.00,
      "high": 182.00,
      "low": 177.50,
      "close": 180.50
    },
    {
      "date": "2024-02-29",
      "open": 175.00,
      "high": 179.50,
      "low": 174.80,
      "close": 178.00
    }
  ]
}
```
**Response (Failure - 500 Internal Server Error):**  
```json
{
  "error": "Failed to fetch historical data"
}
```

---

## **>> Get Trending Stocks**
**Endpoint:**  
```
GET /api/stocks/trending/
```
**Response (Success - 200 OK):**  
```json
{
  "trending_stocks": [
    {
      "symbol": "NVDA",
      "name": "NVIDIA Corporation",
      "price": 550.75,
      "change": 15.30,
      "change_percent": 2.85,
      "day_high": 560.00,
      "day_low": 540.50,
      "market_cap": 1350000000000
    },
    {
      "symbol": "TSLA",
      "name": "Tesla Inc.",
      "price": 210.00,
      "change": 5.20,
      "change_percent": 2.55,
      "day_high": 215.00,
      "day_low": 205.50,
      "market_cap": 700000000000
    }
  ]
}
```
**Response (Failure - 500 Internal Server Error):**  
```json
{
  "error": "Failed to fetch trending stocks"
}
```

---

## **>> Summary**
| Action | Endpoint | Method | Required Parameters |
|--------|----------|--------|--------------------|
| Get All Stocks | `/api/stocks/` | `GET` | None |
| Get Stock Data | `/api/stocks/<symbol>/` | `GET` | `symbol` |
| Search Stocks | `/api/stocks/search/<query>/` | `GET` | `query` |
| Get Stock History | `/api/stocks/<symbol>/history/` | `GET` | `symbol` |
| Get Trending Stocks | `/api/stocks/trending/` | `GET` | None |

---

# Portfolio API Endpoints

### **>> Get User's Portfolio**
**Endpoint:**  
```
GET /api/portfolio
```
**Headers:**  
```http
Authorization: Bearer <access_token>
```
**Response (Success - 200 OK):**  
```json
{
  "stocks": [
    {
      "id": 1,
      "symbol": "AAPL",
      "quantity": 10,
      "purchase_price": 150.00
    }
  ]
}
```

---

### **>> Add Stock to Portfolio**
**Endpoint:**  
```
POST /api/portfolio/add
```
**Headers:**  
```http
Authorization: Bearer <access_token>
Content-Type: application/json
```
**Request Body (JSON):**  
```json
{
  "symbol": "AAPL",
  "quantity": 10,
  "purchase_price": 150.00
}
```
**Response (Success - 201 Created):**  
```json
{
  "id": 1,
  "symbol": "AAPL",
  "quantity": 10,
  "purchase_price": 150.00
}
```

---

### **>> Remove Stock from Portfolio**
**Endpoint:**  
```
DELETE /api/portfolio/<stockId>/delete
```
**Headers:**  
```http
Authorization: Bearer <access_token>
```
**Response (Success - 204 No Content):**  
```json
{}
```

---

### **>> Update Stock Details in Portfolio**
**Endpoint:**  
```
PUT /api/portfolio/<tockId>/update
```
**Headers:**  
```http
Authorization: Bearer <access_token>
Content-Type: application/json
```
**Request Body (JSON):**  
```json
{
  "quantity": 15,
  "purchase_price": 155.00
}
```
**Response (Success - 200 OK):**  
```json
{
  "id": 1,
  "symbol": "AAPL",
  "quantity": 15,
  "purchase_price": 155.00
}
```

---

### **>> Get Portfolio Performance**
**Endpoint:**  
```
GET /api/portfolio/performance
```
**Headers:**  
```http
Authorization: Bearer <access_token>
```
**Response (Success - 200 OK):**  
```json
{
  "total_value": 15000.50,
  "total_gain": 500.25,
  "percentage_change": 3.45
}
```

---

## **>> Summary**

| Action | Endpoint | Method | Required Fields |
|--------|----------|--------|----------------|
| Get Portfolio | `/api/portfolio` | `GET` | `Authorization: Bearer <access_token>` |
| Add Stock | `/api/portfolio/add` | `POST` | `Authorization: Bearer <access_token>`, `symbol`, `quantity`, `purchase_price` |
| Remove Stock | `/api/portfolio/{stockId}` | `DELETE` | `Authorization: Bearer <access_token>` |
| Update Stock | `/api/portfolio/{stockId}` | `PUT` | `Authorization: Bearer <access_token>`, `quantity`, `purchase_price` |
| Get Portfolio Performance | `/api/portfolio/performance` | `GET` | `Authorization: Bearer <access_token>` |

---


