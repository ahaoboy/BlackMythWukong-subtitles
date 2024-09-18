const fs = require('node:fs')
const path = require('node:path')

const Root = path.resolve("./Chinese")
const JSON_NAME = path.resolve("./dist/index.json")

if(!fs.existsSync("./dist")){
  fs.mkdirSync("./dist")
}

const json = {}
for (const d of fs.readdirSync((Root))) {
  const p = path.join(Root, d)
  json[d] = {}
  for (const name of fs.readdirSync(p)) {
    const txt = fs.readFileSync(path.join(p, name), 'utf8')
    json[name] = txt
  }
}

const txt = JSON.stringify(json)
fs.writeFileSync(JSON_NAME, txt)