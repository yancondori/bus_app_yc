# Servicio de Usuarios

Este microservicio es responsable de gestionar las cuentas de usuario, la autenticación y los perfiles de usuario.

## Funcionalidad

*   Registro y autenticación de usuarios.
*   Gestión del perfil (actualizar nombre, email, teléfono).
*   Recuperación de contraseña.

## Tecnologías

*   Python
*   Flask/FastAPI (Elige uno)
*   SQLAlchemy (o un ORM similar)
*   PostgreSQL (u otra base de datos)
*   JWT (JSON Web Tokens) para la autenticación

## Configuración

(Marcador de posición para las instrucciones de configuración)
================================================
DOC API

## API Endpoints - Users Service

### 1. Register a New User

*   **Endpoint:** `/users/register`
*   **Method:** POST
*   **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "securePassword"
    }
    ```
*   **Success Response:**
    *   Code: 201
    *   Content:
        ```json
        {
            "message": "User registered successfully"
        }
        ```
*   **Error Responses:**
    *   Code: 400 BAD REQUEST
    *   Content:
        ```json
        {
            "message": "Email and password are required"
        }
        ```
    *   Code: 400 BAD REQUEST
    *   Content:
        ```json
        {
            "message": "Email already registered"
        }
        ```

### 2. Login User

*   **Endpoint:** `/users/login`
*   **Method:** POST
*   **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "securePassword"
    }
    ```
*   **Success Response:**
    *   Code: 200 OK
    *   Content:
        ```json
        {
            "message": "Login successful"
        }
        ```
*   **Error Responses:**
    *   Code: 400 BAD REQUEST
    *   Content:
        ```json
        {
            "message": "Email and password are required"
        }
        ```
    *   Code: 401 UNAUTHORIZED
    *   Content:
        ```json
        {
            "message": "Invalid credentials"
        }
        ```
