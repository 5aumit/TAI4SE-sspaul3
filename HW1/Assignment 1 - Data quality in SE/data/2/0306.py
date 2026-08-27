from rest_framework import serializers


class BillBaseSerializer(serializers.Serializer):

    vendor = serializers.CharField(required=False)
    amount = serializers.FloatField()
    bill_date = serializers.DateField()
    due_date = serializers.DateField()


class BillListSerializer(BillBaseSerializer):

    id = serializers.SerializerMethodField()

    def get_id(self, object):
        return object.key.id()


class BillCreateSerializer(BillBaseSerializer):

    line_items = serializers.JSONField(default=None)
    company = serializers.CharField()
    branch = serializers.CharField()
    status = serializers.IntegerField()
    date_of_payment = serializers.DateField(default=None)
    notes = serializers.CharField(max_length=500, default=None)


class BillPaymentSerializer(serializers.Serializer):

    status = serializers.IntegerField()
    date_of_payment = serializers.DateField(required=True)
    notes = serializers.CharField(max_length=500, required=False)


class BillDetailSerializer(BillCreateSerializer, BillListSerializer):

    created_by = serializers.CharField(default=None)
    created_on = serializers.DateField(default=None)
    updated_by = serializers.CharField(default=None)
    updated_on = serializers.DateField(default=None)

