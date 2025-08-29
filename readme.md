# Type Measurement Calculator

A simple web application to calculate millimeters (mm) to points (pt), two common units of measurement in typography. This tool is useful for designers, typographers, and anyone working with print or digital media that requires precise measurements.

## Features

*   Calculate millimeters to points.
*   Calculate points to millimeters.
*   Simple and intuitive web interface.
*   REST API for programmatic conversions.
*   API documentation using Swagger UI.

## Technologies Used

*   **Backend:**
    *   Python
    *   Django
    *   Django REST Framework
    *   drf-spectacular (for API documentation)
*   **Database:**
    *   PostgreSQL (via psycopg2-binary)
*   **Frontend:**
    *   HTML
    *   CSS
    *   JavaScript (with jQuery)

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:8000/`.
2.  Select the conversion type (Millimeters to Points or Points to Millimeters).
3.  Enter the value you want to calculate in the input field.
4.  Click the "Calculate" button to see the result.

## API Endpoints

The application provides a REST API for conversions.

### `POST /api/calculate/`

This endpoint converts a value from one unit to another.

**Request Body:**

*   `conversion_type` (string, required): The type of conversion. Must be either `"mm_to_points"` or `"points_to_mm"`.
*   `value` (number, required): The value to be converted.

**Example Request:**

```json
{
    "conversion_type": "mm_to_points",
    "value": 10
}
```

**Example Response:**

```json
{
    "result": "10 mm is approximately 28.35 points",
    "value": 28.35
}
```

### API Documentation

The API is documented using Swagger UI. You can access the documentation at `http://127.0.0.1:8000/api/docs/`.
