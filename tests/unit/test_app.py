"""
This file (test_app.py) contains the unit tests for the Flask application.
"""
import pytest
from pydantic import ValidationError

from project.books.routes import BookModel


def test_validate_book_data_nominal():
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    book_data = BookModel(
        title='Malibu Rising',
        author='Taylor Jenkins Reid',
        rating='5'
    )
    assert book_data.title == 'Malibu Rising'
    assert book_data.author == 'Taylor Jenkins Reid'
    assert book_data.rating == 5


def test_validate_book_data_invalid_rating():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (invalid rating) is passed in
    THEN check that the validation raises a ValueError
    """
    with pytest.raises(ValueError):
        BookModel(
            title='Malibu Rising',
            author='Taylor Jenkins Reid',
            rating='6'  # Invalid
        )


def test_validate_book_data_invalid_title():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (invalid title) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        BookModel(
            title=[1, 2, 3],  # Invalid
            author='Taylor Jenkins Reid',
            rating='5'
        )


def test_validate_book_data_missing_inputs():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (missing input) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        BookModel()  # Missing input data!


def test_validate_book_data_missing_author():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data (missing author) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        BookModel(
            title='Malibu Rising',
            # Missing author!
            rating='6'  # Invalid
        )
