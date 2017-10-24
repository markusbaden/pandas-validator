import pandas as pd
from ..core.exceptions import ValidationError


class BaseIndexValidator(object):
    def __init__(self, size=None, type=None, values=None):

        if values is not None and size is None:
            size = len(values)

        if values is not None and type is None:
            type = pd.Index(values).dtype

        self.size = size
        self.type = type
        self.values = values

    def validate(self, index):
        self._check_size(index)
        self._check_type(index)
        self._check_values(index)

    def _check_size(self, index):
        if self.size is not None and index.size != self.size:
            raise ValidationError('Index has the different size.')

    def _check_type(self, index):
        if self.type is not None and index.dtype.type != self.type:
            raise ValidationError('Index has the different type.')

    def _check_values(self, index):
        if self.values is not None and not (index == self.values).all():
            raise ValidationError('Index has different values')

    def is_valid(self, index):
        try:
            self.validate(index)
        except ValidationError:
            return False
        else:
            return True


class IndexValidator(BaseIndexValidator):
    pass


class ColumnsValidator(BaseIndexValidator):
    pass

