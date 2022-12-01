import fs from "fs";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const Day1 = () => {
  console.log("************ Day 1 ************");
  fs.readFile(path.join(__dirname, "input.txt"), "utf8", (err, data) => {
    if (err) throw err;
    const parsed = data
      .split("\n\n")
      .map(p => p.split('\n').map(l => parseInt(l)).flat())
      .map(p => p.reduce((a, b) => a + b, 0))
      .sort((a, b) => b - a);

    console.log("First part: ", parsed[0]);
    console.log("Second part: ", parsed[0] + parsed[1] + parsed[2]);
  });
};
