from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from .exceptions import ValidationError
from .constraint import Constraint

class MaxConstraint(Constraint):
    id = Column(Integer, ForeignKey('constraint.id'), primary_key=True)
    min = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'max_constraint',
    }

    def validate(self, value):
        if not value:
            raise ValidationError()

        if isinstance(value, int):
            if value > self.min:
                raise ValidationError()

        elif isinstance(value, list):
            if len(value) > self.max:
                raise ValidationError()