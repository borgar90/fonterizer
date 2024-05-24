const express = require("express");
const fileUpload = require("express-fileupload");
const { createFontFromImage } = require("./fontGenerator"); // Hypothetical module you'd create

const app = express();
app.use(fileUpload());

app.post("/upload", (req, res) => {
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send("No files were uploaded.");
  }

  let sampleImage = req.files.sampleImage;

  createFontFromImage(sampleImage.data)
    .then((fontFilePath) => {
      res.download(fontFilePath); // Provide the generated font file for download
    })
    .catch((err) => {
      res.status(500).send("Error processing image");
    });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
