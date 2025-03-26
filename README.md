# Authentication API
| Action | Endpoint | Method | Required Fields |
|--------|----------|--------|----------------|
| Register | `/api/auth/register` | `POST` | `username`, `email`, `password`, `first_name`, `last_name` |
| Login | `/api/auth/login` | `POST` | `username`, `password` |
| Get User | `/api/auth/user` | `GET` | `Authorization: Bearer <access_token>` |
| Logout | `/api/auth/logout` | `POST` | `refresh` token in request body |

---

# Stocks API
| Action | Endpoint | Method | Required Parameters |
|--------|----------|--------|--------------------|
| Get All Stocks | `/api/stocks/` | `GET` | None |
| Get Stock Data | `/api/stocks/<symbol>/` | `GET` | `symbol` |
| Search Stocks | `/api/stocks/search/<query>/` | `GET` | `query` |
| Get Stock History | `/api/stocks/<symbol>/history/` | `GET` | `symbol` |
| Get Trending Stocks | `/api/stocks/trending/` | `GET` | None |

---

# Portfolio API
| Action | Endpoint | Method | Required Fields |
|--------|----------|--------|----------------|
| Get Portfolio | `/api/portfolio` | `GET` | `Authorization: Bearer <access_token>` |
| Add Stock | `/api/portfolio/add` | `POST` | `Authorization: Bearer <access_token>`, `symbol`, `quantity`, `purchase_price` |
| Remove Stock | `/api/portfolio/{stockId}/delete` | `DELETE` | `Authorization: Bearer <access_token>` |
| Update Stock | `/api/portfolio/{stockId}/update` | `PUT` | `Authorization: Bearer <access_token>`, `quantity`, `purchase_price` |
| Get Portfolio Performance | `/api/portfolio/performance` | `GET` | `Authorization: Bearer <access_token>` |

---

# Users API
---
