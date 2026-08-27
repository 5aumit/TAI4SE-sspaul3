from flask_restful import Resource
from flask import jsonify
import logging


class OpenCvConfigurationData(Resource):
    def __init__(self, **kwargs):
        self.matcher = kwargs['matcher']
        self.extractor = self._get_object_name_with_package(kwargs['extractor'])
        self.log = logging.getLogger('vse.OpenCvConfigurationData')

    def get(self):
        json = jsonify(
            extractor=self.extractor,
            matcher_type=self.matcher['matcher_type'],
            norm_type=self.matcher['norm_type']
        )
        self.log.info('OpenCV configuration data request')
        return json

    @classmethod
    def _get_object_name_with_package(cls, obj):
        return obj.__class__.__module__ + '.' + type(obj).__name__
