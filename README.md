# Authentication API
| Action | Endpoint | Method | Required Fields |
|---------|----------|--------|-----------------|
| register | `/api/auth/register/` | `POST` | `username`, `email`, `password`, `first_name`, `last_name` |
| login | `/api/auth/login/` | `POST` | `username`, `password` |
| get user | `/api/auth/user/` | `GET` | `Authorization: Bearer <access_token>` |
| logout | `/api/auth/logout/` | `POST` | `refresh` token in request body |

---

# Stocks API
| Action | Endpoint | Method | Required Parameters |
|---------|----------|--------|-----------------|
| get all stocks | `/api/stocks/` | `GET` | `none` |
| get stock data | `/api/stocks/<symbol>/` | `GET` | `symbol` |
| search stocks | `/api/stocks/search/<query>/` | `GET` | `query` |
| get stock history | `/api/stocks/<symbol>/history/` | `GET` | `symbol` |
| get trending stocks | `/api/stocks/trending/` | `GET` | `none` |

---

# Portfolio API
| Action | Endpoint | Method | Required Fields |
|---------|----------|--------|-----------------|
| get portfolio | `/api/portfolio/` | `GET` | `Authorization: Bearer <access_token>` |
| add stock | `/api/portfolio/add/` | `POST` | `Authorization: Bearer <access_token>`, `symbol`, `quantity`, `purchase_price` |
| remove stock | `/api/portfolio/{stockID}/delete/` | `DELETE` | `Authorization: Bearer <access_token>` |
| update stock | `/api/portfolio/{stockID}/update/` | `PUT` | `Authorization: Bearer <access_token>`, `quantity`, `purchase_price` |
| get performance | `/api/portfolio/performance/` | `GET` | `Authorization: Bearer <access_token>` |

---

# Users API
| Action | Endpoint | Method | Required Fields |
|---------|----------|--------|-----------------|
| update profile | `/api/users/profile/` | `PUT` | `Authorization: Bearer <access_token>`, `first_name`, `last_name`, `email` |
| get watchlist | `/api/users/watchlist/` | `GET` | `Authorization: Bearer <access_token>` |
| add watchlist | `/api/users/watchlist/add/` | `POST` | `Authorization: Bearer <access_token>`, `symbol`, `company_name` |
| remove watchlist | `/api/users/watchlist/{stockID}/delete/` | `DELETE` | `Authorization: Bearer <access_token>`, |

---
