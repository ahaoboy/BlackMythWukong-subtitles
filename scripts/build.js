const fs = require('node:fs')
const path = require('node:path')

const CN_ROOT = path.resolve("./Chinese")
const CN_JSON_PATH = path.resolve("./dist/cn.json")
const CN_JS_PATH = path.resolve("./dist/cn.js")

const EN_ROOT = path.resolve("./English(US)")
const EN_JSON_PATH = path.resolve("./dist/en.json")
const EN_JS_PATH = path.resolve("./dist/en.js")

if (!fs.existsSync("./dist")) {
  fs.mkdirSync("./dist")
}

function build(root, json_output, js_ouput) {
  const json = {}
  for (const d of fs.readdirSync((root))) {
    const p = path.join(root, d)
    json[d] = {}
    for (const name of fs.readdirSync(p)) {
      const txt = fs.readFileSync(path.join(p, name), 'utf8')
      json[d][name.split(".")[0]] = txt
    }
  }

  const txt = JSON.stringify(json)
  fs.writeFileSync(json_output, txt)

  const js = `export default ${txt}`
  fs.writeFileSync(js_ouput, js)
}

build(CN_ROOT, CN_JSON_PATH, CN_JS_PATH)
build(EN_ROOT, EN_JSON_PATH, EN_JS_PATH)

