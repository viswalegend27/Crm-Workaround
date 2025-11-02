# Client Resource Management (CRM) Application

This is a simple Client Resource Management (CRM) application built with Django.

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd client-resource-management
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv crm
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        .\crm\Scripts\activate
        ```

    *   **On macOS/Linux:**

        ```bash
        source crm/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply database migrations:**

    ```bash
    python my_crm/manage.py makemigrations
    python my_crm/manage.py migrate
    ```

6.  **Create a superuser (optional, for admin access):**

    ```bash
    python my_crm/manage.py createsuperuser
    ```

## Running the Application

To run the Django development server, make sure your virtual environment is activated and then execute:

```bash
python my_crm/manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/` in your web browser.