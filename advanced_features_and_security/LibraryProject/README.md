# LibraryProject - Book Store App

This is a simple Django project for learning how to build a bookstore application.

## How to run
1. Open the project folder in your terminal.
2. Run the server:
3. Open your browser and go to:
- Home page → http://127.0.0.1:8000/
- Books app → http://127.0.0.1:8000/books/
- Admin page → http://127.0.0.1:8000/admin/


# Permissions and Groups Setup

This project uses **custom permissions and groups** to control access.

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):

- `can_view` → Allows viewing book instances.
- `can_create` → Allows creating new book instances.
- `can_edit` → Allows editing existing book instances.
- `can_delete` → Allows deleting book instances.

## Groups
Configured via Django Admin (`/admin/`):

- **Viewers**: Assigned `can_view`.
- **Editors**: Assigned `can_view`, `can_create`, `can_edit`.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Usage in Views
In `bookshelf/views.py`:
- `@login_required` → Ensures user is logged in.
- `@permission_required("bookshelf.can_create", raise_exception=True)` → Ensures user has required permission.

## Testing
1. Create users in Django Admin.
2. Assign them to one of the groups (Viewers, Editors, Admins).
3. Log in as those users and access:
   - `/view_books/` → requires login.
   - `/create_book/` → requires `can_create`.
   - `/edit_book/` → requires `can_edit`.
   - `/delete_book/` → requires `can_delete`.

If a user lacks permission, they will be redirected to the login page or shown a **403 Forbidden** error.
