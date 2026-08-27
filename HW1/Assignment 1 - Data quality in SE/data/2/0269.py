import pytest
from marshmallow import ValidationError

from aliceplex.schema import Person, PersonSchema, PersonStrictSchema


def test_person_schema_load(person_schema: PersonSchema):
    schema = person_schema
    load = schema.load({"name": "name", "photo": "photo"})
    assert load == Person(name="name", photo="photo")
    load = schema.load({"name": None, "photo": None})
    assert load == Person()
    load = schema.load({})
    assert load == Person()


def test_person_schema_dump(person_schema: PersonSchema):
    schema = person_schema
    dump = schema.dump(Person(name="name", photo="photo"))
    assert dump == {"name": "name", "photo": "photo"}
    dump = schema.dump(Person())
    assert dump == {"name": None, "photo": None}


def test_person_strict_schema_load(person_strict_schema: PersonStrictSchema):
    schema = person_strict_schema
    load = schema.load({"name": "name", "photo": "photo"})
    assert load == Person(name="name", photo="photo")
    load = schema.load({"name": "name"})
    assert load == Person(name="name")
    with pytest.raises(ValidationError):
        schema.load({"name": None, "photo": None})
    with pytest.raises(ValidationError):
        schema.load({})


def test_person_strict_schema_dump(person_strict_schema: PersonStrictSchema):
    schema = person_strict_schema
    dump = schema.dump(Person(name="name", photo="photo"))
    assert dump == {"name": "name", "photo": "photo"}
    dump = schema.dump(Person())
    assert dump == {"name": None, "photo": None}
