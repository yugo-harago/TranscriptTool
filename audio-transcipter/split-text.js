import fs from "fs";

const result = [];

function splitText(text) {
  text = text.replace("\n", "<br>");
  const delimiterRegex = /([。、！？\n\{\}\[\]「」])/;
  const splittedText = text
    .split(delimiterRegex)
    .filter((chunk) => chunk.trim() !== "");

  return splittedText;
}

fs.readFile("./public/DazaiOsamu_Uso.txt", "utf-8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const spplited = splitText(data);
  for (const word of spplited) {
    result.push(
      "<span click=\"wordClick('" + word + "')\">" + word + "</span>"
    );
  }
  console.log(result.join(""));
});

fs.writeFileSync(
  "./public/DazaiOsamu_Uso.html",
  result.join(""),
  "utf-8",
  (err) => {
    if (err) {
      console.error("Error writing file:", err);
      return;
    }
    console.log("The file has been saved!");
  }
);
