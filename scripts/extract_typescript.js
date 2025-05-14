const ts = require("typescript");
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

function extractFromFile(filePath) {
  const source = fs.readFileSync(filePath, "utf8");
  const sourceFile = ts.createSourceFile(filePath, source, ts.ScriptTarget.Latest, true);

  const dom = new JSDOM("<?xml version=\"1.0\"?><Application name=\"auto_extracted\" domain=\"typescript\"></Application>");
  const app = dom.window.document.querySelector("Application");
  const component = dom.window.document.createElement("Component");
  component.setAttribute("name", path.basename(filePath, ".ts"));
  component.setAttribute("description", "Extracted from TypeScript module");

  function visit(node) {
    if (ts.isFunctionDeclaration(node) && node.name) {
      const func = dom.window.document.createElement("Function");
      func.setAttribute("name", node.name.text);
      func.setAttribute("method", "N/A");
      func.setAttribute("path", "N/A");

      const desc = dom.window.document.createElement("Description");
      desc.textContent = `Function ${node.name.text} extracted from ${filePath}`;
      func.appendChild(desc);

      func.appendChild(dom.window.document.createElement("Returns"));
      func.appendChild(dom.window.document.createElement("Calls"));
      func.appendChild(dom.window.document.createElement("CalledBy"));
      component.appendChild(func);
    }

    if (ts.isClassDeclaration(node) && node.name) {
      const type = dom.window.document.createElement("Type");
      type.setAttribute("name", node.name.text);
      type.setAttribute("kind", "object");
      node.members.forEach(member => {
        if (ts.isPropertyDeclaration(member) && member.name) {
          const prop = dom.window.document.createElement("Property");
          prop.setAttribute("name", member.name.getText());
          prop.setAttribute("type", "unknown");
          prop.setAttribute("required", "true");
          type.appendChild(prop);
        }
      });
      component.appendChild(type);
    }

    ts.forEachChild(node, visit);
  }

  visit(sourceFile);
  app.appendChild(component);
  const serializer = new dom.window.XMLSerializer();
  return serializer.serializeToString(app);
}

function main() {
  const inputPath = process.argv[2];
  const stat = fs.statSync(inputPath);
  const files = [];

  if (stat.isDirectory()) {
    function walk(dir) {
      fs.readdirSync(dir).forEach(file => {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
          walk(fullPath);
        } else if (file.endsWith(".ts")) {
          files.push(fullPath);
        }
      });
    }
    walk(inputPath);
  } else if (inputPath.endsWith(".ts")) {
    files.push(inputPath);
  }

  files.forEach(file => {
    const xml = extractFromFile(file);
    const outPath = path.basename(file, ".ts") + ".xml";
    fs.writeFileSync(outPath, xml, "utf8");
    console.log(`Extracted XML: ${outPath}`);
  });
}

main();
