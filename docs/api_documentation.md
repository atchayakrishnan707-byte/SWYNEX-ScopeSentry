
# ScopeSentry – REST API Documentation

## 1. API Overview

ScopeSentry uses REST APIs developed with Python FastAPI.

Base URL (local development):

http://localhost:8000/api

All protected endpoints require valid authentication.

## 2. Authentication APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /auth/register | Register user |
| POST | /auth/login | User login |
| POST | /auth/refresh | Refresh token |
| POST | /auth/logout | Logout |
| GET | /auth/me | Get current user |

## 3. Organization APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /organizations | Create organization |
| GET | /organizations/me | View organization |
| PUT | /organizations/{id} | Update organization |
| GET | /organizations/{id}/members | List members |
| POST | /organizations/{id}/members | Invite members |

## 4. Project APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /projects | Create project |
| GET | /projects | List projects |
| GET | /projects/{id} | View project |
| PUT | /projects/{id} | Update project |
| DELETE | /projects/{id} | Archive project |

## 5. Document APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /projects/{id}/documents | Upload agreement |
| GET | /projects/{id}/documents | List documents |
| GET | /documents/{id} | View document |
| POST | /documents/{id}/analyze | Extract requirements |
| GET | /analysis-jobs/{id} | Check processing status |

## 6. Requirement APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /projects/{id}/requirements | Add requirement |
| GET | /projects/{id}/requirements | List requirements |
| PUT | /requirements/{id} | Update draft requirement |
| DELETE | /requirements/{id} | Remove draft requirement |
| POST | /projects/{id}/baseline/confirm | Confirm original scope |
| GET | /projects/{id}/baseline | View baseline |

## 7. Change Request APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /projects/{id}/changes | Submit change |
| GET | /projects/{id}/changes | List changes |
| GET | /changes/{id} | View change |
| POST | /changes/{id}/analyze | Analyze scope |
| PUT | /changes/{id} | Update request |
| POST | /changes/{id}/comments | Add comment |

## 8. Impact Analysis APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /changes/{id}/impact | Calculate impact |
| GET | /changes/{id}/impact | View impact report |
| PUT | /changes/{id}/impact | Update estimates |

## 9. Approval APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /changes/{id}/approve | Approve change |
| POST | /changes/{id}/reject | Reject change |
| POST | /changes/{id}/request-clarification | Request clarification |
| GET | /projects/{id}/approvals | View approval history |

## 10. Dashboard and Reporting APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /dashboard/overview | Dashboard statistics |
| GET | /projects/{id}/health | Project health score |
| GET | /projects/{id}/audit-logs | Change history |
| GET | /projects/{id}/reports | Generate reports |
| GET | /notifications | View notifications |

## 11. Authentication and Authorization

- JWT tokens are used to authenticate users.
- Role-Based Access Control determines user permissions.
- Project-specific APIs verify organization membership.
- Clients and developers cannot perform unauthorized approval actions.
- Sensitive information is accessible only to authorized users.

## 12. Error Handling

Recommended HTTP status codes:

| Status | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 400 | Invalid request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Internal server error |

## 13. API Testing

APIs will be tested using Postman and FastAPI's automatic Swagger documentation.

Local Swagger URL:

http://localhost:8000/docs

Note: These endpoints describe the planned API contract. They will become available as their backend modules are implemented.
