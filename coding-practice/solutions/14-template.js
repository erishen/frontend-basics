function render(template, data) {
  return template.replace(/\{\{(\w+)\}\}/g, (_, key) => data[key.trim()] ?? "");
}

function renderDeep(template, data) {
  return template.replace(/\{\{([\w.]+)\}\}/g, (_, path) => {
    return path.trim().split(".").reduce((obj, key) => obj?.[key], data) ?? "";
  });
}

module.exports = { render, renderDeep };
