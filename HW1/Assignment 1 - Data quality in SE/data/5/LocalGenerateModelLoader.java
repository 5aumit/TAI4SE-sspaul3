package info.xpanda.commons.generate.engine.model.local;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import info.xpanda.commons.generate.engine.configuration.ConfigurationHolder;
import info.xpanda.commons.generate.engine.model.GenerateModel;
import info.xpanda.commons.generate.engine.model.GenerateModelLoader;

import java.io.File;
import java.io.IOException;
import java.util.List;

/**
 * description:
 * copyright:
 *
 * @author Marek Solvang
 * @since 20190302
 */
public class LocalGenerateModelLoader implements GenerateModelLoader {
    private String path;

    public LocalGenerateModelLoader() {
        this.path = ConfigurationHolder.getConfiguration().getModelLoader().getSettings().get("path");
    }

    @Override
    public List<GenerateModel> load() {
        try {
            return new ObjectMapper().readValue(new File(path), new TypeReference<List<GenerateModel>>() {});
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
