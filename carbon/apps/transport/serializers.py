from rest_framework import serializers


class TransportSerializer(serializers.Serializer):
    distance = serializers.CharField(max_length=256)
    duration = serializers.CharField(max_length=256)
    emissions = serializers.CharField(max_length=256)
    mode = serializers.CharField(max_length=256)

    # we change the endpoint response body (representation) to generate the data
    # inside a transport_mode object
    def to_representation(self, instance):
        representation = super(TransportSerializer, self).to_representation(instance)

        transports = {}

        transports.update(
            {
                f"{representation['mode']}": {
                    "distance": representation["distance"],
                    "duration": representation["duration"],
                    "emissions": representation["emissions"],
                }
            }
        )

        representation = transports

        return representation
