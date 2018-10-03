import json

from betamax.serializers.json_serializer import JSONSerializer


class JSONBodySerializer(JSONSerializer):
    name = 'json_body'
    stored_as_binary = False

    def _get_content_type(self, ct):
        return ct[0].split(';')[0].strip().lower()

    def _add_json_body(self, r):
        body_string = r['body'].get('string')
        if body_string:
            content_type = self._get_content_type(r['headers']['Content-Type'])
            if content_type == 'application/json':
                r['json_body'] = json.loads(body_string)

    def serialize(self, cassette_data):
        for interaction in cassette_data['http_interactions']:
            self._add_json_body(interaction['request'])
            self._add_json_body(interaction['response'])

        return json.dumps(
            cassette_data,
            sort_keys=True,
            indent=2,
            separators=(',', ': '),
        )
