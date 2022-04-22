const standardVersionUpdaterYaml = require.resolve("standard-version-updater-yaml");

module.exports = {
  bumpFiles: [
    {
      "filename": "package.json",
      "type": "json"
    },
    {
      filename: "tripstagger/Chart.yaml",
      updater: standardVersionUpdaterYaml
    }
  ]
};