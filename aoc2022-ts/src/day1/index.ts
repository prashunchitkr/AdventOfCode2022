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
      .split("\n")
      .reduce<number[]>(
        (acc, curr) => {
          if (curr === "") return [...acc, -1];
          if (acc[acc.length - 1] === -1) return [...acc, parseInt(curr)];
          return [
            ...acc.slice(0, acc.length - 1),
            acc[acc.length - 1] + parseInt(curr),
          ];
        },
        [-1]
      )
      .sort((a, b) => b - a);
    console.log(`Part 1: ${parsed[0]}`);
    console.log(
      `Part 2: ${parsed.slice(0, 3).reduce((acc, curr) => acc + curr, 0)}`
    );
  });
};
