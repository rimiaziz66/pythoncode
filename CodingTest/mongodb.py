import pytest
from pymongo import MongoClient

@pytest.fixture
def db():
    # Setup: Create a connection to the MongoDB client
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test_db
    collection = db.test_collection
    yield collection  # This will provide the collection to the tests
    # Teardown: Drop the collection after tests
    collection.drop()
    client.close()

def test_create(db):
    # Insert a document into the collection
    db.insert_one({"name": "John", "age": 30})
    # Verify the document was inserted
    doc = db.find_one({"name": "John"})
    assert doc is not None
    assert doc["name"] == "John"
    assert doc["age"] == 30

def test_read(db):
    # Insert a document
    db.insert_one({"name": "John", "age": 30})
    # Retrieve the document and verify it
    doc = db.find_one({"name": "John"})
    assert doc["name"] == "John"
    assert doc["age"] == 30

def test_update(db):
    # Insert a document
    db.insert_one({"name": "John", "age": 30})
    # Update the document
    db.update_one({"name": "John"}, {"$set": {"age": 31}})
    # Verify the update
    doc = db.find_one({"name": "John"})
    assert doc["age"] == 31

def test_delete(db):
    # Insert a document
    db.insert_one({"name": "John", "age": 30})
    # Delete the document
    db.delete_one({"name": "John"})
    # Verify the document is deleted
    doc = db.find_one({"name": "John"})
    assert doc is None
