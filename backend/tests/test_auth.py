"""Tests for authentication endpoints."""
import pytest
from fastapi.testclient import TestClient

def test_register_user(client: TestClient):
    """Test user registration."""
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "test@example.com"

def test_register_duplicate_email(client: TestClient):
    """Test duplicate email registration."""
    # First registration
    client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword123"
        }
    )
    
    # Duplicate registration
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "name": "Another User",
            "password": "anotherpassword123"
        }
    )
    assert response.status_code == 400

def test_login_user(client: TestClient):
    """Test user login."""
    # Register user first
    client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "name": "Test User",
            "password": "testpassword123"
        }
    )
    
    # Login
    response = client.post(
        "/api/auth/login",
        json={
            "email": "test@example.com",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_login_invalid_credentials(client: TestClient):
    """Test login with invalid credentials."""
    response = client.post(
        "/api/auth/login",
        json={
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
