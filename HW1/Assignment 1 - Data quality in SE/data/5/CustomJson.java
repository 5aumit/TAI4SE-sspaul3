package com.adapter;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import com.fasterxml.jackson.databind.util.ISO8601DateFormat;

import java.io.IOException;
import java.util.Date;


public final class CustomJson {

    private CustomJson() {
    }


    public static class Deserializer extends JsonDeserializer<Date> {
        @Override
        public Date deserialize(com.fasterxml.jackson.core.JsonParser p, DeserializationContext ctxt) throws IOException, JsonProcessingException {
            return null;
        }
    }


    public static class Serializer extends com.fasterxml.jackson.databind.JsonSerializer<Date> {
        @Override
        public void serialize(Date value, com.fasterxml.jackson.core.JsonGenerator gen,
                              com.fasterxml.jackson.databind.SerializerProvider serializers) throws IOException, JsonProcessingException {
            String formattedValue;
            formattedValue = ISO8601DateFormat.getInstance().format(value);

            gen.writeString(formattedValue);
        }
    }
}
