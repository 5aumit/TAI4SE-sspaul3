package eu.arrowhead.model.storage.model;

import com.fasterxml.jackson.annotation.JsonFormat;
import eu.arrowhead.model.storage.metadata.ModelElementMetadata;
import eu.arrowhead.model.storage.metadata.RepositoryMetadata;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;

import java.util.HashMap;
import java.util.Map;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Document(indexName = "model")
public class Model {

    @Id
    private String id;

    @Field(type = FieldType.Text, name = "name")
    private String name;

    @Field(type = FieldType.Text, name = "file_name")
    private String fileName;

    @Field(type = FieldType.Text, name = "description")
    private String description;

    @Field(type = FieldType.Text, name = "modeling_language")
    private String modelingLanguage;

    @Field(type = FieldType.Text, name = "path")
    private String path;

    @Field(type = FieldType.Text, name = "model")
    private String model;

    @Field(type = FieldType.Text, name = "c_model")
    private String cModel;

    @Field(type = FieldType.Nested, includeInParent = true, name = "elements")
    private ModelElementMetadata elements;

    @Field(type = FieldType.Nested, includeInParent = true, name = "repository")
    private RepositoryMetadata repository;

    @Field(type = FieldType.Object, name = "domains")
    Map<String, Double> domains = new HashMap<>();

    @Field(type = FieldType.Object, name = "versions")
    Map<String, Version> versions = new HashMap<>();

    @Field(type = FieldType.Text, name = "version_number")
    private String versionNumber = "1.0.0";

    @CreatedDate
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss.SSSZZ")
    private Long createdAt;

    @LastModifiedDate
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss.SSSZZ")
    private Long updatedAt;

    public Model(
            String name,
            String description,
            String path,
            String type,
            String repoUrl,
            String versionNumber,
            int stars,
            int forks,
            int branches) {
        this.name = name;
        this.description = description;
        this.path = path;
        this.modelingLanguage = type;
        this.versionNumber = versionNumber;
        this.repository = new RepositoryMetadata(repoUrl, stars, forks, branches);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Model target = (Model) o;
        return id.equals(target.getId());
    }
}
